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


class AdminconversationsGetConversationPrefsResponsePrefs(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def can_thread() -> typing.Type['AdminconversationsGetConversationPrefsResponsePrefsCanThread']:
                return AdminconversationsGetConversationPrefsResponsePrefsCanThread
        
            @staticmethod
            def who_can_post() -> typing.Type['AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost']:
                return AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost
            __annotations__ = {
                "can_thread": can_thread,
                "who_can_post": who_can_post,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_thread"]) -> 'AdminconversationsGetConversationPrefsResponsePrefsCanThread': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["who_can_post"]) -> 'AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["can_thread", "who_can_post", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_thread"]) -> typing.Union['AdminconversationsGetConversationPrefsResponsePrefsCanThread', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["who_can_post"]) -> typing.Union['AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["can_thread", "who_can_post", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        can_thread: typing.Union['AdminconversationsGetConversationPrefsResponsePrefsCanThread', schemas.Unset] = schemas.unset,
        who_can_post: typing.Union['AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdminconversationsGetConversationPrefsResponsePrefs':
        return super().__new__(
            cls,
            *args,
            can_thread=can_thread,
            who_can_post=who_can_post,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.adminconversations_get_conversation_prefs_response_prefs_can_thread import AdminconversationsGetConversationPrefsResponsePrefsCanThread
from slack_web_python_sdk.model.adminconversations_get_conversation_prefs_response_prefs_who_can_post import AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost
