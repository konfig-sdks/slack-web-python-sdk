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


class ReactionsGetResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Schema for successful response from reactions.get method
    """


    class MetaOapg:
        
        
        class items(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class any_of_0(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "channel",
                            "message",
                            "ok",
                            "type",
                        }
                        
                        class properties:
                        
                            @staticmethod
                            def channel() -> typing.Type['DefsChannel']:
                                return DefsChannel
                        
                            @staticmethod
                            def message() -> typing.Type['ObjsMessage']:
                                return ObjsMessage
                        
                            @staticmethod
                            def ok() -> typing.Type['DefsOkTrue']:
                                return DefsOkTrue
                            
                            
                            class type(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                                
                                @schemas.classproperty
                                def MESSAGE(cls):
                                    return cls("message")
                            __annotations__ = {
                                "channel": channel,
                                "message": message,
                                "ok": ok,
                                "type": type,
                            }
                        additional_properties = schemas.NotAnyTypeSchema
                    
                    channel: 'DefsChannel'
                    message: 'ObjsMessage'
                    ok: 'DefsOkTrue'
                    type: MetaOapg.properties.type
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> 'DefsChannel': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["message"]) -> 'ObjsMessage': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel"], typing_extensions.Literal["message"], typing_extensions.Literal["ok"], typing_extensions.Literal["type"], ]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> 'DefsChannel': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> 'ObjsMessage': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel"], typing_extensions.Literal["message"], typing_extensions.Literal["ok"], typing_extensions.Literal["type"], ]):
                        return super().get_item_oapg(name)
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        channel: 'DefsChannel',
                        message: 'ObjsMessage',
                        ok: 'DefsOkTrue',
                        type: typing.Union[MetaOapg.properties.type, str, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs,
                    ) -> 'any_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            channel=channel,
                            message=message,
                            ok=ok,
                            type=type,
                            _configuration=_configuration,
                        )
                
                
                class any_of_1(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "file",
                            "ok",
                            "type",
                        }
                        
                        class properties:
                        
                            @staticmethod
                            def file() -> typing.Type['ObjsFile']:
                                return ObjsFile
                        
                            @staticmethod
                            def ok() -> typing.Type['DefsOkTrue']:
                                return DefsOkTrue
                            
                            
                            class type(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                                
                                @schemas.classproperty
                                def FILE(cls):
                                    return cls("file")
                            __annotations__ = {
                                "file": file,
                                "ok": ok,
                                "type": type,
                            }
                        additional_properties = schemas.NotAnyTypeSchema
                    
                    file: 'ObjsFile'
                    ok: 'DefsOkTrue'
                    type: MetaOapg.properties.type
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["file"]) -> 'ObjsFile': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["file"], typing_extensions.Literal["ok"], typing_extensions.Literal["type"], ]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> 'ObjsFile': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["file"], typing_extensions.Literal["ok"], typing_extensions.Literal["type"], ]):
                        return super().get_item_oapg(name)
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        file: 'ObjsFile',
                        ok: 'DefsOkTrue',
                        type: typing.Union[MetaOapg.properties.type, str, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs,
                    ) -> 'any_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            file=file,
                            ok=ok,
                            type=type,
                            _configuration=_configuration,
                        )
                
                
                class any_of_2(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "file",
                            "comment",
                            "ok",
                            "type",
                        }
                        
                        class properties:
                        
                            @staticmethod
                            def comment() -> typing.Type['ObjsComment']:
                                return ObjsComment
                        
                            @staticmethod
                            def file() -> typing.Type['ObjsFile']:
                                return ObjsFile
                        
                            @staticmethod
                            def ok() -> typing.Type['DefsOkTrue']:
                                return DefsOkTrue
                            
                            
                            class type(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                                
                                @schemas.classproperty
                                def FILE_COMMENT(cls):
                                    return cls("file_comment")
                            __annotations__ = {
                                "comment": comment,
                                "file": file,
                                "ok": ok,
                                "type": type,
                            }
                        additional_properties = schemas.NotAnyTypeSchema
                    
                    file: 'ObjsFile'
                    comment: 'ObjsComment'
                    ok: 'DefsOkTrue'
                    type: MetaOapg.properties.type
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["file"]) -> 'ObjsFile': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> 'ObjsComment': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["file"], typing_extensions.Literal["comment"], typing_extensions.Literal["ok"], typing_extensions.Literal["type"], ]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> 'ObjsFile': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> 'ObjsComment': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["file"], typing_extensions.Literal["comment"], typing_extensions.Literal["ok"], typing_extensions.Literal["type"], ]):
                        return super().get_item_oapg(name)
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        file: 'ObjsFile',
                        comment: 'ObjsComment',
                        ok: 'DefsOkTrue',
                        type: typing.Union[MetaOapg.properties.type, str, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs,
                    ) -> 'any_of_2':
                        return super().__new__(
                            cls,
                            *args,
                            file=file,
                            comment=comment,
                            ok=ok,
                            type=type,
                            _configuration=_configuration,
                        )
                
                @classmethod
                @functools.lru_cache()
                def any_of(cls):
                    # we need this here to make our import statements work
                    # we must store _composed_schemas in here so the code is only run
                    # when we invoke this method. If we kept this at the class
                    # level we would get an error because the class level
                    # code would be run when this module is imported, and these composed
                    # classes don't exist yet because their module has not finished
                    # loading
                    return [
                        cls.any_of_0,
                        cls.any_of_1,
                        cls.any_of_2,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ReactionsGetResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)

from slack_web_python_sdk.model.defs_channel import DefsChannel
from slack_web_python_sdk.model.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.model.objs_comment import ObjsComment
from slack_web_python_sdk.model.objs_file import ObjsFile
from slack_web_python_sdk.model.objs_message import ObjsMessage
