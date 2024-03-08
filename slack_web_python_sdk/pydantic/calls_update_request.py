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


class CallsUpdateRequest(BaseModel):
    # `id` returned by the [`calls.add`](https://slack.dev) method.
    id: str = Field(alias='id')

    # The name of the Call.
    title: typing.Optional[str] = Field(None, alias='title')

    # When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
    desktop_app_join_url: typing.Optional[str] = Field(None, alias='desktop_app_join_url')

    # The URL required for a client to join the Call.
    join_url: typing.Optional[str] = Field(None, alias='join_url')
    class Config:
        arbitrary_types_allowed = True
