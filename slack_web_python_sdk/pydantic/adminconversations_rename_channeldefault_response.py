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

class AdminconversationsRenameChanneldefaultResponse(BaseModel):
    error: Literal["feature_not_enabled", "channel_not_found", "channel_type_not_supported", "restricted_action", "could_not_rename_channel", "default_org_wide_channel", "name_taken"] = Field(alias='error')

    ok: DefsOkFalse = Field(alias='ok')
    class Config:
        arbitrary_types_allowed = True
