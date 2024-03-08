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

from slack_web_python_sdk.type.defs_channel_id import DefsChannelId
from slack_web_python_sdk.type.defs_team import DefsTeam
from slack_web_python_sdk.type.defs_ts import DefsTs
from slack_web_python_sdk.type.defs_user_id import DefsUserId
from slack_web_python_sdk.type.objs_channel_purpose import ObjsChannelPurpose
from slack_web_python_sdk.type.objs_channel_topic import ObjsChannelTopic
from slack_web_python_sdk.type.objs_message import ObjsMessage

class RequiredObjsChannel(TypedDict):
    created: int

    creator: DefsUserId

    id: DefsChannelId

    is_channel: bool

    is_mpim: bool

    is_org_shared: bool

    is_private: bool

    is_shared: bool

    members: typing.List[DefsUserId]

    name: str

    name_normalized: str

    purpose: ObjsChannelPurpose

    topic: ObjsChannelTopic

class OptionalObjsChannel(TypedDict, total=False):
    accepted_user: DefsUserId

    is_archived: bool

    is_frozen: bool

    is_general: bool

    is_member: bool

    is_moved: int

    is_non_threadable: bool

    is_pending_ext_shared: bool

    is_read_only: bool

    is_thread_only: bool

    last_read: DefsTs

    latest: typing.List[typing.Union[typing.List[ObjsMessage], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]

    num_members: int

    pending_shared: typing.List[DefsTeam]

    previous_names: typing.List[str]

    priority: typing.Union[int, float]

    unlinked: int

    unread_count: int

    unread_count_display: int

class ObjsChannel(RequiredObjsChannel, OptionalObjsChannel):
    pass
