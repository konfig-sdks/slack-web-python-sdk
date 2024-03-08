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

from slack_web_python_sdk.type.defs_channel_id import DefsChannelId
from slack_web_python_sdk.type.defs_group_id import DefsGroupId

class RequiredObjsSubteamPrefs(TypedDict):
    channels: typing.List[DefsChannelId]

    groups: typing.List[DefsGroupId]

class OptionalObjsSubteamPrefs(TypedDict, total=False):
    pass

class ObjsSubteamPrefs(RequiredObjsSubteamPrefs, OptionalObjsSubteamPrefs):
    pass
