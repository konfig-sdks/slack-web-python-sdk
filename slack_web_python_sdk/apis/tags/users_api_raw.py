# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.users_conversations.get import ConversationsRaw
from slack_web_python_sdk.paths.users_delete_photo.post import DeletePhotoRaw
from slack_web_python_sdk.paths.users_get_presence.get import GetPresenceRaw
from slack_web_python_sdk.paths.users_profile_get.get import GetProfileInfoRaw
from slack_web_python_sdk.paths.users_identity.get import IdentityRaw
from slack_web_python_sdk.paths.users_info.get import InfoRaw
from slack_web_python_sdk.paths.users_list.get import ListRaw
from slack_web_python_sdk.paths.users_lookup_by_email.get import LookupByEmailRaw
from slack_web_python_sdk.paths.users_set_active.post import SetActiveRaw
from slack_web_python_sdk.paths.users_set_photo.post import SetPhotoRaw
from slack_web_python_sdk.paths.users_set_presence.post import SetPresenceRaw
from slack_web_python_sdk.paths.users_profile_set.post import SetProfileInfoRaw


class UsersApiRaw(
    ConversationsRaw,
    DeletePhotoRaw,
    GetPresenceRaw,
    GetProfileInfoRaw,
    IdentityRaw,
    InfoRaw,
    ListRaw,
    LookupByEmailRaw,
    SetActiveRaw,
    SetPhotoRaw,
    SetPresenceRaw,
    SetProfileInfoRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
