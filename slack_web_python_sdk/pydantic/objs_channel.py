# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from slack_web_python_sdk.pydantic.defs_channel_id import DefsChannelId
from slack_web_python_sdk.pydantic.defs_team import DefsTeam
from slack_web_python_sdk.pydantic.defs_ts import DefsTs
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId
from slack_web_python_sdk.pydantic.objs_channel_purpose import ObjsChannelPurpose
from slack_web_python_sdk.pydantic.objs_channel_topic import ObjsChannelTopic
from slack_web_python_sdk.pydantic.objs_message import ObjsMessage

class ObjsChannel(BaseModel):
    created: int = Field(alias='created')

    creator: DefsUserId = Field(alias='creator')

    id: DefsChannelId = Field(alias='id')

    is_channel: bool = Field(alias='is_channel')

    is_mpim: bool = Field(alias='is_mpim')

    is_org_shared: bool = Field(alias='is_org_shared')

    is_private: bool = Field(alias='is_private')

    is_shared: bool = Field(alias='is_shared')

    members: typing.List[DefsUserId] = Field(alias='members')

    name: str = Field(alias='name')

    name_normalized: str = Field(alias='name_normalized')

    purpose: ObjsChannelPurpose = Field(alias='purpose')

    topic: ObjsChannelTopic = Field(alias='topic')

    accepted_user: typing.Optional[DefsUserId] = Field(None, alias='accepted_user')

    is_archived: typing.Optional[bool] = Field(None, alias='is_archived')

    is_frozen: typing.Optional[bool] = Field(None, alias='is_frozen')

    is_general: typing.Optional[bool] = Field(None, alias='is_general')

    is_member: typing.Optional[bool] = Field(None, alias='is_member')

    is_moved: typing.Optional[int] = Field(None, alias='is_moved')

    is_non_threadable: typing.Optional[bool] = Field(None, alias='is_non_threadable')

    is_pending_ext_shared: typing.Optional[bool] = Field(None, alias='is_pending_ext_shared')

    is_read_only: typing.Optional[bool] = Field(None, alias='is_read_only')

    is_thread_only: typing.Optional[bool] = Field(None, alias='is_thread_only')

    last_read: typing.Optional[DefsTs] = Field(None, alias='last_read')

    latest: typing.Optional[typing.List[typing.Union[typing.List[ObjsMessage], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]] = Field(None, alias='latest')

    num_members: typing.Optional[int] = Field(None, alias='num_members')

    pending_shared: typing.Optional[typing.List[DefsTeam]] = Field(None, alias='pending_shared')

    previous_names: typing.Optional[typing.List[str]] = Field(None, alias='previous_names')

    priority: typing.Optional[typing.Union[int, float]] = Field(None, alias='priority')

    unlinked: typing.Optional[int] = Field(None, alias='unlinked')

    unread_count: typing.Optional[int] = Field(None, alias='unread_count')

    unread_count_display: typing.Optional[int] = Field(None, alias='unread_count_display')
    class Config:
        arbitrary_types_allowed = True
