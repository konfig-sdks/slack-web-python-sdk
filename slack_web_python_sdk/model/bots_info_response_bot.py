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


class BotsInfoResponseBot(
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
            def icons() -> typing.Type['BotsInfoResponseBotIcons']:
                return BotsInfoResponseBotIcons
        
            @staticmethod
            def id() -> typing.Type['DefsBotId']:
                return DefsBotId
            name = schemas.StrSchema
            updated = schemas.IntSchema
        
            @staticmethod
            def user_id() -> typing.Type['DefsUserId']:
                return DefsUserId
            __annotations__ = {
                "app_id": app_id,
                "deleted": deleted,
                "icons": icons,
                "id": id,
                "name": name,
                "updated": updated,
                "user_id": user_id,
            }
    
    deleted: MetaOapg.properties.deleted
    name: MetaOapg.properties.name
    id: 'DefsBotId'
    icons: 'BotsInfoResponseBotIcons'
    app_id: 'DefsAppId'
    updated: MetaOapg.properties.updated
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_id"]) -> 'DefsAppId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icons"]) -> 'BotsInfoResponseBotIcons': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'DefsBotId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> 'DefsUserId': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["app_id", "deleted", "icons", "id", "name", "updated", "user_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_id"]) -> 'DefsAppId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icons"]) -> 'BotsInfoResponseBotIcons': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'DefsBotId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union['DefsUserId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["app_id", "deleted", "icons", "id", "name", "updated", "user_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        deleted: typing.Union[MetaOapg.properties.deleted, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: 'DefsBotId',
        icons: 'BotsInfoResponseBotIcons',
        app_id: 'DefsAppId',
        updated: typing.Union[MetaOapg.properties.updated, decimal.Decimal, int, ],
        user_id: typing.Union['DefsUserId', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BotsInfoResponseBot':
        return super().__new__(
            cls,
            *args,
            deleted=deleted,
            name=name,
            id=id,
            icons=icons,
            app_id=app_id,
            updated=updated,
            user_id=user_id,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.bots_info_response_bot_icons import BotsInfoResponseBotIcons
from slack_web_python_sdk.model.defs_app_id import DefsAppId
from slack_web_python_sdk.model.defs_bot_id import DefsBotId
from slack_web_python_sdk.model.defs_user_id import DefsUserId
