"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _OuterEnum:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OuterEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OuterEnum.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _OuterEnum.ValueType  # 0
    FOO3: _OuterEnum.ValueType  # 1
    BAR3: _OuterEnum.ValueType  # 2
class OuterEnum(_OuterEnum, metaclass=_OuterEnumEnumTypeWrapper):
    pass

UNKNOWN: OuterEnum.ValueType  # 0
FOO3: OuterEnum.ValueType  # 1
BAR3: OuterEnum.ValueType  # 2
global___OuterEnum = OuterEnum


class OuterMessage3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    A_STRING_FIELD_NUMBER: builtins.int
    a_string: typing.Text
    def __init__(self,
        *,
        a_string: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["a_string",b"a_string"]) -> None: ...
global___OuterMessage3 = OuterMessage3

class SimpleProto3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _InnerEnum:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _InnerEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SimpleProto3._InnerEnum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        INNER1: SimpleProto3._InnerEnum.ValueType  # 0
        INNER2: SimpleProto3._InnerEnum.ValueType  # 1
    class InnerEnum(_InnerEnum, metaclass=_InnerEnumEnumTypeWrapper):
        pass

    INNER1: SimpleProto3.InnerEnum.ValueType  # 0
    INNER2: SimpleProto3.InnerEnum.ValueType  # 1

    class MapScalarEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: typing.Text
        def __init__(self,
            *,
            key: builtins.int = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class MapMessageEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___OuterMessage3: ...
        def __init__(self,
            *,
            key: builtins.int = ...,
            value: global___OuterMessage3 | None = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    A_STRING_FIELD_NUMBER: builtins.int
    A_REPEATED_STRING_FIELD_NUMBER: builtins.int
    A_OUTER_ENUM_FIELD_NUMBER: builtins.int
    OUTER_MESSAGE_FIELD_NUMBER: builtins.int
    INNER_ENUM_FIELD_NUMBER: builtins.int
    A_ONEOF_1_FIELD_NUMBER: builtins.int
    A_ONEOF_2_FIELD_NUMBER: builtins.int
    OUTER_MESSAGE_IN_ONEOF_FIELD_NUMBER: builtins.int
    OUTER_ENUM_IN_ONEOF_FIELD_NUMBER: builtins.int
    INNER_ENUM_IN_ONEOF_FIELD_NUMBER: builtins.int
    B_ONEOF_1_FIELD_NUMBER: builtins.int
    B_ONEOF_2_FIELD_NUMBER: builtins.int
    BOOL_FIELD_NUMBER: builtins.int
    OUTERENUM_FIELD_NUMBER: builtins.int
    OUTERMESSAGE3_FIELD_NUMBER: builtins.int
    MAP_SCALAR_FIELD_NUMBER: builtins.int
    MAP_MESSAGE_FIELD_NUMBER: builtins.int
    AN_OPTIONAL_STRING_FIELD_NUMBER: builtins.int
    a_string: typing.Text
    @property
    def a_repeated_string(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    a_outer_enum: global___OuterEnum.ValueType
    @property
    def outer_message(self) -> global___OuterMessage3: ...
    inner_enum: global___SimpleProto3.InnerEnum.ValueType
    a_oneof_1: typing.Text
    a_oneof_2: typing.Text
    @property
    def outer_message_in_oneof(self) -> global___OuterMessage3: ...
    outer_enum_in_oneof: global___OuterEnum.ValueType
    inner_enum_in_oneof: global___SimpleProto3.InnerEnum.ValueType
    b_oneof_1: typing.Text
    b_oneof_2: typing.Text
    @property
    def bool(self) -> global___OuterMessage3: ...
    OuterEnum: global___OuterEnum.ValueType
    """Test having fieldname match messagename"""

    @property
    def OuterMessage3(self) -> global___OuterMessage3: ...
    @property
    def map_scalar(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, typing.Text]:
        """Test generation of map"""
        pass
    @property
    def map_message(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___OuterMessage3]: ...
    an_optional_string: typing.Text
    def __init__(self,
        *,
        a_string: typing.Text = ...,
        a_repeated_string: typing.Iterable[typing.Text] | None = ...,
        a_outer_enum: global___OuterEnum.ValueType = ...,
        outer_message: global___OuterMessage3 | None = ...,
        inner_enum: global___SimpleProto3.InnerEnum.ValueType = ...,
        a_oneof_1: typing.Text = ...,
        a_oneof_2: typing.Text = ...,
        outer_message_in_oneof: global___OuterMessage3 | None = ...,
        outer_enum_in_oneof: global___OuterEnum.ValueType = ...,
        inner_enum_in_oneof: global___SimpleProto3.InnerEnum.ValueType = ...,
        b_oneof_1: typing.Text = ...,
        b_oneof_2: typing.Text = ...,
        bool: global___OuterMessage3 | None = ...,
        OuterEnum: global___OuterEnum.ValueType = ...,
        OuterMessage3: global___OuterMessage3 | None = ...,
        map_scalar: typing.Mapping[builtins.int, typing.Text] | None = ...,
        map_message: typing.Mapping[builtins.int, global___OuterMessage3] | None = ...,
        an_optional_string: typing.Text | None = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["OuterMessage3",b"OuterMessage3","_an_optional_string",b"_an_optional_string","a_oneof",b"a_oneof","a_oneof_1",b"a_oneof_1","a_oneof_2",b"a_oneof_2","an_optional_string",b"an_optional_string","b_oneof",b"b_oneof","b_oneof_1",b"b_oneof_1","b_oneof_2",b"b_oneof_2","bool",b"bool","inner_enum_in_oneof",b"inner_enum_in_oneof","outer_enum_in_oneof",b"outer_enum_in_oneof","outer_message",b"outer_message","outer_message_in_oneof",b"outer_message_in_oneof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["OuterEnum",b"OuterEnum","OuterMessage3",b"OuterMessage3","_an_optional_string",b"_an_optional_string","a_oneof",b"a_oneof","a_oneof_1",b"a_oneof_1","a_oneof_2",b"a_oneof_2","a_outer_enum",b"a_outer_enum","a_repeated_string",b"a_repeated_string","a_string",b"a_string","an_optional_string",b"an_optional_string","b_oneof",b"b_oneof","b_oneof_1",b"b_oneof_1","b_oneof_2",b"b_oneof_2","bool",b"bool","inner_enum",b"inner_enum","inner_enum_in_oneof",b"inner_enum_in_oneof","map_message",b"map_message","map_scalar",b"map_scalar","outer_enum_in_oneof",b"outer_enum_in_oneof","outer_message",b"outer_message","outer_message_in_oneof",b"outer_message_in_oneof"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_an_optional_string",b"_an_optional_string"]) -> typing_extensions.Literal["an_optional_string"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["a_oneof",b"a_oneof"]) -> typing_extensions.Literal["a_oneof_1","a_oneof_2","outer_message_in_oneof","outer_enum_in_oneof","inner_enum_in_oneof"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["b_oneof",b"b_oneof"]) -> typing_extensions.Literal["b_oneof_1","b_oneof_2"] | None: ...
global___SimpleProto3 = SimpleProto3
