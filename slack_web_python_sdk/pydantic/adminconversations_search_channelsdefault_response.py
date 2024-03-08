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
from pydantic import BaseModel, Field, RootModel

from slack_web_python_sdk.pydantic.defs_ok_false import DefsOkFalse

class AdminconversationsSearchChannelsdefaultResponse(BaseModel):
    error: Literal["feature_not_enabled", "not_an_admin", "not_an_enterprise", "team_not_found", "not_allowed", "invalid_auth", "invalid_cursor", "invalid_search_channel_type", "invalid_sort", "invalid_sort_dir"] = Field(alias='error')

    ok: DefsOkFalse = Field(alias='ok')
    class Config:
        arbitrary_types_allowed = True
