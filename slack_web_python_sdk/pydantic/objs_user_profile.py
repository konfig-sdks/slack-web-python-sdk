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

from slack_web_python_sdk.pydantic.defs_bot_id import DefsBotId
from slack_web_python_sdk.pydantic.defs_optional_app_id import DefsOptionalAppId
from slack_web_python_sdk.pydantic.defs_workspace_id import DefsWorkspaceId

class ObjsUserProfile(BaseModel):
    title: str = Field(alias='title')

    avatar_hash: str = Field(alias='avatar_hash')

    display_name: str = Field(alias='display_name')

    display_name_normalized: str = Field(alias='display_name_normalized')

    fields: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(alias='fields')

    phone: str = Field(alias='phone')

    real_name: str = Field(alias='real_name')

    real_name_normalized: str = Field(alias='real_name_normalized')

    skype: str = Field(alias='skype')

    status_emoji: str = Field(alias='status_emoji')

    status_text: str = Field(alias='status_text')

    always_active: typing.Optional[bool] = Field(None, alias='always_active')

    api_app_id: typing.Optional[DefsOptionalAppId] = Field(None, alias='api_app_id')

    bot_id: typing.Optional[DefsBotId] = Field(None, alias='bot_id')

    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='first_name')

    guest_expiration_ts: typing.Optional[typing.Optional[int]] = Field(None, alias='guest_expiration_ts')

    guest_invited_by: typing.Optional[typing.Optional[str]] = Field(None, alias='guest_invited_by')

    image_1024: typing.Optional[typing.Optional[str]] = Field(None, alias='image_1024')

    image_192: typing.Optional[typing.Optional[str]] = Field(None, alias='image_192')

    image_24: typing.Optional[typing.Optional[str]] = Field(None, alias='image_24')

    image_32: typing.Optional[typing.Optional[str]] = Field(None, alias='image_32')

    image_48: typing.Optional[typing.Optional[str]] = Field(None, alias='image_48')

    image_512: typing.Optional[typing.Optional[str]] = Field(None, alias='image_512')

    image_72: typing.Optional[typing.Optional[str]] = Field(None, alias='image_72')

    image_original: typing.Optional[typing.Optional[str]] = Field(None, alias='image_original')

    is_app_user: typing.Optional[bool] = Field(None, alias='is_app_user')

    is_custom_image: typing.Optional[bool] = Field(None, alias='is_custom_image')

    is_restricted: typing.Optional[typing.Optional[bool]] = Field(None, alias='is_restricted')

    is_ultra_restricted: typing.Optional[typing.Optional[bool]] = Field(None, alias='is_ultra_restricted')

    last_avatar_image_hash: typing.Optional[str] = Field(None, alias='last_avatar_image_hash')

    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='last_name')

    memberships_count: typing.Optional[int] = Field(None, alias='memberships_count')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    pronouns: typing.Optional[str] = Field(None, alias='pronouns')

    status_default_emoji: typing.Optional[str] = Field(None, alias='status_default_emoji')

    status_default_text: typing.Optional[str] = Field(None, alias='status_default_text')

    status_default_text_canonical: typing.Optional[typing.Optional[str]] = Field(None, alias='status_default_text_canonical')

    status_expiration: typing.Optional[int] = Field(None, alias='status_expiration')

    status_text_canonical: typing.Optional[typing.Optional[str]] = Field(None, alias='status_text_canonical')

    team: typing.Optional[DefsWorkspaceId] = Field(None, alias='team')

    updated: typing.Optional[int] = Field(None, alias='updated')

    user_id: typing.Optional[str] = Field(None, alias='user_id')

    username: typing.Optional[typing.Optional[str]] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
