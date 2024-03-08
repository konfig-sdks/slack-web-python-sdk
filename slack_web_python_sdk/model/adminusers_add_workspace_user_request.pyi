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


class AdminusersAddWorkspaceUserRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "user_id",
            "team_id",
        }
        
        class properties:
            team_id = schemas.StrSchema
            user_id = schemas.StrSchema
            channel_ids = schemas.StrSchema
            is_restricted = schemas.BoolSchema
            is_ultra_restricted = schemas.BoolSchema
            __annotations__ = {
                "team_id": team_id,
                "user_id": user_id,
                "channel_ids": channel_ids,
                "is_restricted": is_restricted,
                "is_ultra_restricted": is_ultra_restricted,
            }
    
    user_id: MetaOapg.properties.user_id
    team_id: MetaOapg.properties.team_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_ids"]) -> MetaOapg.properties.channel_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_restricted"]) -> MetaOapg.properties.is_restricted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_ultra_restricted"]) -> MetaOapg.properties.is_ultra_restricted: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["team_id", "user_id", "channel_ids", "is_restricted", "is_ultra_restricted", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_ids"]) -> typing.Union[MetaOapg.properties.channel_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_restricted"]) -> typing.Union[MetaOapg.properties.is_restricted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_ultra_restricted"]) -> typing.Union[MetaOapg.properties.is_ultra_restricted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["team_id", "user_id", "channel_ids", "is_restricted", "is_ultra_restricted", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, ],
        team_id: typing.Union[MetaOapg.properties.team_id, str, ],
        channel_ids: typing.Union[MetaOapg.properties.channel_ids, str, schemas.Unset] = schemas.unset,
        is_restricted: typing.Union[MetaOapg.properties.is_restricted, bool, schemas.Unset] = schemas.unset,
        is_ultra_restricted: typing.Union[MetaOapg.properties.is_ultra_restricted, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdminusersAddWorkspaceUserRequest':
        return super().__new__(
            cls,
            *args,
            user_id=user_id,
            team_id=team_id,
            channel_ids=channel_ids,
            is_restricted=is_restricted,
            is_ultra_restricted=is_ultra_restricted,
            _configuration=_configuration,
            **kwargs,
        )