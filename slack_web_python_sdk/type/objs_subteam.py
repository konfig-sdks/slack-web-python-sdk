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

from slack_web_python_sdk.type.defs_subteam_id import DefsSubteamId
from slack_web_python_sdk.type.defs_team import DefsTeam
from slack_web_python_sdk.type.defs_user_id import DefsUserId
from slack_web_python_sdk.type.objs_subteam_prefs import ObjsSubteamPrefs

class RequiredObjsSubteam(TypedDict):
    description: str

    auto_provision: bool

    auto_type: typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[str]]]

    created_by: DefsUserId

    date_create: int

    date_delete: int

    date_update: int

    deleted_by: typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[DefsUserId]]]

    enterprise_subteam_id: str

    handle: str

    id: DefsSubteamId

    is_external: bool

    is_subteam: bool

    is_usergroup: bool

    name: str

    prefs: ObjsSubteamPrefs

    team_id: DefsTeam

    updated_by: DefsUserId

class OptionalObjsSubteam(TypedDict, total=False):
    channel_count: int

    user_count: int

    users: typing.List[DefsUserId]

class ObjsSubteam(RequiredObjsSubteam, OptionalObjsSubteam):
    pass
