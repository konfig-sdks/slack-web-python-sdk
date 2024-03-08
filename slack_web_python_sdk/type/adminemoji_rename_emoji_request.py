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


class RequiredAdminemojiRenameEmojiRequest(TypedDict):
    # The name of the emoji to be renamed. Colons (`:myemoji:`) around the value are not required, although they may be included.
    name: str

    # The new name of the emoji.
    new_name: str

    # Authentication token. Requires scope: `admin.teams:write`
    token: str

class OptionalAdminemojiRenameEmojiRequest(TypedDict, total=False):
    pass

class AdminemojiRenameEmojiRequest(RequiredAdminemojiRenameEmojiRequest, OptionalAdminemojiRenameEmojiRequest):
    pass
