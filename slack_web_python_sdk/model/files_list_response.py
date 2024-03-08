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


class FilesListResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Schema for successful response from files.list method
    """


    class MetaOapg:
        required = {
            "files",
            "paging",
            "ok",
        }
        
        class properties:
            
            
            class files(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    min_items = 0
                    
                    @staticmethod
                    def items() -> typing.Type['ObjsFile']:
                        return ObjsFile
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ObjsFile'], typing.List['ObjsFile']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'files':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObjsFile':
                    return super().__getitem__(i)
        
            @staticmethod
            def ok() -> typing.Type['DefsOkTrue']:
                return DefsOkTrue
        
            @staticmethod
            def paging() -> typing.Type['ObjsPaging']:
                return ObjsPaging
            __annotations__ = {
                "files": files,
                "ok": ok,
                "paging": paging,
            }
    
    files: MetaOapg.properties.files
    paging: 'ObjsPaging'
    ok: 'DefsOkTrue'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paging"]) -> 'ObjsPaging': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["files", "ok", "paging", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paging"]) -> 'ObjsPaging': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["files", "ok", "paging", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        files: typing.Union[MetaOapg.properties.files, list, tuple, ],
        paging: 'ObjsPaging',
        ok: 'DefsOkTrue',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FilesListResponse':
        return super().__new__(
            cls,
            *args,
            files=files,
            paging=paging,
            ok=ok,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.model.objs_file import ObjsFile
from slack_web_python_sdk.model.objs_paging import ObjsPaging