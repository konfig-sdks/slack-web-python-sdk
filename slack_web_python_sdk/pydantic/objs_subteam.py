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

from slack_web_python_sdk.pydantic.defs_subteam_id import DefsSubteamId
from slack_web_python_sdk.pydantic.defs_team import DefsTeam
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId
from slack_web_python_sdk.pydantic.objs_subteam_prefs import ObjsSubteamPrefs

class ObjsSubteam(BaseModel):
    description: str = Field(alias='description')

    auto_provision: bool = Field(alias='auto_provision')

    auto_type: typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[str]]] = Field(alias='auto_type')

    created_by: DefsUserId = Field(alias='created_by')

    date_create: int = Field(alias='date_create')

    date_delete: int = Field(alias='date_delete')

    date_update: int = Field(alias='date_update')

    deleted_by: typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[DefsUserId]]] = Field(alias='deleted_by')

    enterprise_subteam_id: str = Field(alias='enterprise_subteam_id')

    handle: str = Field(alias='handle')

    id: DefsSubteamId = Field(alias='id')

    is_external: bool = Field(alias='is_external')

    is_subteam: bool = Field(alias='is_subteam')

    is_usergroup: bool = Field(alias='is_usergroup')

    name: str = Field(alias='name')

    prefs: ObjsSubteamPrefs = Field(alias='prefs')

    team_id: DefsTeam = Field(alias='team_id')

    updated_by: DefsUserId = Field(alias='updated_by')

    channel_count: typing.Optional[int] = Field(None, alias='channel_count')

    user_count: typing.Optional[int] = Field(None, alias='user_count')

    users: typing.Optional[typing.List[DefsUserId]] = Field(None, alias='users')
    class Config:
        arbitrary_types_allowed = True
