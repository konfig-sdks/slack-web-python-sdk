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


class AdminconversationsInviteUserToChannelRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "user_ids",
            "channel_id",
        }
        
        class properties:
            channel_id = schemas.StrSchema
            user_ids = schemas.StrSchema
            __annotations__ = {
                "channel_id": channel_id,
                "user_ids": user_ids,
            }
    
    user_ids: MetaOapg.properties.user_ids
    channel_id: MetaOapg.properties.channel_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_id"]) -> MetaOapg.properties.channel_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_ids"]) -> MetaOapg.properties.user_ids: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel_id", "user_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_id"]) -> MetaOapg.properties.channel_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_ids"]) -> MetaOapg.properties.user_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel_id", "user_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        user_ids: typing.Union[MetaOapg.properties.user_ids, str, ],
        channel_id: typing.Union[MetaOapg.properties.channel_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdminconversationsInviteUserToChannelRequest':
        return super().__new__(
            cls,
            *args,
            user_ids=user_ids,
            channel_id=channel_id,
            _configuration=_configuration,
            **kwargs,
        )