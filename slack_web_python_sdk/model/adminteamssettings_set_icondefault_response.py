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


class AdminteamssettingsSetIcondefaultResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    This method either only returns a brief _not OK_ response or a verbose schema is not available for this method.
    """


    class MetaOapg:
        required = {
            "ok",
        }
        
        class properties:
        
            @staticmethod
            def ok() -> typing.Type['DefsOkFalse']:
                return DefsOkFalse
            __annotations__ = {
                "ok": ok,
            }
        additional_properties = schemas.AnyTypeSchema
    
    ok: 'DefsOkFalse'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkFalse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ok"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkFalse': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ok"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ok: 'DefsOkFalse',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'AdminteamssettingsSetIcondefaultResponse':
        return super().__new__(
            cls,
            *args,
            ok=ok,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.defs_ok_false import DefsOkFalse
