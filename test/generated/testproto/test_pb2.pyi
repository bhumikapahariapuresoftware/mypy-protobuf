"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import builtins
import concurrent.futures
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import google.protobuf.service
import test.test_generated_mypy
import testproto.inner.inner_pb2
import testproto.nested.nested_pb2
import testproto.nopackage_pb2
import testproto.test3_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _OuterEnum:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OuterEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OuterEnum.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FOO: _OuterEnum.ValueType  # 1
    """FOO"""

    BAR: _OuterEnum.ValueType  # 2
    """BAR"""

class OuterEnum(_OuterEnum, metaclass=_OuterEnumEnumTypeWrapper):
    """Outer Enum"""
    pass

FOO: OuterEnum.ValueType  # 1
"""FOO"""

BAR: OuterEnum.ValueType  # 2
"""BAR"""

global___OuterEnum = OuterEnum


class _NamingConflicts:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _NamingConflictsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NamingConflicts.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
class NamingConflicts(_NamingConflicts, metaclass=_NamingConflictsEnumTypeWrapper):
    """Naming conflicts!"""
    pass

Name: NamingConflicts.ValueType  # 1
Value: NamingConflicts.ValueType  # 2
keys: NamingConflicts.ValueType  # 3
values: NamingConflicts.ValueType  # 4
items: NamingConflicts.ValueType  # 5
"""See https://github.com/protocolbuffers/protobuf/issues/8803
proto itself generates broken code when DESCRIPTOR is there
DESCRIPTOR = 8;
"""

global___NamingConflicts = NamingConflicts


