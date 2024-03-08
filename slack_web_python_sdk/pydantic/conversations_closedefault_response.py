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

class ConversationsClosedefaultResponse(BaseModel):
    error: Literal["method_not_supported_for_channel_type", "channel_not_found", "user_does_not_own_channel", "missing_scope", "not_authed", "invalid_auth", "account_inactive", "invalid_arg_name", "invalid_array_arg", "invalid_charset", "invalid_form_data", "invalid_post_type", "missing_post_type", "team_added_to_org", "invalid_json", "json_not_object", "request_timeout", "upgrade_required"] = Field(alias='error')

    ok: DefsOkFalse = Field(alias='ok')

    # Note: PHP callstack is only visible in dev/qa
    callstack: typing.Optional[str] = Field(None, alias='callstack')

    needed: typing.Optional[str] = Field(None, alias='needed')

    provided: typing.Optional[str] = Field(None, alias='provided')
    class Config:
        arbitrary_types_allowed = True
