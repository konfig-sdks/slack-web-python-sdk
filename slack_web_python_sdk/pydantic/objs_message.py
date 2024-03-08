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

from slack_web_python_sdk.pydantic.blocks import Blocks
from slack_web_python_sdk.pydantic.defs_bot_id import DefsBotId
from slack_web_python_sdk.pydantic.defs_channel import DefsChannel
from slack_web_python_sdk.pydantic.defs_ts import DefsTs
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId
from slack_web_python_sdk.pydantic.defs_workspace_id import DefsWorkspaceId
from slack_web_python_sdk.pydantic.objs_bot_profile import ObjsBotProfile
from slack_web_python_sdk.pydantic.objs_comment import ObjsComment
from slack_web_python_sdk.pydantic.objs_file import ObjsFile
from slack_web_python_sdk.pydantic.objs_message_attachments import ObjsMessageAttachments
from slack_web_python_sdk.pydantic.objs_message_icons import ObjsMessageIcons
from slack_web_python_sdk.pydantic.objs_reaction import ObjsReaction
from slack_web_python_sdk.pydantic.objs_user_profile_short import ObjsUserProfileShort

class ObjsMessage(BaseModel):
    text: str = Field(alias='text')

    ts: DefsTs = Field(alias='ts')

    type: str = Field(alias='type')

    attachments: typing.Optional[ObjsMessageAttachments] = Field(None, alias='attachments')

    blocks: typing.Optional[Blocks] = Field(None, alias='blocks')

    bot_id: typing.Optional[typing.List[typing.Union[typing.List[DefsBotId], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]] = Field(None, alias='bot_id')

    bot_profile: typing.Optional[ObjsBotProfile] = Field(None, alias='bot_profile')

    client_msg_id: typing.Optional[str] = Field(None, alias='client_msg_id')

    comment: typing.Optional[ObjsComment] = Field(None, alias='comment')

    display_as_bot: typing.Optional[bool] = Field(None, alias='display_as_bot')

    file: typing.Optional[ObjsFile] = Field(None, alias='file')

    files: typing.Optional[typing.List[ObjsFile]] = Field(None, alias='files')

    icons: typing.Optional[ObjsMessageIcons] = Field(None, alias='icons')

    inviter: typing.Optional[DefsUserId] = Field(None, alias='inviter')

    is_delayed_message: typing.Optional[bool] = Field(None, alias='is_delayed_message')

    is_intro: typing.Optional[bool] = Field(None, alias='is_intro')

    is_starred: typing.Optional[bool] = Field(None, alias='is_starred')

    last_read: typing.Optional[DefsTs] = Field(None, alias='last_read')

    latest_reply: typing.Optional[DefsTs] = Field(None, alias='latest_reply')

    name: typing.Optional[str] = Field(None, alias='name')

    old_name: typing.Optional[str] = Field(None, alias='old_name')

    parent_user_id: typing.Optional[DefsUserId] = Field(None, alias='parent_user_id')

    permalink: typing.Optional[str] = Field(None, alias='permalink')

    pinned_to: typing.Optional[typing.List[DefsChannel]] = Field(None, alias='pinned_to')

    purpose: typing.Optional[str] = Field(None, alias='purpose')

    reactions: typing.Optional[typing.List[ObjsReaction]] = Field(None, alias='reactions')

    reply_count: typing.Optional[int] = Field(None, alias='reply_count')

    reply_users: typing.Optional[typing.List[DefsUserId]] = Field(None, alias='reply_users')

    reply_users_count: typing.Optional[int] = Field(None, alias='reply_users_count')

    source_team: typing.Optional[DefsWorkspaceId] = Field(None, alias='source_team')

    subscribed: typing.Optional[bool] = Field(None, alias='subscribed')

    subtype: typing.Optional[str] = Field(None, alias='subtype')

    team: typing.Optional[DefsWorkspaceId] = Field(None, alias='team')

    thread_ts: typing.Optional[DefsTs] = Field(None, alias='thread_ts')

    topic: typing.Optional[str] = Field(None, alias='topic')

    unread_count: typing.Optional[int] = Field(None, alias='unread_count')

    upload: typing.Optional[bool] = Field(None, alias='upload')

    user: typing.Optional[DefsUserId] = Field(None, alias='user')

    user_profile: typing.Optional[ObjsUserProfileShort] = Field(None, alias='user_profile')

    user_team: typing.Optional[DefsWorkspaceId] = Field(None, alias='user_team')

    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
