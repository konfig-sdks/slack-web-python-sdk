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


class CallsparticipantsAddNewParticipantRequest(BaseModel):
    # `id` returned by the [`calls.add`](https://slack.dev) method.
    id: str = Field(alias='id')

    # The list of users to add as participants in the Call. [Read more on how to specify users here](https://slack.dev).
    users: str = Field(alias='users')
    class Config:
        arbitrary_types_allowed = True
