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


class RequiredCallsUpdateRequest(TypedDict):
    # `id` returned by the [`calls.add`](https://slack.dev) method.
    id: str

class OptionalCallsUpdateRequest(TypedDict, total=False):
    # The name of the Call.
    title: str

    # When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
    desktop_app_join_url: str

    # The URL required for a client to join the Call.
    join_url: str

class CallsUpdateRequest(RequiredCallsUpdateRequest, OptionalCallsUpdateRequest):
    pass
