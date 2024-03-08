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


class RequiredUsersSetPhotoRequest(TypedDict):
    # Authentication token. Requires scope: `users.profile:write`
    token: str

class OptionalUsersSetPhotoRequest(TypedDict, total=False):
    # Width/height of crop box (always square)
    crop_w: str

    # X coordinate of top-left corner of crop box
    crop_x: str

    # Y coordinate of top-left corner of crop box
    crop_y: str

    # File contents via `multipart/form-data`.
    image: str

class UsersSetPhotoRequest(RequiredUsersSetPhotoRequest, OptionalUsersSetPhotoRequest):
    pass
