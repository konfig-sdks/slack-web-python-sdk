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


class RequiredUsersSetPhotoResponseProfile(TypedDict):
    avatar_hash: str

    image_1024: str

    image_192: str

    image_24: str

    image_32: str

    image_48: str

    image_512: str

    image_72: str

    image_original: str

class OptionalUsersSetPhotoResponseProfile(TypedDict, total=False):
    pass

class UsersSetPhotoResponseProfile(RequiredUsersSetPhotoResponseProfile, OptionalUsersSetPhotoResponseProfile):
    pass
