"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import pyatv.mrp.protobuf.Common_pb2
import pyatv.mrp.protobuf.NowPlayingInfo_pb2
import pyatv.mrp.protobuf.PlaybackQueueCapabilities_pb2
import pyatv.mrp.protobuf.PlaybackQueueRequestMessage_pb2
import pyatv.mrp.protobuf.PlaybackQueue_pb2
import pyatv.mrp.protobuf.PlayerPath_pb2
import pyatv.mrp.protobuf.SupportedCommands_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SetDefaultSupportedCommandsMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NOWPLAYINGINFO_FIELD_NUMBER: builtins.int
    SUPPORTEDCOMMANDS_FIELD_NUMBER: builtins.int
    PLAYBACKQUEUE_FIELD_NUMBER: builtins.int
    DISPLAYID_FIELD_NUMBER: builtins.int
    DISPLAYNAME_FIELD_NUMBER: builtins.int
    PLAYBACKSTATE_FIELD_NUMBER: builtins.int
    PLAYBACKQUEUECAPABILITIES_FIELD_NUMBER: builtins.int
    PLAYERPATH_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    PLAYBACKSTATETIMESTAMP_FIELD_NUMBER: builtins.int
    displayID: typing.Text = ...
    displayName: typing.Text = ...
    playbackState: pyatv.mrp.protobuf.Common_pb2.PlaybackState.Enum.V = ...
    playbackStateTimestamp: builtins.float = ...

    @property
    def nowPlayingInfo(self) -> pyatv.mrp.protobuf.NowPlayingInfo_pb2.NowPlayingInfo: ...

    @property
    def supportedCommands(self) -> pyatv.mrp.protobuf.SupportedCommands_pb2.SupportedCommands: ...

    @property
    def playbackQueue(self) -> pyatv.mrp.protobuf.PlaybackQueue_pb2.PlaybackQueue: ...

    @property
    def playbackQueueCapabilities(self) -> pyatv.mrp.protobuf.PlaybackQueueCapabilities_pb2.PlaybackQueueCapabilities: ...

    @property
    def playerPath(self) -> pyatv.mrp.protobuf.PlayerPath_pb2.PlayerPath: ...

    @property
    def request(self) -> pyatv.mrp.protobuf.PlaybackQueueRequestMessage_pb2.PlaybackQueueRequestMessage: ...

    def __init__(self,
        *,
        nowPlayingInfo : typing.Optional[pyatv.mrp.protobuf.NowPlayingInfo_pb2.NowPlayingInfo] = ...,
        supportedCommands : typing.Optional[pyatv.mrp.protobuf.SupportedCommands_pb2.SupportedCommands] = ...,
        playbackQueue : typing.Optional[pyatv.mrp.protobuf.PlaybackQueue_pb2.PlaybackQueue] = ...,
        displayID : typing.Optional[typing.Text] = ...,
        displayName : typing.Optional[typing.Text] = ...,
        playbackState : typing.Optional[pyatv.mrp.protobuf.Common_pb2.PlaybackState.Enum.V] = ...,
        playbackQueueCapabilities : typing.Optional[pyatv.mrp.protobuf.PlaybackQueueCapabilities_pb2.PlaybackQueueCapabilities] = ...,
        playerPath : typing.Optional[pyatv.mrp.protobuf.PlayerPath_pb2.PlayerPath] = ...,
        request : typing.Optional[pyatv.mrp.protobuf.PlaybackQueueRequestMessage_pb2.PlaybackQueueRequestMessage] = ...,
        playbackStateTimestamp : typing.Optional[builtins.float] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"displayID",b"displayID",u"displayName",b"displayName",u"nowPlayingInfo",b"nowPlayingInfo",u"playbackQueue",b"playbackQueue",u"playbackQueueCapabilities",b"playbackQueueCapabilities",u"playbackState",b"playbackState",u"playbackStateTimestamp",b"playbackStateTimestamp",u"playerPath",b"playerPath",u"request",b"request",u"supportedCommands",b"supportedCommands"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"displayID",b"displayID",u"displayName",b"displayName",u"nowPlayingInfo",b"nowPlayingInfo",u"playbackQueue",b"playbackQueue",u"playbackQueueCapabilities",b"playbackQueueCapabilities",u"playbackState",b"playbackState",u"playbackStateTimestamp",b"playbackStateTimestamp",u"playerPath",b"playerPath",u"request",b"request",u"supportedCommands",b"supportedCommands"]) -> None: ...
global___SetDefaultSupportedCommandsMessage = SetDefaultSupportedCommandsMessage

setDefaultSupportedCommandsMessage: google.protobuf.descriptor.FieldDescriptor = ...
