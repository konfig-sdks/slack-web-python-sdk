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

from slack_web_python_sdk.pydantic.chatscheduled_messages_list_response_response_metadata import ChatscheduledMessagesListResponseResponseMetadata
from slack_web_python_sdk.pydantic.chatscheduled_messages_list_response_scheduled_messages import ChatscheduledMessagesListResponseScheduledMessages
from slack_web_python_sdk.pydantic.defs_ok_true import DefsOkTrue

class ChatscheduledMessagesListResponse(BaseModel):
    ok: DefsOkTrue = Field(alias='ok')

    response_metadata: ChatscheduledMessagesListResponseResponseMetadata = Field(alias='response_metadata')

    scheduled_messages: ChatscheduledMessagesListResponseScheduledMessages = Field(alias='scheduled_messages')
    class Config:
        arbitrary_types_allowed = True