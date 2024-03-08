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

from slack_web_python_sdk.type.defs_dm_id import DefsDmId
from slack_web_python_sdk.type.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.type.defs_ts import DefsTs
from slack_web_python_sdk.type.defs_user_id import DefsUserId
from slack_web_python_sdk.type.objs_conversation import ObjsConversation
from slack_web_python_sdk.type.objs_message import ObjsMessage

class RequiredConversationsOpenResponse(TypedDict):
    channel: typing.List[typing.Union[typing.List[ObjsConversation], typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]]

    ok: DefsOkTrue

class OptionalConversationsOpenResponse(TypedDict, total=False):
    already_open: bool

    no_op: bool

class ConversationsOpenResponse(RequiredConversationsOpenResponse, OptionalConversationsOpenResponse):
    pass
