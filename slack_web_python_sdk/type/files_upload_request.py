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


class RequiredFilesUploadRequest(TypedDict):
    pass

class OptionalFilesUploadRequest(TypedDict, total=False):
    # Title of file.
    title: str

    # Comma-separated list of channel names or IDs where the file will be shared.
    channels: str

    # File contents via a POST variable. If omitting this parameter, you must provide a `file`.
    content: str

    # File contents via `multipart/form-data`. If omitting this parameter, you must submit `content`.
    file: str

    # Filename of file.
    filename: str

    # A [file type](https://slack.dev) identifier.
    filetype: str

    # The message text introducing the file in specified `channels`.
    initial_comment: str

    # Provide another message's `ts` value to upload this file as a reply. Never use a reply's `ts` value; use its parent instead.
    thread_ts: typing.Union[int, float]

    # Authentication token. Requires scope: `files:write:user`
    token: str

class FilesUploadRequest(RequiredFilesUploadRequest, OptionalFilesUploadRequest):
    pass
