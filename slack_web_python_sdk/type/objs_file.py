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

from slack_web_python_sdk.type.defs_channel import DefsChannel
from slack_web_python_sdk.type.defs_channel_id import DefsChannelId
from slack_web_python_sdk.type.defs_dm_id import DefsDmId
from slack_web_python_sdk.type.defs_file_id import DefsFileId
from slack_web_python_sdk.type.defs_group_id import DefsGroupId
from slack_web_python_sdk.type.defs_team import DefsTeam
from slack_web_python_sdk.type.defs_user_id import DefsUserId
from slack_web_python_sdk.type.objs_file_shares import ObjsFileShares
from slack_web_python_sdk.type.objs_reaction import ObjsReaction

class RequiredObjsFile(TypedDict):
    pass

class OptionalObjsFile(TypedDict, total=False):
    title: str

    channels: typing.List[DefsChannelId]

    comments_count: int

    created: int

    date_delete: int

    display_as_bot: bool

    editable: bool

    editor: DefsUserId

    external_id: str

    external_type: str

    external_url: str

    filetype: str

    groups: typing.List[DefsGroupId]

    has_rich_preview: bool

    id: DefsFileId

    image_exif_rotation: int

    ims: typing.List[DefsDmId]

    is_external: bool

    is_public: bool

    is_starred: bool

    is_tombstoned: bool

    last_editor: DefsUserId

    mimetype: str

    mode: str

    name: str

    non_owner_editable: bool

    num_stars: int

    original_h: int

    original_w: int

    permalink: str

    permalink_public: str

    pinned_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    pinned_to: typing.List[DefsChannel]

    pretty_type: str

    preview: str

    public_url_shared: bool

    reactions: typing.List[ObjsReaction]

    shares: ObjsFileShares

    size: int

    source_team: DefsTeam

    state: str

    thumb_1024: str

    thumb_1024_h: int

    thumb_1024_w: int

    thumb_160: str

    thumb_360: str

    thumb_360_h: int

    thumb_360_w: int

    thumb_480: str

    thumb_480_h: int

    thumb_480_w: int

    thumb_64: str

    thumb_720: str

    thumb_720_h: int

    thumb_720_w: int

    thumb_80: str

    thumb_800: str

    thumb_800_h: int

    thumb_800_w: int

    thumb_960: str

    thumb_960_h: int

    thumb_960_w: int

    thumb_tiny: str

    timestamp: int

    updated: int

    url_private: str

    url_private_download: str

    user: str

    user_team: DefsTeam

    username: str

class ObjsFile(RequiredObjsFile, OptionalObjsFile):
    pass
