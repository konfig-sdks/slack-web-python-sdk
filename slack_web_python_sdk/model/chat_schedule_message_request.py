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


class ChatScheduleMessageRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            as_user = schemas.BoolSchema
            attachments = schemas.StrSchema
            blocks = schemas.StrSchema
            channel = schemas.StrSchema
            link_names = schemas.BoolSchema
            parse = schemas.StrSchema
            post_at = schemas.StrSchema
            reply_broadcast = schemas.BoolSchema
            text = schemas.StrSchema
            thread_ts = schemas.NumberSchema
            unfurl_links = schemas.BoolSchema
            unfurl_media = schemas.BoolSchema
            __annotations__ = {
                "as_user": as_user,
                "attachments": attachments,
                "blocks": blocks,
                "channel": channel,
                "link_names": link_names,
                "parse": parse,
                "post_at": post_at,
                "reply_broadcast": reply_broadcast,
                "text": text,
                "thread_ts": thread_ts,
                "unfurl_links": unfurl_links,
                "unfurl_media": unfurl_media,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["as_user"]) -> MetaOapg.properties.as_user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blocks"]) -> MetaOapg.properties.blocks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_names"]) -> MetaOapg.properties.link_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parse"]) -> MetaOapg.properties.parse: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_at"]) -> MetaOapg.properties.post_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reply_broadcast"]) -> MetaOapg.properties.reply_broadcast: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thread_ts"]) -> MetaOapg.properties.thread_ts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unfurl_links"]) -> MetaOapg.properties.unfurl_links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unfurl_media"]) -> MetaOapg.properties.unfurl_media: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["as_user", "attachments", "blocks", "channel", "link_names", "parse", "post_at", "reply_broadcast", "text", "thread_ts", "unfurl_links", "unfurl_media", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["as_user"]) -> typing.Union[MetaOapg.properties.as_user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blocks"]) -> typing.Union[MetaOapg.properties.blocks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_names"]) -> typing.Union[MetaOapg.properties.link_names, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parse"]) -> typing.Union[MetaOapg.properties.parse, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_at"]) -> typing.Union[MetaOapg.properties.post_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reply_broadcast"]) -> typing.Union[MetaOapg.properties.reply_broadcast, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thread_ts"]) -> typing.Union[MetaOapg.properties.thread_ts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unfurl_links"]) -> typing.Union[MetaOapg.properties.unfurl_links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unfurl_media"]) -> typing.Union[MetaOapg.properties.unfurl_media, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["as_user", "attachments", "blocks", "channel", "link_names", "parse", "post_at", "reply_broadcast", "text", "thread_ts", "unfurl_links", "unfurl_media", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        as_user: typing.Union[MetaOapg.properties.as_user, bool, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, str, schemas.Unset] = schemas.unset,
        blocks: typing.Union[MetaOapg.properties.blocks, str, schemas.Unset] = schemas.unset,
        channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
        link_names: typing.Union[MetaOapg.properties.link_names, bool, schemas.Unset] = schemas.unset,
        parse: typing.Union[MetaOapg.properties.parse, str, schemas.Unset] = schemas.unset,
        post_at: typing.Union[MetaOapg.properties.post_at, str, schemas.Unset] = schemas.unset,
        reply_broadcast: typing.Union[MetaOapg.properties.reply_broadcast, bool, schemas.Unset] = schemas.unset,
        text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
        thread_ts: typing.Union[MetaOapg.properties.thread_ts, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        unfurl_links: typing.Union[MetaOapg.properties.unfurl_links, bool, schemas.Unset] = schemas.unset,
        unfurl_media: typing.Union[MetaOapg.properties.unfurl_media, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChatScheduleMessageRequest':
        return super().__new__(
            cls,
            *args,
            as_user=as_user,
            attachments=attachments,
            blocks=blocks,
            channel=channel,
            link_names=link_names,
            parse=parse,
            post_at=post_at,
            reply_broadcast=reply_broadcast,
            text=text,
            thread_ts=thread_ts,
            unfurl_links=unfurl_links,
            unfurl_media=unfurl_media,
            _configuration=_configuration,
            **kwargs,
        )