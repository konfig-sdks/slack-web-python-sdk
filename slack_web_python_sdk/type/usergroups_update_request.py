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


class RequiredUsergroupsUpdateRequest(TypedDict):
    # The encoded ID of the User Group to update.
    usergroup: str

class OptionalUsergroupsUpdateRequest(TypedDict, total=False):
    # A short description of the User Group.
    description: str

    # A comma separated string of encoded channel IDs for which the User Group uses as a default.
    channels: str

    # A mention handle. Must be unique among channels, users and User Groups.
    handle: str

    # Include the number of users in the User Group.
    include_count: bool

    # A name for the User Group. Must be unique among User Groups.
    name: str

class UsergroupsUpdateRequest(RequiredUsergroupsUpdateRequest, OptionalUsergroupsUpdateRequest):
    pass
