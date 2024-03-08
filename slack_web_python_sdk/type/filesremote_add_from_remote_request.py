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


class RequiredFilesremoteAddFromRemoteRequest(TypedDict):
    pass

class OptionalFilesremoteAddFromRemoteRequest(TypedDict, total=False):
    # Title of the file being shared.
    title: str

    # Creator defined GUID for the file.
    external_id: str

    # URL of the remote file.
    external_url: str

    # type of file
    filetype: str

    # A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.
    indexable_file_contents: str

    # Preview of the document via `multipart/form-data`.
    preview_image: str

    # Authentication token. Requires scope: `remote_files:write`
    token: str

class FilesremoteAddFromRemoteRequest(RequiredFilesremoteAddFromRemoteRequest, OptionalFilesremoteAddFromRemoteRequest):
    pass