class Simple1(google.protobuf.message.Message):
    """Message with one of everything"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _InnerEnum:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _InnerEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Simple1._InnerEnum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        INNER1: Simple1._InnerEnum.ValueType  # 1
        """INNER1"""

        INNER2: Simple1._InnerEnum.ValueType  # 2
        """INNER2"""

    class InnerEnum(_InnerEnum, metaclass=_InnerEnumEnumTypeWrapper):
        """Inner Enum"""
        pass

    INNER1: Simple1.InnerEnum.ValueType  # 1
    """INNER1"""

    INNER2: Simple1.InnerEnum.ValueType  # 2
    """INNER2"""


    class InnerMessage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        def __init__(self,
            ) -> None: ...

    class EmailByUidEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Optional[builtins.int] = ...,
            value: typing.Optional[typing.Text] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    A_STRING_FIELD_NUMBER: builtins.int
    A_REPEATED_STRING_FIELD_NUMBER: builtins.int
    A_BOOLEAN_FIELD_NUMBER: builtins.int
    A_UINT32_FIELD_NUMBER: builtins.int
    A_ENUM_FIELD_NUMBER: builtins.int
    A_EXTERNAL_ENUM_FIELD_NUMBER: builtins.int
    A_INNER_FIELD_NUMBER: builtins.int
    A_NESTED_FIELD_NUMBER: builtins.int
    INNER_ENUM_FIELD_NUMBER: builtins.int
    REP_INNER_ENUM_FIELD_NUMBER: builtins.int
    INNER_MESSAGE_FIELD_NUMBER: builtins.int
    REP_INNER_MESSAGE_FIELD_NUMBER: builtins.int
    NO_PACKAGE_FIELD_NUMBER: builtins.int
    NESTED_ENUM_FIELD_NUMBER: builtins.int
    NESTED_MESSAGE_FIELD_NUMBER: builtins.int
    A_ONEOF_1_FIELD_NUMBER: builtins.int
    A_ONEOF_2_FIELD_NUMBER: builtins.int
    OUTER_MESSAGE_IN_ONEOF_FIELD_NUMBER: builtins.int
    OUTER_ENUM_IN_ONEOF_FIELD_NUMBER: builtins.int
    INNER_ENUM_IN_ONEOF_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    EMAIL_BY_UID_FIELD_NUMBER: builtins.int
    a_string: typing.Text
    @property
    def a_repeated_string(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    a_boolean: builtins.bool
    a_uint32: builtins.int
    a_enum: global___OuterEnum.ValueType
    a_external_enum: testproto.test3_pb2.OuterEnum.ValueType
    @property
    def a_inner(self) -> testproto.inner.inner_pb2.Inner: ...
    @property
    def a_nested(self) -> testproto.nested.nested_pb2.Nested: ...
    inner_enum: global___Simple1.InnerEnum.ValueType
    @property
    def rep_inner_enum(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___Simple1.InnerEnum.ValueType]: ...
    @property
    def inner_message(self) -> global___Simple1.InnerMessage: ...
    @property
    def rep_inner_message(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Simple1.InnerMessage]: ...
    @property
    def no_package(self) -> testproto.nopackage_pb2.NoPackage: ...
    nested_enum: testproto.nested.nested_pb2.AnotherNested.NestedEnum.ValueType
    @property
    def nested_message(self) -> testproto.nested.nested_pb2.AnotherNested.NestedMessage: ...
    a_oneof_1: typing.Text
    a_oneof_2: typing.Text
    @property
    def outer_message_in_oneof(self) -> global___Simple2: ...
    outer_enum_in_oneof: global___OuterEnum.ValueType
    inner_enum_in_oneof: global___Simple1.InnerEnum.ValueType
    user_id: test.test_generated_mypy.UserId
    email: test.test_generated_mypy.Email
    @property
    def email_by_uid(self) -> google.protobuf.internal.containers.ScalarMap[test.test_generated_mypy.UserId, test.test_generated_mypy.Email]: ...
    def __init__(self,
        *,
        a_string: typing.Optional[typing.Text] = ...,
        a_repeated_string: typing.Optional[typing.Iterable[typing.Text]] = ...,
        a_boolean: typing.Optional[builtins.bool] = ...,
        a_uint32: typing.Optional[builtins.int] = ...,
        a_enum: typing.Optional[global___OuterEnum.ValueType] = ...,
        a_external_enum: typing.Optional[testproto.test3_pb2.OuterEnum.ValueType] = ...,
        a_inner: typing.Optional[testproto.inner.inner_pb2.Inner] = ...,
        a_nested: typing.Optional[testproto.nested.nested_pb2.Nested] = ...,
        inner_enum: typing.Optional[global___Simple1.InnerEnum.ValueType] = ...,
        rep_inner_enum: typing.Optional[typing.Iterable[global___Simple1.InnerEnum.ValueType]] = ...,
        inner_message: typing.Optional[global___Simple1.InnerMessage] = ...,
        rep_inner_message: typing.Optional[typing.Iterable[global___Simple1.InnerMessage]] = ...,
        no_package: typing.Optional[testproto.nopackage_pb2.NoPackage] = ...,
        nested_enum: typing.Optional[testproto.nested.nested_pb2.AnotherNested.NestedEnum.ValueType] = ...,
        nested_message: typing.Optional[testproto.nested.nested_pb2.AnotherNested.NestedMessage] = ...,
        a_oneof_1: typing.Optional[typing.Text] = ...,
        a_oneof_2: typing.Optional[typing.Text] = ...,
        outer_message_in_oneof: typing.Optional[global___Simple2] = ...,
        outer_enum_in_oneof: typing.Optional[global___OuterEnum.ValueType] = ...,
        inner_enum_in_oneof: typing.Optional[global___Simple1.InnerEnum.ValueType] = ...,
        user_id: typing.Optional[test.test_generated_mypy.UserId] = ...,
        email: typing.Optional[test.test_generated_mypy.Email] = ...,
        email_by_uid: typing.Optional[typing.Mapping[test.test_generated_mypy.UserId, test.test_generated_mypy.Email]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["a_boolean",b"a_boolean","a_enum",b"a_enum","a_external_enum",b"a_external_enum","a_inner",b"a_inner","a_nested",b"a_nested","a_oneof",b"a_oneof","a_oneof_1",b"a_oneof_1","a_oneof_2",b"a_oneof_2","a_string",b"a_string","a_uint32",b"a_uint32","email",b"email","inner_enum",b"inner_enum","inner_enum_in_oneof",b"inner_enum_in_oneof","inner_message",b"inner_message","nested_enum",b"nested_enum","nested_message",b"nested_message","no_package",b"no_package","outer_enum_in_oneof",b"outer_enum_in_oneof","outer_message_in_oneof",b"outer_message_in_oneof","user_id",b"user_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["a_boolean",b"a_boolean","a_enum",b"a_enum","a_external_enum",b"a_external_enum","a_inner",b"a_inner","a_nested",b"a_nested","a_oneof",b"a_oneof","a_oneof_1",b"a_oneof_1","a_oneof_2",b"a_oneof_2","a_repeated_string",b"a_repeated_string","a_string",b"a_string","a_uint32",b"a_uint32","email",b"email","email_by_uid",b"email_by_uid","inner_enum",b"inner_enum","inner_enum_in_oneof",b"inner_enum_in_oneof","inner_message",b"inner_message","nested_enum",b"nested_enum","nested_message",b"nested_message","no_package",b"no_package","outer_enum_in_oneof",b"outer_enum_in_oneof","outer_message_in_oneof",b"outer_message_in_oneof","rep_inner_enum",b"rep_inner_enum","rep_inner_message",b"rep_inner_message","user_id",b"user_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["a_oneof",b"a_oneof"]) -> typing.Optional[typing_extensions.Literal["a_oneof_1","a_oneof_2","outer_message_in_oneof","outer_enum_in_oneof","inner_enum_in_oneof"]]: ...
global___Simple1 = Simple1

class Simple2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    A_STRING_FIELD_NUMBER: builtins.int
    a_string: typing.Text
    def __init__(self,
        *,
        a_string: typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["a_string",b"a_string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["a_string",b"a_string"]) -> None: ...
global___Simple2 = Simple2

class Extensions1(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXT1_STRING_FIELD_NUMBER: builtins.int
    ext1_string: typing.Text
    ext: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[global___Simple1, global___Extensions1]
    """ext"""

    def __init__(self,
        *,
        ext1_string: typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ext1_string",b"ext1_string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ext1_string",b"ext1_string"]) -> None: ...
global___Extensions1 = Extensions1

class Extensions2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FLAG_FIELD_NUMBER: builtins.int
    flag: builtins.bool
    foo: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[global___Simple1, global___Extensions2]
    """foo"""

    def __init__(self,
        *,
        flag: typing.Optional[builtins.bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["flag",b"flag"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["flag",b"flag"]) -> None: ...
global___Extensions2 = Extensions2

class _r_None(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALID_FIELD_NUMBER: builtins.int
    valid: builtins.int
    def __init__(self,
        *,
        valid: typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["valid",b"valid"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["valid",b"valid"]) -> None: ...
global____r_None = _r_None

class PythonReservedKeywords(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _finally:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _finallyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PythonReservedKeywords._finally.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        valid_in_finally: PythonReservedKeywords._finally.ValueType  # 2
    class _r_finally(_finally, metaclass=_finallyEnumTypeWrapper):
        pass

    valid_in_finally: PythonReservedKeywords._r_finally.ValueType  # 2

    class _r_lambda(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CONTINUE_FIELD_NUMBER: builtins.int
        VALID_FIELD_NUMBER: builtins.int
        valid: builtins.int
        def __init__(self,
            *,
            valid: typing.Optional[builtins.int] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["continue",b"continue","valid",b"valid"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["continue",b"continue","valid",b"valid"]) -> None: ...

    FROM_FIELD_NUMBER: builtins.int
    IN_FIELD_NUMBER: builtins.int
    IS_FIELD_NUMBER: builtins.int
    FOR_FIELD_NUMBER: builtins.int
    TRY_FIELD_NUMBER: builtins.int
    DEF_FIELD_NUMBER: builtins.int
    NONLOCAL_FIELD_NUMBER: builtins.int
    WHILE_FIELD_NUMBER: builtins.int
    AND_FIELD_NUMBER: builtins.int
    DEL_FIELD_NUMBER: builtins.int
    GLOBAL_FIELD_NUMBER: builtins.int
    NOT_FIELD_NUMBER: builtins.int
    WITH_FIELD_NUMBER: builtins.int
    AS_FIELD_NUMBER: builtins.int
    ELIF_FIELD_NUMBER: builtins.int
    IF_FIELD_NUMBER: builtins.int
    OR_FIELD_NUMBER: builtins.int
    YIELD_FIELD_NUMBER: builtins.int
    ASSERT_FIELD_NUMBER: builtins.int
    ELSE_FIELD_NUMBER: builtins.int
    IMPORT_FIELD_NUMBER: builtins.int
    PASS_FIELD_NUMBER: builtins.int
    BREAK_FIELD_NUMBER: builtins.int
    EXCEPT_FIELD_NUMBER: builtins.int
    RAISE_FIELD_NUMBER: builtins.int
    FALSE_FIELD_NUMBER: builtins.int
    TRUE_FIELD_NUMBER: builtins.int
    CLASS_FIELD_NUMBER: builtins.int
    NONE_FIELD_NUMBER: builtins.int
    VALID_FIELD_NUMBER: builtins.int
    @property
    def none(self) -> global____r_None:
        """Test unreserved identifiers w/ reserved message names"""
        pass
    valid: global___PythonReservedKeywords._r_finally.ValueType
    def __init__(self,
        *,
        none: typing.Optional[global____r_None] = ...,
        valid: typing.Optional[global___PythonReservedKeywords._r_finally.ValueType] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["False",b"False","True",b"True","and",b"and","as",b"as","assert",b"assert","break",b"break","class",b"class","def",b"def","del",b"del","elif",b"elif","else",b"else","except",b"except","for",b"for","from",b"from","global",b"global","if",b"if","import",b"import","in",b"in","is",b"is","none",b"none","nonlocal",b"nonlocal","not",b"not","or",b"or","pass",b"pass","raise",b"raise","try",b"try","valid",b"valid","while",b"while","with",b"with","yield",b"yield"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["False",b"False","True",b"True","and",b"and","as",b"as","assert",b"assert","break",b"break","class",b"class","def",b"def","del",b"del","elif",b"elif","else",b"else","except",b"except","for",b"for","from",b"from","global",b"global","if",b"if","import",b"import","in",b"in","is",b"is","none",b"none","nonlocal",b"nonlocal","not",b"not","or",b"or","pass",b"pass","raise",b"raise","try",b"try","valid",b"valid","while",b"while","with",b"with","yield",b"yield"]) -> None: ...
global___PythonReservedKeywords = PythonReservedKeywords

class PythonReservedKeywordsSmall(google.protobuf.message.Message):
    """Do one with just one arg - to make sure it's syntactically correct"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FROM_FIELD_NUMBER: builtins.int
    def __init__(self,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["from",b"from"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["from",b"from"]) -> None: ...
global___PythonReservedKeywordsSmall = PythonReservedKeywordsSmall

class SelfField(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SELF_FIELD_NUMBER: builtins.int
    self: builtins.int
    """Field self -> must generate an __init__ method w/ different name"""

    # pyright: reportSelfClsParameterName=false
    def __init__(self_,
        *,
        self: typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["self",b"self"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["self",b"self"]) -> None: ...
global___SelfField = SelfField

class PythonReservedKeywordsService(google.protobuf.service.Service, metaclass=abc.ABCMeta):
    """Method name is reserved"""
    @abc.abstractmethod
    def valid_method_name1(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global____r_None], None]],
    ) -> concurrent.futures.Future[global____r_None]:
        """valid_method_name1"""
        pass
    @abc.abstractmethod
    def valid_method_name2(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global___PythonReservedKeywords._r_lambda], None]],
    ) -> concurrent.futures.Future[global___PythonReservedKeywords._r_lambda]:
        """valid_method_name2"""
        pass
class PythonReservedKeywordsService_Stub(PythonReservedKeywordsService):
    """Method name is reserved"""
    def __init__(self, rpc_channel: google.protobuf.service.RpcChannel) -> None: ...
    def valid_method_name1(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global____r_None], None]],
    ) -> concurrent.futures.Future[global____r_None]:
        """valid_method_name1"""
        pass
    def valid_method_name2(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global___PythonReservedKeywords._r_lambda], None]],
    ) -> concurrent.futures.Future[global___PythonReservedKeywords._r_lambda]:
        """valid_method_name2"""
        pass
class ATestService(google.protobuf.service.Service, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Echo(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global___Simple2], None]],
    ) -> concurrent.futures.Future[global___Simple2]: ...
class ATestService_Stub(ATestService):
    def __init__(self, rpc_channel: google.protobuf.service.RpcChannel) -> None: ...
    def Echo(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global___Simple2], None]],
    ) -> concurrent.futures.Future[global___Simple2]: ...