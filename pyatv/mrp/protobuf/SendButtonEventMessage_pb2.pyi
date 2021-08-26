"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SendButtonEventMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USAGEPAGE_FIELD_NUMBER: builtins.int
    USAGE_FIELD_NUMBER: builtins.int
    BUTTONDOWN_FIELD_NUMBER: builtins.int
    usagePage: builtins.int = ...
    usage: builtins.int = ...
    buttonDown: builtins.bool = ...

    def __init__(self,
        *,
        usagePage : typing.Optional[builtins.int] = ...,
        usage : typing.Optional[builtins.int] = ...,
        buttonDown : typing.Optional[builtins.bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"buttonDown",b"buttonDown",u"usage",b"usage",u"usagePage",b"usagePage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"buttonDown",b"buttonDown",u"usage",b"usage",u"usagePage",b"usagePage"]) -> None: ...
global___SendButtonEventMessage = SendButtonEventMessage

sendButtonEventMessage: google.protobuf.descriptor.FieldDescriptor = ...
