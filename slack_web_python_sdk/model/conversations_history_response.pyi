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


class ConversationsHistoryResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Schema for successful response from conversations.history method
    """


    class MetaOapg:
        required = {
            "channel_actions_count",
            "pin_count",
            "messages",
            "channel_actions_ts",
            "has_more",
            "ok",
        }
        
        class properties:
            channel_actions_count = schemas.IntSchema
            
            
            class channel_actions_ts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            any_of_0 = schemas.IntSchema
                            any_of_1 = schemas.AnyTypeSchema
                            
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
                ) -> 'channel_actions_ts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            has_more = schemas.BoolSchema
            
            
            class messages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ObjsMessage']:
                        return ObjsMessage
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ObjsMessage'], typing.List['ObjsMessage']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'messages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObjsMessage':
                    return super().__getitem__(i)
        
            @staticmethod
            def ok() -> typing.Type['DefsOkTrue']:
                return DefsOkTrue
            pin_count = schemas.IntSchema
            __annotations__ = {
                "channel_actions_count": channel_actions_count,
                "channel_actions_ts": channel_actions_ts,
                "has_more": has_more,
                "messages": messages,
                "ok": ok,
                "pin_count": pin_count,
            }
    
    channel_actions_count: MetaOapg.properties.channel_actions_count
    pin_count: MetaOapg.properties.pin_count
    messages: MetaOapg.properties.messages
    channel_actions_ts: MetaOapg.properties.channel_actions_ts
    has_more: MetaOapg.properties.has_more
    ok: 'DefsOkTrue'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_actions_count"]) -> MetaOapg.properties.channel_actions_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_actions_ts"]) -> MetaOapg.properties.channel_actions_ts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_more"]) -> MetaOapg.properties.has_more: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messages"]) -> MetaOapg.properties.messages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pin_count"]) -> MetaOapg.properties.pin_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel_actions_count", "channel_actions_ts", "has_more", "messages", "ok", "pin_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_actions_count"]) -> MetaOapg.properties.channel_actions_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_actions_ts"]) -> MetaOapg.properties.channel_actions_ts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_more"]) -> MetaOapg.properties.has_more: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messages"]) -> MetaOapg.properties.messages: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkTrue': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pin_count"]) -> MetaOapg.properties.pin_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel_actions_count", "channel_actions_ts", "has_more", "messages", "ok", "pin_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        channel_actions_count: typing.Union[MetaOapg.properties.channel_actions_count, decimal.Decimal, int, ],
        pin_count: typing.Union[MetaOapg.properties.pin_count, decimal.Decimal, int, ],
        messages: typing.Union[MetaOapg.properties.messages, list, tuple, ],
        channel_actions_ts: typing.Union[MetaOapg.properties.channel_actions_ts, list, tuple, ],
        has_more: typing.Union[MetaOapg.properties.has_more, bool, ],
        ok: 'DefsOkTrue',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConversationsHistoryResponse':
        return super().__new__(
            cls,
            *args,
            channel_actions_count=channel_actions_count,
            pin_count=pin_count,
            messages=messages,
            channel_actions_ts=channel_actions_ts,
            has_more=has_more,
            ok=ok,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.model.objs_message import ObjsMessage
