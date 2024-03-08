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

from slack_web_python_sdk.type.blocks import Blocks
from slack_web_python_sdk.type.defs_bot_id import DefsBotId
from slack_web_python_sdk.type.defs_channel import DefsChannel
from slack_web_python_sdk.type.defs_ts import DefsTs
from slack_web_python_sdk.type.defs_user_id import DefsUserId
from slack_web_python_sdk.type.defs_workspace_id import DefsWorkspaceId
from slack_web_python_sdk.type.objs_bot_profile import ObjsBotProfile
from slack_web_python_sdk.type.objs_comment import ObjsComment
from slack_web_python_sdk.type.objs_file import ObjsFile
from slack_web_python_sdk.type.objs_message_attachments import ObjsMessageAttachments
from slack_web_python_sdk.type.objs_message_icons import ObjsMessageIcons
from slack_web_python_sdk.type.objs_reaction import ObjsReaction
from slack_web_python_sdk.type.objs_user_profile_short import ObjsUserProfileShort

class RequiredObjsMessage(TypedDict):
    text: str

    ts: DefsTs

    type: str

class OptionalObjsMessage(TypedDict, total=False):
    attachments: ObjsMessageAttachments

    blocks: Blocks

    bot_id: typing.List[typing.Union[typing.List[DefsBotId], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]

    bot_profile: ObjsBotProfile

    client_msg_id: str

    comment: ObjsComment

    display_as_bot: bool

    file: ObjsFile

    files: typing.List[ObjsFile]

    icons: ObjsMessageIcons

    inviter: DefsUserId

    is_delayed_message: bool

    is_intro: bool

    is_starred: bool

    last_read: DefsTs

    latest_reply: DefsTs

    name: str

    old_name: str

    parent_user_id: DefsUserId

    permalink: str

    pinned_to: typing.List[DefsChannel]

    purpose: str

    reactions: typing.List[ObjsReaction]

    reply_count: int

    reply_users: typing.List[DefsUserId]

    reply_users_count: int

    source_team: DefsWorkspaceId

    subscribed: bool

    subtype: str

    team: DefsWorkspaceId

    thread_ts: DefsTs

    topic: str

    unread_count: int

    upload: bool

    user: DefsUserId

    user_profile: ObjsUserProfileShort

    user_team: DefsWorkspaceId

    username: str

class ObjsMessage(RequiredObjsMessage, OptionalObjsMessage):
    pass
