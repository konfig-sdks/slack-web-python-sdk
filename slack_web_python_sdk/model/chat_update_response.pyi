# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from slack_web_python_sdk import schemas  # noqa: F401


class ChatUpdateResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Schema for successful response of chat.update method
    """


    class MetaOapg:
        required = {
            "channel",
            "text",
            "message",
            "ok",
            "ts",
        }
        
        class properties:
            channel = schemas.StrSchema
        
            @staticmethod
            def message() -> typing.Type['ChatUpdateResponseMessage']:
                return ChatUpdateResponseMessage
        
            @staticmethod
            def ok() -> typing.Type['DefsOkTrue']:
                return DefsOkTrue
            text = schemas.StrSchema
            ts = schemas.StrSchema
            __annotations__ = {
                "channel": channel,
                "message": message,
                "ok": ok,
                "text": text,
                "ts": ts,
            }
    
    channel: MetaOapg.properties.channel
    text: MetaOapg.properties.text
    message: 'ChatUpdateResponseMessage'
    ok: 'DefsOkTrue'
    ts: MetaOapg.properties.ts
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> 'ChatUpdateResponseMessage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ts"]) -> MetaOapg.properties.ts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel", "message", "ok", "text", "ts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> 'ChatUpdateResponseMessage': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ts"]) -> MetaOapg.properties.ts: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel", "message", "ok", "text", "ts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        channel: typing.Union[MetaOapg.properties.channel, str, ],
        text: typing.Union[MetaOapg.properties.text, str, ],
        message: 'ChatUpdateResponseMessage',
        ok: 'DefsOkTrue',
        ts: typing.Union[MetaOapg.properties.ts, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChatUpdateResponse':
        return super().__new__(
            cls,
            *args,
            channel=channel,
            text=text,
            message=message,
            ok=ok,
            ts=ts,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.chat_update_response_message import ChatUpdateResponseMessage
from slack_web_python_sdk.model.defs_ok_true import DefsOkTrue