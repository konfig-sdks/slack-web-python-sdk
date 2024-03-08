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


class AppspermissionsresourcesGetResourcesListResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Schema for successful response apps.permissions.resources.list method
    """


    class MetaOapg:
        required = {
            "resources",
            "ok",
        }
        
        class properties:
        
            @staticmethod
            def ok() -> typing.Type['DefsOkTrue']:
                return DefsOkTrue
        
            @staticmethod
            def resources() -> typing.Type['AppspermissionsresourcesGetResourcesListResponseResources']:
                return AppspermissionsresourcesGetResourcesListResponseResources
        
            @staticmethod
            def response_metadata() -> typing.Type['AppspermissionsresourcesGetResourcesListResponseResponseMetadata']:
                return AppspermissionsresourcesGetResourcesListResponseResponseMetadata
            __annotations__ = {
                "ok": ok,
                "resources": resources,
                "response_metadata": response_metadata,
            }
        additional_properties = schemas.AnyTypeSchema
    
    resources: 'AppspermissionsresourcesGetResourcesListResponseResources'
    ok: 'DefsOkTrue'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> 'AppspermissionsresourcesGetResourcesListResponseResources': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response_metadata"]) -> 'AppspermissionsresourcesGetResourcesListResponseResponseMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resources"], typing_extensions.Literal["ok"], typing_extensions.Literal["response_metadata"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> 'AppspermissionsresourcesGetResourcesListResponseResources': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response_metadata"]) -> typing.Union['AppspermissionsresourcesGetResourcesListResponseResponseMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resources"], typing_extensions.Literal["ok"], typing_extensions.Literal["response_metadata"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        resources: 'AppspermissionsresourcesGetResourcesListResponseResources',
        ok: 'DefsOkTrue',
        response_metadata: typing.Union['AppspermissionsresourcesGetResourcesListResponseResponseMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'AppspermissionsresourcesGetResourcesListResponse':
        return super().__new__(
            cls,
            *args,
            resources=resources,
            ok=ok,
            response_metadata=response_metadata,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.appspermissionsresources_get_resources_list_response_resources import AppspermissionsresourcesGetResourcesListResponseResources
from slack_web_python_sdk.model.appspermissionsresources_get_resources_list_response_response_metadata import AppspermissionsresourcesGetResourcesListResponseResponseMetadata
from slack_web_python_sdk.model.defs_ok_true import DefsOkTrue
