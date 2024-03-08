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


class RequiredConversationsOpenRequest(TypedDict):
    pass

class OptionalConversationsOpenRequest(TypedDict, total=False):
    # Resume a conversation by supplying an `im` or `mpim`'s ID. Or provide the `users` field instead.
    channel: str

    # Boolean, indicates you want the full IM channel definition in the response.
    return_im: bool

    # Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a `channel` when not supplying `users`.
    users: str

class ConversationsOpenRequest(RequiredConversationsOpenRequest, OptionalConversationsOpenRequest):
    pass
