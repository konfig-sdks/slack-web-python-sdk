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


class ObjsResources(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "ids",
        }
        
        class properties:
        
            @staticmethod
            def ids() -> typing.Type['ObjsResourcesIds']:
                return ObjsResourcesIds
        
            @staticmethod
            def excluded_ids() -> typing.Type['ObjsResourcesExcludedIds']:
                return ObjsResourcesExcludedIds
            wildcard = schemas.BoolSchema
            __annotations__ = {
                "ids": ids,
                "excluded_ids": excluded_ids,
                "wildcard": wildcard,
            }
    
    ids: 'ObjsResourcesIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ids"]) -> 'ObjsResourcesIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excluded_ids"]) -> 'ObjsResourcesExcludedIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wildcard"]) -> MetaOapg.properties.wildcard: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ids", "excluded_ids", "wildcard", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ids"]) -> 'ObjsResourcesIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excluded_ids"]) -> typing.Union['ObjsResourcesExcludedIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wildcard"]) -> typing.Union[MetaOapg.properties.wildcard, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ids", "excluded_ids", "wildcard", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ids: 'ObjsResourcesIds',
        excluded_ids: typing.Union['ObjsResourcesExcludedIds', schemas.Unset] = schemas.unset,
        wildcard: typing.Union[MetaOapg.properties.wildcard, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjsResources':
        return super().__new__(
            cls,
            *args,
            ids=ids,
            excluded_ids=excluded_ids,
            wildcard=wildcard,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.objs_resources_excluded_ids import ObjsResourcesExcludedIds
from slack_web_python_sdk.model.objs_resources_ids import ObjsResourcesIds
