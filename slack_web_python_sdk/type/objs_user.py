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

from slack_web_python_sdk.type.defs_user_id import DefsUserId
from slack_web_python_sdk.type.defs_workspace_id import DefsWorkspaceId
from slack_web_python_sdk.type.objs_enterprise_user import ObjsEnterpriseUser
from slack_web_python_sdk.type.objs_team_profile_field import ObjsTeamProfileField
from slack_web_python_sdk.type.objs_user_profile import ObjsUserProfile

ObjsUser = typing.List[typing.Union[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]], typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]]
