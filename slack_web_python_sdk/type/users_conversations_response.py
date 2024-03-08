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

from slack_web_python_sdk.type.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.type.objs_conversation import ObjsConversation
from slack_web_python_sdk.type.users_conversations_response_response_metadata import UsersConversationsResponseResponseMetadata

class RequiredUsersConversationsResponse(TypedDict):
    channels: typing.List[ObjsConversation]

    ok: DefsOkTrue

class OptionalUsersConversationsResponse(TypedDict, total=False):
    response_metadata: UsersConversationsResponseResponseMetadata

class UsersConversationsResponse(RequiredUsersConversationsResponse, OptionalUsersConversationsResponse):
    pass
