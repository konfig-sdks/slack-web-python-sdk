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

class ChatPostMessagedefaultResponse(BaseModel):
    error: Literal["channel_not_found", "not_in_channel", "is_archived", "msg_too_long", "no_text", "too_many_attachments", "rate_limited", "not_authed", "invalid_auth", "account_inactive", "invalid_arg_name", "invalid_array_arg", "invalid_charset", "invalid_form_data", "invalid_post_type", "missing_post_type"] = Field(alias='error')

    ok: DefsOkFalse = Field(alias='ok')

    # Note: PHP callstack is only visible in dev/qa
    callstack: typing.Optional[str] = Field(None, alias='callstack')
    class Config:
        arbitrary_types_allowed = True
