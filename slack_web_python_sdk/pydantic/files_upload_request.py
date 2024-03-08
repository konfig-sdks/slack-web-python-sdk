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


class FilesUploadRequest(BaseModel):
    # Title of file.
    title: typing.Optional[str] = Field(None, alias='title')

    # Comma-separated list of channel names or IDs where the file will be shared.
    channels: typing.Optional[str] = Field(None, alias='channels')

    # File contents via a POST variable. If omitting this parameter, you must provide a `file`.
    content: typing.Optional[str] = Field(None, alias='content')

    # File contents via `multipart/form-data`. If omitting this parameter, you must submit `content`.
    file: typing.Optional[str] = Field(None, alias='file')

    # Filename of file.
    filename: typing.Optional[str] = Field(None, alias='filename')

    # A [file type](https://slack.dev) identifier.
    filetype: typing.Optional[str] = Field(None, alias='filetype')

    # The message text introducing the file in specified `channels`.
    initial_comment: typing.Optional[str] = Field(None, alias='initial_comment')

    # Provide another message's `ts` value to upload this file as a reply. Never use a reply's `ts` value; use its parent instead.
    thread_ts: typing.Optional[typing.Union[int, float]] = Field(None, alias='thread_ts')

    # Authentication token. Requires scope: `files:write:user`
    token: typing.Optional[str] = Field(None, alias='token')
    class Config:
        arbitrary_types_allowed = True
