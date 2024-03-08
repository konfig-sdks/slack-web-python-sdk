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

from slack_web_python_sdk.type.bots_info_response_bot_icons import BotsInfoResponseBotIcons
from slack_web_python_sdk.type.defs_app_id import DefsAppId
from slack_web_python_sdk.type.defs_bot_id import DefsBotId
from slack_web_python_sdk.type.defs_user_id import DefsUserId

class RequiredBotsInfoResponseBot(TypedDict):
    app_id: DefsAppId

    deleted: bool

    icons: BotsInfoResponseBotIcons

    id: DefsBotId

    name: str

    updated: int

class OptionalBotsInfoResponseBot(TypedDict, total=False):
    user_id: DefsUserId

class BotsInfoResponseBot(RequiredBotsInfoResponseBot, OptionalBotsInfoResponseBot):
    pass
