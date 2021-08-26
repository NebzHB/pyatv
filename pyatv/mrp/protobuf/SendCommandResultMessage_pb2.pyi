"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import pyatv.mrp.protobuf.PlayerPath_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SendError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Enum(metaclass=_Enum):
        V = typing.NewType('V', builtins.int)

    NoError = SendError.Enum.V(0)
    ApplicationNotFound = SendError.Enum.V(1)
    ConnectionFailed = SendError.Enum.V(2)
    Ignored = SendError.Enum.V(3)
    CouldNotLaunchApplication = SendError.Enum.V(4)
    TimedOut = SendError.Enum.V(5)
    OriginDoesNotExist = SendError.Enum.V(6)
    InvalidOptions = SendError.Enum.V(7)
    NoCommandHandlers = SendError.Enum.V(8)
    ApplicationNotInstalled = SendError.Enum.V(9)

    class _Enum(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Enum.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        NoError = SendError.Enum.V(0)
        ApplicationNotFound = SendError.Enum.V(1)
        ConnectionFailed = SendError.Enum.V(2)
        Ignored = SendError.Enum.V(3)
        CouldNotLaunchApplication = SendError.Enum.V(4)
        TimedOut = SendError.Enum.V(5)
        OriginDoesNotExist = SendError.Enum.V(6)
        InvalidOptions = SendError.Enum.V(7)
        NoCommandHandlers = SendError.Enum.V(8)
        ApplicationNotInstalled = SendError.Enum.V(9)


    def __init__(self,
        ) -> None: ...
global___SendError = SendError

class HandlerReturnStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Enum(metaclass=_Enum):
        V = typing.NewType('V', builtins.int)

    Success = HandlerReturnStatus.Enum.V(0)
    NoSuchContent = HandlerReturnStatus.Enum.V(1)
    CommandFailed = HandlerReturnStatus.Enum.V(2)
    NoActionableNowPlayingItem = HandlerReturnStatus.Enum.V(10)
    DeviceNotFound = HandlerReturnStatus.Enum.V(20)
    UIKitLegacy = HandlerReturnStatus.Enum.V(3)
    SkipAdProhibited = HandlerReturnStatus.Enum.V(100)
    QueueIsUserCurated = HandlerReturnStatus.Enum.V(101)
    UserModifiedQueueDisabled = HandlerReturnStatus.Enum.V(102)
    UserQueueModificationNotSupportedForCurrentItem = HandlerReturnStatus.Enum.V(103)
    SubscriptionRequiredForSharedQueue = HandlerReturnStatus.Enum.V(104)

    class _Enum(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Enum.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        Success = HandlerReturnStatus.Enum.V(0)
        NoSuchContent = HandlerReturnStatus.Enum.V(1)
        CommandFailed = HandlerReturnStatus.Enum.V(2)
        NoActionableNowPlayingItem = HandlerReturnStatus.Enum.V(10)
        DeviceNotFound = HandlerReturnStatus.Enum.V(20)
        UIKitLegacy = HandlerReturnStatus.Enum.V(3)
        SkipAdProhibited = HandlerReturnStatus.Enum.V(100)
        QueueIsUserCurated = HandlerReturnStatus.Enum.V(101)
        UserModifiedQueueDisabled = HandlerReturnStatus.Enum.V(102)
        UserQueueModificationNotSupportedForCurrentItem = HandlerReturnStatus.Enum.V(103)
        SubscriptionRequiredForSharedQueue = HandlerReturnStatus.Enum.V(104)


    def __init__(self,
        ) -> None: ...
global___HandlerReturnStatus = HandlerReturnStatus

class SendCommandResultMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SENDERROR_FIELD_NUMBER: builtins.int
    HANDLERRETURNSTATUS_FIELD_NUMBER: builtins.int
    HANDLERRETURNSTATUSDATAS_FIELD_NUMBER: builtins.int
    COMMANDID_FIELD_NUMBER: builtins.int
    PLAYERPATH_FIELD_NUMBER: builtins.int
    sendError: global___SendError.Enum.V = ...
    handlerReturnStatus: global___HandlerReturnStatus.Enum.V = ...

    @property
    def handlerReturnStatusDatas(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    commandID: typing.Text = ...

    @property
    def playerPath(self) -> pyatv.mrp.protobuf.PlayerPath_pb2.PlayerPath: ...

    def __init__(self,
        *,
        sendError : typing.Optional[global___SendError.Enum.V] = ...,
        handlerReturnStatus : typing.Optional[global___HandlerReturnStatus.Enum.V] = ...,
        handlerReturnStatusDatas : typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        commandID : typing.Optional[typing.Text] = ...,
        playerPath : typing.Optional[pyatv.mrp.protobuf.PlayerPath_pb2.PlayerPath] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"commandID",b"commandID",u"handlerReturnStatus",b"handlerReturnStatus",u"playerPath",b"playerPath",u"sendError",b"sendError"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"commandID",b"commandID",u"handlerReturnStatus",b"handlerReturnStatus",u"handlerReturnStatusDatas",b"handlerReturnStatusDatas",u"playerPath",b"playerPath",u"sendError",b"sendError"]) -> None: ...
global___SendCommandResultMessage = SendCommandResultMessage

sendCommandResultMessage: google.protobuf.descriptor.FieldDescriptor = ...
