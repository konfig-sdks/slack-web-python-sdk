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


class ObjsBotProfile(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "deleted",
            "name",
            "id",
            "team_id",
            "icons",
            "app_id",
            "updated",
        }
        
        class properties:
        
            @staticmethod
            def app_id() -> typing.Type['DefsAppId']:
                return DefsAppId
            deleted = schemas.BoolSchema
        
            @staticmethod
            def icons() -> typing.Type['ObjsBotProfileIcons']:
                return ObjsBotProfileIcons
        
            @staticmethod
            def id() -> typing.Type['DefsBotId']:
                return DefsBotId
            name = schemas.StrSchema
        
            @staticmethod
            def team_id() -> typing.Type['DefsTeam']:
                return DefsTeam
            updated = schemas.IntSchema
            __annotations__ = {
                "app_id": app_id,
                "deleted": deleted,
                "icons": icons,
                "id": id,
                "name": name,
                "team_id": team_id,
                "updated": updated,
            }
    
    deleted: MetaOapg.properties.deleted
    name: MetaOapg.properties.name
    id: 'DefsBotId'
    team_id: 'DefsTeam'
    icons: 'ObjsBotProfileIcons'
    app_id: 'DefsAppId'
    updated: MetaOapg.properties.updated
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_id"]) -> 'DefsAppId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icons"]) -> 'ObjsBotProfileIcons': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'DefsBotId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_id"]) -> 'DefsTeam': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["app_id", "deleted", "icons", "id", "name", "team_id", "updated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_id"]) -> 'DefsAppId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icons"]) -> 'ObjsBotProfileIcons': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'DefsBotId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_id"]) -> 'DefsTeam': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["app_id", "deleted", "icons", "id", "name", "team_id", "updated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        deleted: typing.Union[MetaOapg.properties.deleted, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: 'DefsBotId',
        team_id: 'DefsTeam',
        icons: 'ObjsBotProfileIcons',
        app_id: 'DefsAppId',
        updated: typing.Union[MetaOapg.properties.updated, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjsBotProfile':
        return super().__new__(
            cls,
            *args,
            deleted=deleted,
            name=name,
            id=id,
            team_id=team_id,
            icons=icons,
            app_id=app_id,
            updated=updated,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.defs_app_id import DefsAppId
from slack_web_python_sdk.model.defs_bot_id import DefsBotId
from slack_web_python_sdk.model.defs_team import DefsTeam
from slack_web_python_sdk.model.objs_bot_profile_icons import ObjsBotProfileIcons
