#!/bin/bash -ex

RED="\033[0;31m"
NC='\033[0m'
if [ `uname -m` == "aarch64" ]; then
    PROTOC_ZIP=protoc-3.18.1-linux-aarch_64.zip
    curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v3.18.1/$PROTOC_ZIP
    unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
    unzip -o $PROTOC_ZIP -d /usr/local include/*
    PROTOC=${PROTOC:=protoc}
    echo $PROTOC
    echo $protoc
    PY_VER_MYPY_PROTOBUF=${PY_VER_MYPY_PROTOBUF:=3.8.11}
    PY_VER_MYPY_PROTOBUF_SHORT=$(echo $PY_VER_MYPY_PROTOBUF | cut -d. -f1-2)
    PY_VER_MYPY=${PY_VER_MYPY:=3.8.11}
    PY_VER_UNIT_TESTS="${PY_VER_UNIT_TESTS_3:=3.8.11}"
    pip install enum34 aenum
    PROTOC_ARGS="--proto_path=proto/ --experimental_allow_proto3_optional"
    GRPC_PROTOS=$(find proto/testproto/grpc -name "*.proto")
else
    PROTOC=${PROTOC:=protoc}
    PY_VER_MYPY_PROTOBUF=${PY_VER_MYPY_PROTOBUF:=3.8.11}
    PY_VER_MYPY_PROTOBUF_SHORT=$(echo $PY_VER_MYPY_PROTOBUF | cut -d. -f1-2)
    PY_VER_MYPY=${PY_VER_MYPY:=3.8.11}
    PY_VER_UNIT_TESTS="${PY_VER_UNIT_TESTS_3:=3.8.11}"
    PROTOC_ARGS="--proto_path=proto/ --experimental_allow_proto3_optional"
    GRPC_PROTOS=$(find proto/testproto/grpc -name "*.proto")

fi

# Clean out generated/ directory - except for .generated / __init__.py
find test/generated -type f -not \( -name "*.expected" -or -name "__init__.py" \) -delete

if [ -e $CUSTOM_TYPESHED_DIR ]; then
    export MYPYPATH=$CUSTOM_TYPESHED_DIR/stubs/protobuf
fi

# Create mypy venv
MYPY_VENV=venv_$PY_VER_MYPY
(
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    pyenv shell $PY_VER_MYPY

    if [[ -z $SKIP_CLEAN ]] || [[ ! -e $MYPY_VENV ]]; then
        python3 --version
        python3 -m pip --version
        python -m pip install virtualenv
        python3 -m virtualenv $MYPY_VENV
        $MYPY_VENV/bin/python3 -m pip install -r mypy_requirements.txt
    fi
    $MYPY_VENV/bin/mypy --version
)

# Create unit tests venvs
for PY_VER in $PY_VER_UNIT_TESTS; do
    (
        UNIT_TESTS_VENV=venv_$PY_VER
        eval "$(pyenv init --path)"
        eval "$(pyenv init -)"
        pyenv shell $PY_VER

        if [[ -z $SKIP_CLEAN ]] || [[ ! -e $UNIT_TESTS_VENV ]]; then
            python -m pip install virtualenv
            python -m virtualenv $UNIT_TESTS_VENV
            $UNIT_TESTS_VENV/bin/python -m pip install -r test_requirements.txt
        fi
        $UNIT_TESTS_VENV/bin/py.test --version
    )
done

# Create mypy-protobuf venv
MYPY_PROTOBUF_VENV=venv_$PY_VER_MYPY_PROTOBUF
(
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    pyenv shell $PY_VER_MYPY_PROTOBUF

    # Create virtualenv + Install requirements for mypy-protobuf
    if [[ -z $SKIP_CLEAN ]] || [[ ! -e $MYPY_PROTOBUF_VENV ]]; then
        python -m pip install virtualenv
        python -m virtualenv $MYPY_PROTOBUF_VENV
        $MYPY_PROTOBUF_VENV/bin/python -m pip install -e .
    fi
)

# Run mypy-protobuf
(
    source $MYPY_PROTOBUF_VENV/bin/activate

    # Confirm version number
    test "$(protoc-gen-mypy -V)" = "mypy-protobuf 3.0.0"
    test "$(protoc-gen-mypy --version)" = "mypy-protobuf 3.0.0"

    # Run mypy on mypy-protobuf internal code for developers to catch issues
    FILES="mypy_protobuf/main.py"
    $MYPY_VENV/bin/mypy --strict --custom-typeshed-dir=$CUSTOM_TYPESHED_DIR --python-executable=$MYPY_PROTOBUF_VENV/bin/python3 --python-version=$PY_VER_MYPY_PROTOBUF_SHORT --pretty --show-error-codes $FILES

    # Generate protos
    python --version
    $PROTOC --version
    expected="libprotoc 3.18.1"
    if [[ $($PROTOC --version) != $expected ]]; then
        echo -e "${RED}For tests - must install protoc version ${expected} ${NC}"
        exit 1
    fi

    PROTOC_ARGS="--proto_path=proto/ --experimental_allow_proto3_optional"
    # Compile protoc -> python
    $PROTOC $PROTOC_ARGS --python_out=test/generated `find proto -name "*.proto"`

    # Compile protoc -> mypy using mypy_protobuf
    # Prereq - create the mypy.proto python proto
    $PROTOC $PROTOC_ARGS --python_out=. `find proto/mypy_protobuf -name "*.proto"`
    $PROTOC $PROTOC_ARGS --mypy_out=. `find proto/mypy_protobuf -name "*.proto"`

    # Sanity check that our flags work
    $PROTOC $PROTOC_ARGS --mypy_out=quiet:test/generated `find proto -name "*.proto"`
    $PROTOC $PROTOC_ARGS --mypy_out=readable_stubs:test/generated `find proto -name "*.proto"`
    $PROTOC $PROTOC_ARGS --mypy_out=relax_strict_optional_primitives:test/generated `find proto -name "*.proto"`
    # Overwrite w/ run with mypy-protobuf without flags
    $PROTOC $PROTOC_ARGS --mypy_out=test/generated `find proto -name "*.proto"`

    # Compile GRPC
    GRPC_PROTOS=$(find proto/testproto/grpc -name "*.proto")
    $PROTOC $PROTOC_ARGS --mypy_grpc_out=test/generated $GRPC_PROTOS
    python -m grpc_tools.protoc $PROTOC_ARGS --grpc_python_out=test/generated $GRPC_PROTOS
)

for PY_VER in $PY_VER_UNIT_TESTS; do
    UNIT_TESTS_VENV=venv_$PY_VER
    PY_VER_MYPY_TARGET=$(echo $PY_VER | cut -d. -f1-2)

    # Run mypy on unit tests / generated output
    (
        source $MYPY_VENV/bin/activate

        # Run mypy
       
        FILES38="test/"
        FILES=$FILES38
        
        mypy --strict --custom-typeshed-dir=$CUSTOM_TYPESHED_DIR --python-executable=$UNIT_TESTS_VENV/bin/python --python-version=$PY_VER_MYPY_TARGET --pretty --show-error-codes $FILES

        # run mypy on negative-tests (expected mypy failures)
       
        NEGATIVE_FILES_38="test_negative/negative.py test_negative/negative_3.8.py $FILES38"
        NEGATIVE_FILES=$NEGATIVE_FILES_38
        
        MYPY_OUTPUT=`mktemp -d`
        call_mypy() {
            # Write output to file. Make variant w/ omitted line numbers for easy diffing / CR
            PY_VER_MYPY_TARGET=$(echo $1 | cut -d. -f1-2)
            mypy --strict --custom-typeshed-dir=$CUSTOM_TYPESHED_DIR --python-executable=venv_$1/bin/python --python-version=$PY_VER_MYPY_TARGET ${@: 2} > $MYPY_OUTPUT/mypy_output || true
            cut -d: -f1,3- $MYPY_OUTPUT/mypy_output > $MYPY_OUTPUT/mypy_output.omit_linenos
        }

        call_mypy $PY_VER $NEGATIVE_FILES
        if ! diff $MYPY_OUTPUT/mypy_output test_negative/output.expected.$PY_VER_MYPY_TARGET || ! diff $MYPY_OUTPUT/mypy_output.omit_linenos test_negative/output.expected.$PY_VER_MYPY_TARGET.omit_linenos; then
            echo -e "${RED}test_negative/output.expected.$PY_VER_MYPY_TARGET didnt match. Copying over for you. Now rerun${NC}"

            # Copy over all the mypy results for the developer.
            
            call_mypy 3.8.11 $NEGATIVE_FILES_38
            cp $MYPY_OUTPUT/mypy_output test_negative/output.expected.3.8
            cp $MYPY_OUTPUT/mypy_output.omit_linenos test_negative/output.expected.3.8.omit_linenos
            exit 1
        fi
    )

    (
        # Run unit tests. These tests generate .expected files
        source $UNIT_TESTS_VENV/bin/activate
        if [[ $PY_VER =~ ^2.* ]]; then IGNORE="--ignore=test/test_grpc_usage.py"; else IGNORE=""; fi
        PYTHONPATH=test/generated py.test --ignore=test/generated $IGNORE -v
    )
done
