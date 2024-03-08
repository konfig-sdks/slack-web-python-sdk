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


class FilesremoteUpdateRemoteFileRequest(BaseModel):
    # Title of the file being shared.
    title: typing.Optional[str] = Field(None, alias='title')

    # Creator defined GUID for the file.
    external_id: typing.Optional[str] = Field(None, alias='external_id')

    # URL of the remote file.
    external_url: typing.Optional[str] = Field(None, alias='external_url')

    # Specify a file by providing its ID.
    file: typing.Optional[str] = Field(None, alias='file')

    # type of file
    filetype: typing.Optional[str] = Field(None, alias='filetype')

    # File containing contents that can be used to improve searchability for the remote file.
    indexable_file_contents: typing.Optional[str] = Field(None, alias='indexable_file_contents')

    # Preview of the document via `multipart/form-data`.
    preview_image: typing.Optional[str] = Field(None, alias='preview_image')

    # Authentication token. Requires scope: `remote_files:write`
    token: typing.Optional[str] = Field(None, alias='token')
    class Config:
        arbitrary_types_allowed = True
