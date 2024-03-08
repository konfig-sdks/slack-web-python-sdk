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

from slack_web_python_sdk.pydantic.chat_update_response_message_attachments import ChatUpdateResponseMessageAttachments

class ChatUpdateResponseMessage(BaseModel):
    text: str = Field(alias='text')

    attachments: typing.Optional[ChatUpdateResponseMessageAttachments] = Field(None, alias='attachments')

    blocks: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='blocks')
    class Config:
        arbitrary_types_allowed = True
