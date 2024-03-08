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


class ObjsEnterpriseUser(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "is_admin",
            "teams",
            "is_owner",
            "id",
            "enterprise_id",
            "enterprise_name",
        }
        
        class properties:
        
            @staticmethod
            def enterprise_id() -> typing.Type['DefsEnterpriseId']:
                return DefsEnterpriseId
            enterprise_name = schemas.StrSchema
        
            @staticmethod
            def id() -> typing.Type['DefsEnterpriseUserId']:
                return DefsEnterpriseUserId
            is_admin = schemas.BoolSchema
            is_owner = schemas.BoolSchema
            
            
            class teams(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DefsTeam']:
                        return DefsTeam
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DefsTeam'], typing.List['DefsTeam']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'teams':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DefsTeam':
                    return super().__getitem__(i)
            __annotations__ = {
                "enterprise_id": enterprise_id,
                "enterprise_name": enterprise_name,
                "id": id,
                "is_admin": is_admin,
                "is_owner": is_owner,
                "teams": teams,
            }
    
    is_admin: MetaOapg.properties.is_admin
    teams: MetaOapg.properties.teams
    is_owner: MetaOapg.properties.is_owner
    id: 'DefsEnterpriseUserId'
    enterprise_id: 'DefsEnterpriseId'
    enterprise_name: MetaOapg.properties.enterprise_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enterprise_id"]) -> 'DefsEnterpriseId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enterprise_name"]) -> MetaOapg.properties.enterprise_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'DefsEnterpriseUserId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_admin"]) -> MetaOapg.properties.is_admin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_owner"]) -> MetaOapg.properties.is_owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teams"]) -> MetaOapg.properties.teams: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enterprise_id", "enterprise_name", "id", "is_admin", "is_owner", "teams", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enterprise_id"]) -> 'DefsEnterpriseId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enterprise_name"]) -> MetaOapg.properties.enterprise_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'DefsEnterpriseUserId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_admin"]) -> MetaOapg.properties.is_admin: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_owner"]) -> MetaOapg.properties.is_owner: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teams"]) -> MetaOapg.properties.teams: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enterprise_id", "enterprise_name", "id", "is_admin", "is_owner", "teams", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_admin: typing.Union[MetaOapg.properties.is_admin, bool, ],
        teams: typing.Union[MetaOapg.properties.teams, list, tuple, ],
        is_owner: typing.Union[MetaOapg.properties.is_owner, bool, ],
        id: 'DefsEnterpriseUserId',
        enterprise_id: 'DefsEnterpriseId',
        enterprise_name: typing.Union[MetaOapg.properties.enterprise_name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjsEnterpriseUser':
        return super().__new__(
            cls,
            *args,
            is_admin=is_admin,
            teams=teams,
            is_owner=is_owner,
            id=id,
            enterprise_id=enterprise_id,
            enterprise_name=enterprise_name,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.defs_enterprise_id import DefsEnterpriseId
from slack_web_python_sdk.model.defs_enterprise_user_id import DefsEnterpriseUserId
from slack_web_python_sdk.model.defs_team import DefsTeam
