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


class RequiredConversationsInviteRequest(TypedDict):
    pass

class OptionalConversationsInviteRequest(TypedDict, total=False):
    # The ID of the public or private channel to invite user(s) to.
    channel: str

    # A comma separated list of user IDs. Up to 1000 users may be listed.
    users: str

class ConversationsInviteRequest(RequiredConversationsInviteRequest, OptionalConversationsInviteRequest):
    pass
