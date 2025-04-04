"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SetConnectionStateMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ConnectionState:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ConnectionStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SetConnectionStateMessage._ConnectionState.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Connecting: SetConnectionStateMessage._ConnectionState.ValueType  # 1
        Connected: SetConnectionStateMessage._ConnectionState.ValueType  # 2
        Disconnected: SetConnectionStateMessage._ConnectionState.ValueType  # 3

    class ConnectionState(_ConnectionState, metaclass=_ConnectionStateEnumTypeWrapper): ...
    Connecting: SetConnectionStateMessage.ConnectionState.ValueType  # 1
    Connected: SetConnectionStateMessage.ConnectionState.ValueType  # 2
    Disconnected: SetConnectionStateMessage.ConnectionState.ValueType  # 3

    STATE_FIELD_NUMBER: builtins.int
    state: global___SetConnectionStateMessage.ConnectionState.ValueType
    def __init__(
        self,
        *,
        state: global___SetConnectionStateMessage.ConnectionState.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["state", b"state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["state", b"state"]) -> None: ...

global___SetConnectionStateMessage = SetConnectionStateMessage

SETCONNECTIONSTATEMESSAGE_FIELD_NUMBER: builtins.int
setConnectionStateMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___SetConnectionStateMessage]
