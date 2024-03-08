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


class RequiredAdminusersSetExpirationGuestRequest(TypedDict):
    # Timestamp when guest account should be disabled.
    expiration_ts: int

    # The ID (`T1234`) of the workspace.
    team_id: str

    # The ID of the user to set an expiration for.
    user_id: str

class OptionalAdminusersSetExpirationGuestRequest(TypedDict, total=False):
    pass

class AdminusersSetExpirationGuestRequest(RequiredAdminusersSetExpirationGuestRequest, OptionalAdminusersSetExpirationGuestRequest):
    pass
