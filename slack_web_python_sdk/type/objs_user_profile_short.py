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

from slack_web_python_sdk.type.defs_workspace_id import DefsWorkspaceId

class RequiredObjsUserProfileShort(TypedDict):
    avatar_hash: str

    display_name: str

    first_name: typing.Optional[str]

    image_72: str

    is_restricted: bool

    is_ultra_restricted: bool

    name: str

    real_name: str

    team: DefsWorkspaceId

class OptionalObjsUserProfileShort(TypedDict, total=False):
    display_name_normalized: str

    real_name_normalized: str

class ObjsUserProfileShort(RequiredObjsUserProfileShort, OptionalObjsUserProfileShort):
    pass
