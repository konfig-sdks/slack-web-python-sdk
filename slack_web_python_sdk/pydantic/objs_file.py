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

from slack_web_python_sdk.pydantic.defs_channel import DefsChannel
from slack_web_python_sdk.pydantic.defs_channel_id import DefsChannelId
from slack_web_python_sdk.pydantic.defs_dm_id import DefsDmId
from slack_web_python_sdk.pydantic.defs_file_id import DefsFileId
from slack_web_python_sdk.pydantic.defs_group_id import DefsGroupId
from slack_web_python_sdk.pydantic.defs_team import DefsTeam
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId
from slack_web_python_sdk.pydantic.objs_file_shares import ObjsFileShares
from slack_web_python_sdk.pydantic.objs_reaction import ObjsReaction

class ObjsFile(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    channels: typing.Optional[typing.List[DefsChannelId]] = Field(None, alias='channels')

    comments_count: typing.Optional[int] = Field(None, alias='comments_count')

    created: typing.Optional[int] = Field(None, alias='created')

    date_delete: typing.Optional[int] = Field(None, alias='date_delete')

    display_as_bot: typing.Optional[bool] = Field(None, alias='display_as_bot')

    editable: typing.Optional[bool] = Field(None, alias='editable')

    editor: typing.Optional[DefsUserId] = Field(None, alias='editor')

    external_id: typing.Optional[str] = Field(None, alias='external_id')

    external_type: typing.Optional[str] = Field(None, alias='external_type')

    external_url: typing.Optional[str] = Field(None, alias='external_url')

    filetype: typing.Optional[str] = Field(None, alias='filetype')

    groups: typing.Optional[typing.List[DefsGroupId]] = Field(None, alias='groups')

    has_rich_preview: typing.Optional[bool] = Field(None, alias='has_rich_preview')

    id: typing.Optional[DefsFileId] = Field(None, alias='id')

    image_exif_rotation: typing.Optional[int] = Field(None, alias='image_exif_rotation')

    ims: typing.Optional[typing.List[DefsDmId]] = Field(None, alias='ims')

    is_external: typing.Optional[bool] = Field(None, alias='is_external')

    is_public: typing.Optional[bool] = Field(None, alias='is_public')

    is_starred: typing.Optional[bool] = Field(None, alias='is_starred')

    is_tombstoned: typing.Optional[bool] = Field(None, alias='is_tombstoned')

    last_editor: typing.Optional[DefsUserId] = Field(None, alias='last_editor')

    mimetype: typing.Optional[str] = Field(None, alias='mimetype')

    mode: typing.Optional[str] = Field(None, alias='mode')

    name: typing.Optional[str] = Field(None, alias='name')

    non_owner_editable: typing.Optional[bool] = Field(None, alias='non_owner_editable')

    num_stars: typing.Optional[int] = Field(None, alias='num_stars')

    original_h: typing.Optional[int] = Field(None, alias='original_h')

    original_w: typing.Optional[int] = Field(None, alias='original_w')

    permalink: typing.Optional[str] = Field(None, alias='permalink')

    permalink_public: typing.Optional[str] = Field(None, alias='permalink_public')

    pinned_info: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='pinned_info')

    pinned_to: typing.Optional[typing.List[DefsChannel]] = Field(None, alias='pinned_to')

    pretty_type: typing.Optional[str] = Field(None, alias='pretty_type')

    preview: typing.Optional[str] = Field(None, alias='preview')

    public_url_shared: typing.Optional[bool] = Field(None, alias='public_url_shared')

    reactions: typing.Optional[typing.List[ObjsReaction]] = Field(None, alias='reactions')

    shares: typing.Optional[ObjsFileShares] = Field(None, alias='shares')

    size: typing.Optional[int] = Field(None, alias='size')

    source_team: typing.Optional[DefsTeam] = Field(None, alias='source_team')

    state: typing.Optional[str] = Field(None, alias='state')

    thumb_1024: typing.Optional[str] = Field(None, alias='thumb_1024')

    thumb_1024_h: typing.Optional[int] = Field(None, alias='thumb_1024_h')

    thumb_1024_w: typing.Optional[int] = Field(None, alias='thumb_1024_w')

    thumb_160: typing.Optional[str] = Field(None, alias='thumb_160')

    thumb_360: typing.Optional[str] = Field(None, alias='thumb_360')

    thumb_360_h: typing.Optional[int] = Field(None, alias='thumb_360_h')

    thumb_360_w: typing.Optional[int] = Field(None, alias='thumb_360_w')

    thumb_480: typing.Optional[str] = Field(None, alias='thumb_480')

    thumb_480_h: typing.Optional[int] = Field(None, alias='thumb_480_h')

    thumb_480_w: typing.Optional[int] = Field(None, alias='thumb_480_w')

    thumb_64: typing.Optional[str] = Field(None, alias='thumb_64')

    thumb_720: typing.Optional[str] = Field(None, alias='thumb_720')

    thumb_720_h: typing.Optional[int] = Field(None, alias='thumb_720_h')

    thumb_720_w: typing.Optional[int] = Field(None, alias='thumb_720_w')

    thumb_80: typing.Optional[str] = Field(None, alias='thumb_80')

    thumb_800: typing.Optional[str] = Field(None, alias='thumb_800')

    thumb_800_h: typing.Optional[int] = Field(None, alias='thumb_800_h')

    thumb_800_w: typing.Optional[int] = Field(None, alias='thumb_800_w')

    thumb_960: typing.Optional[str] = Field(None, alias='thumb_960')

    thumb_960_h: typing.Optional[int] = Field(None, alias='thumb_960_h')

    thumb_960_w: typing.Optional[int] = Field(None, alias='thumb_960_w')

    thumb_tiny: typing.Optional[str] = Field(None, alias='thumb_tiny')

    timestamp: typing.Optional[int] = Field(None, alias='timestamp')

    updated: typing.Optional[int] = Field(None, alias='updated')

    url_private: typing.Optional[str] = Field(None, alias='url_private')

    url_private_download: typing.Optional[str] = Field(None, alias='url_private_download')

    user: typing.Optional[str] = Field(None, alias='user')

    user_team: typing.Optional[DefsTeam] = Field(None, alias='user_team')

    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
