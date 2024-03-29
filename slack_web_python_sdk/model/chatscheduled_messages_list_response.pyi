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


class ChatscheduledMessagesListResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Schema for successful response from chat.scheduledMessages.list method
    """


    class MetaOapg:
        required = {
            "scheduled_messages",
            "response_metadata",
            "ok",
        }
        
        class properties:
        
            @staticmethod
            def ok() -> typing.Type['DefsOkTrue']:
                return DefsOkTrue
        
            @staticmethod
            def response_metadata() -> typing.Type['ChatscheduledMessagesListResponseResponseMetadata']:
                return ChatscheduledMessagesListResponseResponseMetadata
        
            @staticmethod
            def scheduled_messages() -> typing.Type['ChatscheduledMessagesListResponseScheduledMessages']:
                return ChatscheduledMessagesListResponseScheduledMessages
            __annotations__ = {
                "ok": ok,
                "response_metadata": response_metadata,
                "scheduled_messages": scheduled_messages,
            }
    
    scheduled_messages: 'ChatscheduledMessagesListResponseScheduledMessages'
    response_metadata: 'ChatscheduledMessagesListResponseResponseMetadata'
    ok: 'DefsOkTrue'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response_metadata"]) -> 'ChatscheduledMessagesListResponseResponseMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduled_messages"]) -> 'ChatscheduledMessagesListResponseScheduledMessages': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ok", "response_metadata", "scheduled_messages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response_metadata"]) -> 'ChatscheduledMessagesListResponseResponseMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduled_messages"]) -> 'ChatscheduledMessagesListResponseScheduledMessages': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ok", "response_metadata", "scheduled_messages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scheduled_messages: 'ChatscheduledMessagesListResponseScheduledMessages',
        response_metadata: 'ChatscheduledMessagesListResponseResponseMetadata',
        ok: 'DefsOkTrue',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChatscheduledMessagesListResponse':
        return super().__new__(
            cls,
            *args,
            scheduled_messages=scheduled_messages,
            response_metadata=response_metadata,
            ok=ok,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.chatscheduled_messages_list_response_response_metadata import ChatscheduledMessagesListResponseResponseMetadata
from slack_web_python_sdk.model.chatscheduled_messages_list_response_scheduled_messages import ChatscheduledMessagesListResponseScheduledMessages
from slack_web_python_sdk.model.defs_ok_true import DefsOkTrue
