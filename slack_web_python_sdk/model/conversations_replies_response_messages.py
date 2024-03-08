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


class ConversationsRepliesResponseMessages(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.ListSchema
        ):
        
        
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
                                    "subscribed",
                                    "thread_ts",
                                    "text",
                                    "reply_count",
                                    "type",
                                    "user",
                                    "ts",
                                }
                                
                                class properties:
                                
                                    @staticmethod
                                    def last_read() -> typing.Type['DefsTs']:
                                        return DefsTs
                                
                                    @staticmethod
                                    def latest_reply() -> typing.Type['DefsTs']:
                                        return DefsTs
                                    reply_count = schemas.IntSchema
                                    
                                    
                                    class reply_users(
                                        schemas.ListSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            unique_items = True
                                            
                                            @staticmethod
                                            def items() -> typing.Type['DefsUserId']:
                                                return DefsUserId
                                    
                                        def __new__(
                                            cls,
                                            arg: typing.Union[typing.Tuple['DefsUserId'], typing.List['DefsUserId']],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                        ) -> 'reply_users':
                                            return super().__new__(
                                                cls,
                                                arg,
                                                _configuration=_configuration,
                                            )
                                    
                                        def __getitem__(self, i: int) -> 'DefsUserId':
                                            return super().__getitem__(i)
                                    reply_users_count = schemas.IntSchema
                                
                                    @staticmethod
                                    def source_team() -> typing.Type['DefsTeam']:
                                        return DefsTeam
                                    subscribed = schemas.BoolSchema
                                
                                    @staticmethod
                                    def team() -> typing.Type['DefsTeam']:
                                        return DefsTeam
                                    text = schemas.StrSchema
                                
                                    @staticmethod
                                    def thread_ts() -> typing.Type['DefsTs']:
                                        return DefsTs
                                
                                    @staticmethod
                                    def ts() -> typing.Type['DefsTs']:
                                        return DefsTs
                                    type = schemas.StrSchema
                                    unread_count = schemas.IntSchema
                                
                                    @staticmethod
                                    def user() -> typing.Type['DefsUserId']:
                                        return DefsUserId
                                
                                    @staticmethod
                                    def user_profile() -> typing.Type['ObjsUserProfileShort']:
                                        return ObjsUserProfileShort
                                
                                    @staticmethod
                                    def user_team() -> typing.Type['DefsTeam']:
                                        return DefsTeam
                                    __annotations__ = {
                                        "last_read": last_read,
                                        "latest_reply": latest_reply,
                                        "reply_count": reply_count,
                                        "reply_users": reply_users,
                                        "reply_users_count": reply_users_count,
                                        "source_team": source_team,
                                        "subscribed": subscribed,
                                        "team": team,
                                        "text": text,
                                        "thread_ts": thread_ts,
                                        "ts": ts,
                                        "type": type,
                                        "unread_count": unread_count,
                                        "user": user,
                                        "user_profile": user_profile,
                                        "user_team": user_team,
                                    }
                            
                            subscribed: MetaOapg.properties.subscribed
                            thread_ts: 'DefsTs'
                            text: MetaOapg.properties.text
                            reply_count: MetaOapg.properties.reply_count
                            type: MetaOapg.properties.type
                            user: 'DefsUserId'
                            ts: 'DefsTs'
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["last_read"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["latest_reply"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["reply_count"]) -> MetaOapg.properties.reply_count: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["reply_users"]) -> MetaOapg.properties.reply_users: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["reply_users_count"]) -> MetaOapg.properties.reply_users_count: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["source_team"]) -> 'DefsTeam': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["subscribed"]) -> MetaOapg.properties.subscribed: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["team"]) -> 'DefsTeam': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["thread_ts"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["ts"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["unread_count"]) -> MetaOapg.properties.unread_count: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'DefsUserId': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["user_profile"]) -> 'ObjsUserProfileShort': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["user_team"]) -> 'DefsTeam': ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["last_read", "latest_reply", "reply_count", "reply_users", "reply_users_count", "source_team", "subscribed", "team", "text", "thread_ts", "ts", "type", "unread_count", "user", "user_profile", "user_team", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["last_read"]) -> typing.Union['DefsTs', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["latest_reply"]) -> typing.Union['DefsTs', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["reply_count"]) -> MetaOapg.properties.reply_count: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["reply_users"]) -> typing.Union[MetaOapg.properties.reply_users, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["reply_users_count"]) -> typing.Union[MetaOapg.properties.reply_users_count, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["source_team"]) -> typing.Union['DefsTeam', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["subscribed"]) -> MetaOapg.properties.subscribed: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union['DefsTeam', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["thread_ts"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["ts"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["unread_count"]) -> typing.Union[MetaOapg.properties.unread_count, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'DefsUserId': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["user_profile"]) -> typing.Union['ObjsUserProfileShort', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["user_team"]) -> typing.Union['DefsTeam', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["last_read", "latest_reply", "reply_count", "reply_users", "reply_users_count", "source_team", "subscribed", "team", "text", "thread_ts", "ts", "type", "unread_count", "user", "user_profile", "user_team", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                subscribed: typing.Union[MetaOapg.properties.subscribed, bool, ],
                                thread_ts: 'DefsTs',
                                text: typing.Union[MetaOapg.properties.text, str, ],
                                reply_count: typing.Union[MetaOapg.properties.reply_count, decimal.Decimal, int, ],
                                type: typing.Union[MetaOapg.properties.type, str, ],
                                user: 'DefsUserId',
                                ts: 'DefsTs',
                                last_read: typing.Union['DefsTs', schemas.Unset] = schemas.unset,
                                latest_reply: typing.Union['DefsTs', schemas.Unset] = schemas.unset,
                                reply_users: typing.Union[MetaOapg.properties.reply_users, list, tuple, schemas.Unset] = schemas.unset,
                                reply_users_count: typing.Union[MetaOapg.properties.reply_users_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                source_team: typing.Union['DefsTeam', schemas.Unset] = schemas.unset,
                                team: typing.Union['DefsTeam', schemas.Unset] = schemas.unset,
                                unread_count: typing.Union[MetaOapg.properties.unread_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                user_profile: typing.Union['ObjsUserProfileShort', schemas.Unset] = schemas.unset,
                                user_team: typing.Union['DefsTeam', schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'any_of_0':
                                return super().__new__(
                                    cls,
                                    *args,
                                    subscribed=subscribed,
                                    thread_ts=thread_ts,
                                    text=text,
                                    reply_count=reply_count,
                                    type=type,
                                    user=user,
                                    ts=ts,
                                    last_read=last_read,
                                    latest_reply=latest_reply,
                                    reply_users=reply_users,
                                    reply_users_count=reply_users_count,
                                    source_team=source_team,
                                    team=team,
                                    unread_count=unread_count,
                                    user_profile=user_profile,
                                    user_team=user_team,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class any_of_1(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "parent_user_id",
                                    "thread_ts",
                                    "text",
                                    "type",
                                    "user",
                                    "ts",
                                }
                                
                                class properties:
                                    is_starred = schemas.BoolSchema
                                
                                    @staticmethod
                                    def parent_user_id() -> typing.Type['DefsUserId']:
                                        return DefsUserId
                                
                                    @staticmethod
                                    def source_team() -> typing.Type['DefsTeam']:
                                        return DefsTeam
                                
                                    @staticmethod
                                    def team() -> typing.Type['DefsTeam']:
                                        return DefsTeam
                                    text = schemas.StrSchema
                                
                                    @staticmethod
                                    def thread_ts() -> typing.Type['DefsTs']:
                                        return DefsTs
                                
                                    @staticmethod
                                    def ts() -> typing.Type['DefsTs']:
                                        return DefsTs
                                    type = schemas.StrSchema
                                
                                    @staticmethod
                                    def user() -> typing.Type['DefsUserId']:
                                        return DefsUserId
                                
                                    @staticmethod
                                    def user_profile() -> typing.Type['ObjsUserProfileShort']:
                                        return ObjsUserProfileShort
                                
                                    @staticmethod
                                    def user_team() -> typing.Type['DefsTeam']:
                                        return DefsTeam
                                    __annotations__ = {
                                        "is_starred": is_starred,
                                        "parent_user_id": parent_user_id,
                                        "source_team": source_team,
                                        "team": team,
                                        "text": text,
                                        "thread_ts": thread_ts,
                                        "ts": ts,
                                        "type": type,
                                        "user": user,
                                        "user_profile": user_profile,
                                        "user_team": user_team,
                                    }
                            
                            parent_user_id: 'DefsUserId'
                            thread_ts: 'DefsTs'
                            text: MetaOapg.properties.text
                            type: MetaOapg.properties.type
                            user: 'DefsUserId'
                            ts: 'DefsTs'
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["is_starred"]) -> MetaOapg.properties.is_starred: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["parent_user_id"]) -> 'DefsUserId': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["source_team"]) -> 'DefsTeam': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["team"]) -> 'DefsTeam': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["thread_ts"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["ts"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'DefsUserId': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["user_profile"]) -> 'ObjsUserProfileShort': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["user_team"]) -> 'DefsTeam': ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_starred", "parent_user_id", "source_team", "team", "text", "thread_ts", "ts", "type", "user", "user_profile", "user_team", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["is_starred"]) -> typing.Union[MetaOapg.properties.is_starred, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["parent_user_id"]) -> 'DefsUserId': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["source_team"]) -> typing.Union['DefsTeam', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union['DefsTeam', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["thread_ts"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["ts"]) -> 'DefsTs': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'DefsUserId': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["user_profile"]) -> typing.Union['ObjsUserProfileShort', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["user_team"]) -> typing.Union['DefsTeam', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_starred", "parent_user_id", "source_team", "team", "text", "thread_ts", "ts", "type", "user", "user_profile", "user_team", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                parent_user_id: 'DefsUserId',
                                thread_ts: 'DefsTs',
                                text: typing.Union[MetaOapg.properties.text, str, ],
                                type: typing.Union[MetaOapg.properties.type, str, ],
                                user: 'DefsUserId',
                                ts: 'DefsTs',
                                is_starred: typing.Union[MetaOapg.properties.is_starred, bool, schemas.Unset] = schemas.unset,
                                source_team: typing.Union['DefsTeam', schemas.Unset] = schemas.unset,
                                team: typing.Union['DefsTeam', schemas.Unset] = schemas.unset,
                                user_profile: typing.Union['ObjsUserProfileShort', schemas.Unset] = schemas.unset,
                                user_team: typing.Union['DefsTeam', schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'any_of_1':
                                return super().__new__(
                                    cls,
                                    *args,
                                    parent_user_id=parent_user_id,
                                    thread_ts=thread_ts,
                                    text=text,
                                    type=type,
                                    user=user,
                                    ts=ts,
                                    is_starred=is_starred,
                                    source_team=source_team,
                                    team=team,
                                    user_profile=user_profile,
                                    user_team=user_team,
                                    _configuration=_configuration,
                                    **kwargs,
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
            ) -> 'items':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> MetaOapg.items:
                return super().__getitem__(i)

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ConversationsRepliesResponseMessages':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)

from slack_web_python_sdk.model.defs_team import DefsTeam
from slack_web_python_sdk.model.defs_ts import DefsTs
from slack_web_python_sdk.model.defs_user_id import DefsUserId
from slack_web_python_sdk.model.objs_user_profile_short import ObjsUserProfileShort
