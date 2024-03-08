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


class AdminconversationsrestrictAccessRemoveIdpGroupRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "group_id",
            "team_id",
            "channel_id",
            "token",
        }
        
        class properties:
            channel_id = schemas.StrSchema
            group_id = schemas.StrSchema
            team_id = schemas.StrSchema
            token = schemas.StrSchema
            __annotations__ = {
                "channel_id": channel_id,
                "group_id": group_id,
                "team_id": team_id,
                "token": token,
            }
    
    group_id: MetaOapg.properties.group_id
    team_id: MetaOapg.properties.team_id
    channel_id: MetaOapg.properties.channel_id
    token: MetaOapg.properties.token
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_id"]) -> MetaOapg.properties.channel_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_id"]) -> MetaOapg.properties.group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel_id", "group_id", "team_id", "token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_id"]) -> MetaOapg.properties.channel_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_id"]) -> MetaOapg.properties.group_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel_id", "group_id", "team_id", "token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        group_id: typing.Union[MetaOapg.properties.group_id, str, ],
        team_id: typing.Union[MetaOapg.properties.team_id, str, ],
        channel_id: typing.Union[MetaOapg.properties.channel_id, str, ],
        token: typing.Union[MetaOapg.properties.token, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdminconversationsrestrictAccessRemoveIdpGroupRequest':
        return super().__new__(
            cls,
            *args,
            group_id=group_id,
            team_id=team_id,
            channel_id=channel_id,
            token=token,
            _configuration=_configuration,
            **kwargs,
        )
