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


class RequiredUsergroupsusersUpdateListRequest(TypedDict):
    # The encoded ID of the User Group to update.
    usergroup: str

    # A comma separated string of encoded user IDs that represent the entire list of users for the User Group.
    users: str

class OptionalUsergroupsusersUpdateListRequest(TypedDict, total=False):
    # Include the number of users in the User Group.
    include_count: bool

class UsergroupsusersUpdateListRequest(RequiredUsergroupsusersUpdateListRequest, OptionalUsergroupsusersUpdateListRequest):
    pass
