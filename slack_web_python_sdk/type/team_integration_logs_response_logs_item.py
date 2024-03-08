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

from slack_web_python_sdk.type.defs_app_id import DefsAppId
from slack_web_python_sdk.type.defs_channel import DefsChannel
from slack_web_python_sdk.type.defs_user_id import DefsUserId

class RequiredTeamIntegrationLogsResponseLogsItem(TypedDict):
    app_id: DefsAppId

    app_type: str

    change_type: str

    date: str

    scope: str

    user_id: DefsUserId

    user_name: str

class OptionalTeamIntegrationLogsResponseLogsItem(TypedDict, total=False):
    admin_app_id: DefsAppId

    channel: DefsChannel

    service_id: str

    service_type: str

class TeamIntegrationLogsResponseLogsItem(RequiredTeamIntegrationLogsResponseLogsItem, OptionalTeamIntegrationLogsResponseLogsItem):
    pass
