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


class RequiredCallsAddRequest(TypedDict):
    # An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service.
    external_unique_id: str

    # The URL required for a client to join the Call.
    join_url: str

class OptionalCallsAddRequest(TypedDict, total=False):
    # The name of the Call.
    title: str

    # The valid Slack user ID of the user who created this Call. When this method is called with a user token, the `created_by` field is optional and defaults to the authed user of the token. Otherwise, the field is required.
    created_by: str

    # Call start time in UTC UNIX timestamp format
    date_start: int

    # When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
    desktop_app_join_url: str

    # An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object.
    external_display_id: str

    # The list of users to register as participants in the Call. [Read more on how to specify users here](https://slack.dev).
    users: str

class CallsAddRequest(RequiredCallsAddRequest, OptionalCallsAddRequest):
    pass
