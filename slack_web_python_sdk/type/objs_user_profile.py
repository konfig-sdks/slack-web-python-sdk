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

from slack_web_python_sdk.type.defs_bot_id import DefsBotId
from slack_web_python_sdk.type.defs_optional_app_id import DefsOptionalAppId
from slack_web_python_sdk.type.defs_workspace_id import DefsWorkspaceId

class RequiredObjsUserProfile(TypedDict):
    title: str

    avatar_hash: str

    display_name: str

    display_name_normalized: str

    fields: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]

    phone: str

    real_name: str

    real_name_normalized: str

    skype: str

    status_emoji: str

    status_text: str

class OptionalObjsUserProfile(TypedDict, total=False):
    always_active: bool

    api_app_id: DefsOptionalAppId

    bot_id: DefsBotId

    email: typing.Optional[str]

    first_name: typing.Optional[str]

    guest_expiration_ts: typing.Optional[int]

    guest_invited_by: typing.Optional[str]

    image_1024: typing.Optional[str]

    image_192: typing.Optional[str]

    image_24: typing.Optional[str]

    image_32: typing.Optional[str]

    image_48: typing.Optional[str]

    image_512: typing.Optional[str]

    image_72: typing.Optional[str]

    image_original: typing.Optional[str]

    is_app_user: bool

    is_custom_image: bool

    is_restricted: typing.Optional[bool]

    is_ultra_restricted: typing.Optional[bool]

    last_avatar_image_hash: str

    last_name: typing.Optional[str]

    memberships_count: int

    name: typing.Optional[str]

    pronouns: str

    status_default_emoji: str

    status_default_text: str

    status_default_text_canonical: typing.Optional[str]

    status_expiration: int

    status_text_canonical: typing.Optional[str]

    team: DefsWorkspaceId

    updated: int

    user_id: str

    username: typing.Optional[str]

class ObjsUserProfile(RequiredObjsUserProfile, OptionalObjsUserProfile):
    pass
