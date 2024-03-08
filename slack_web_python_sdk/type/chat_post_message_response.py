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
from slack_web_python_sdk.type.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.type.defs_ts import DefsTs
from slack_web_python_sdk.type.objs_message import ObjsMessage

class RequiredChatPostMessageResponse(TypedDict):
    channel: DefsChannel

    message: ObjsMessage

    ok: DefsOkTrue

    ts: DefsTs

class OptionalChatPostMessageResponse(TypedDict, total=False):
    pass

class ChatPostMessageResponse(RequiredChatPostMessageResponse, OptionalChatPostMessageResponse):
    pass
