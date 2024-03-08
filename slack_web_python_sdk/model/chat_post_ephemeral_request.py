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


class ChatPostEphemeralRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "channel",
            "user",
        }
        
        class properties:
            channel = schemas.StrSchema
            user = schemas.StrSchema
            as_user = schemas.BoolSchema
            attachments = schemas.StrSchema
            blocks = schemas.StrSchema
            icon_emoji = schemas.StrSchema
            icon_url = schemas.StrSchema
            link_names = schemas.BoolSchema
            parse = schemas.StrSchema
            text = schemas.StrSchema
            thread_ts = schemas.StrSchema
            username = schemas.StrSchema
            __annotations__ = {
                "channel": channel,
                "user": user,
                "as_user": as_user,
                "attachments": attachments,
                "blocks": blocks,
                "icon_emoji": icon_emoji,
                "icon_url": icon_url,
                "link_names": link_names,
                "parse": parse,
                "text": text,
                "thread_ts": thread_ts,
                "username": username,
            }
    
    channel: MetaOapg.properties.channel
    user: MetaOapg.properties.user
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["as_user"]) -> MetaOapg.properties.as_user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blocks"]) -> MetaOapg.properties.blocks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon_emoji"]) -> MetaOapg.properties.icon_emoji: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon_url"]) -> MetaOapg.properties.icon_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_names"]) -> MetaOapg.properties.link_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parse"]) -> MetaOapg.properties.parse: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thread_ts"]) -> MetaOapg.properties.thread_ts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel", "user", "as_user", "attachments", "blocks", "icon_emoji", "icon_url", "link_names", "parse", "text", "thread_ts", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["as_user"]) -> typing.Union[MetaOapg.properties.as_user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blocks"]) -> typing.Union[MetaOapg.properties.blocks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon_emoji"]) -> typing.Union[MetaOapg.properties.icon_emoji, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon_url"]) -> typing.Union[MetaOapg.properties.icon_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_names"]) -> typing.Union[MetaOapg.properties.link_names, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parse"]) -> typing.Union[MetaOapg.properties.parse, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thread_ts"]) -> typing.Union[MetaOapg.properties.thread_ts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel", "user", "as_user", "attachments", "blocks", "icon_emoji", "icon_url", "link_names", "parse", "text", "thread_ts", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        channel: typing.Union[MetaOapg.properties.channel, str, ],
        user: typing.Union[MetaOapg.properties.user, str, ],
        as_user: typing.Union[MetaOapg.properties.as_user, bool, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, str, schemas.Unset] = schemas.unset,
        blocks: typing.Union[MetaOapg.properties.blocks, str, schemas.Unset] = schemas.unset,
        icon_emoji: typing.Union[MetaOapg.properties.icon_emoji, str, schemas.Unset] = schemas.unset,
        icon_url: typing.Union[MetaOapg.properties.icon_url, str, schemas.Unset] = schemas.unset,
        link_names: typing.Union[MetaOapg.properties.link_names, bool, schemas.Unset] = schemas.unset,
        parse: typing.Union[MetaOapg.properties.parse, str, schemas.Unset] = schemas.unset,
        text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
        thread_ts: typing.Union[MetaOapg.properties.thread_ts, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChatPostEphemeralRequest':
        return super().__new__(
            cls,
            *args,
            channel=channel,
            user=user,
            as_user=as_user,
            attachments=attachments,
            blocks=blocks,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            link_names=link_names,
            parse=parse,
            text=text,
            thread_ts=thread_ts,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
