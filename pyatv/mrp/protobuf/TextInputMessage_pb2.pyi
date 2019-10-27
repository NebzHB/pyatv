# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class TextInputMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ActionType2(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> TextInputMessage.ActionType2: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[TextInputMessage.ActionType2]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, TextInputMessage.ActionType2]]: ...
        Unknown = typing___cast(TextInputMessage.ActionType2, 0)
        Insert = typing___cast(TextInputMessage.ActionType2, 1)
        Set = typing___cast(TextInputMessage.ActionType2, 2)
        Delete = typing___cast(TextInputMessage.ActionType2, 3)
        CleaRr = typing___cast(TextInputMessage.ActionType2, 4)
    Unknown = typing___cast(TextInputMessage.ActionType2, 0)
    Insert = typing___cast(TextInputMessage.ActionType2, 1)
    Set = typing___cast(TextInputMessage.ActionType2, 2)
    Delete = typing___cast(TextInputMessage.ActionType2, 3)
    CleaRr = typing___cast(TextInputMessage.ActionType2, 4)

    timestamp = ... # type: float
    text = ... # type: typing___Text

    def __init__(self,
        *,
        timestamp : typing___Optional[float] = None,
        text : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TextInputMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"text",u"timestamp"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"text",u"timestamp"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"text",b"text",u"timestamp",b"timestamp"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"text",b"text",u"timestamp",b"timestamp"]) -> None: ...

textInputMessage = ... # type: google___protobuf___descriptor___FieldDescriptor