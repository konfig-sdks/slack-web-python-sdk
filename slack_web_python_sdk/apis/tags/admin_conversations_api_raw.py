# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.admin_conversations_archive.post import ArchiveChannelRaw
from slack_web_python_sdk.paths.admin_conversations_convert_to_private.post import ConvertToPrivateChannelRaw
from slack_web_python_sdk.paths.admin_conversations_create.post import CreateChannelBasedConversationRaw
from slack_web_python_sdk.paths.admin_conversations_delete.post import DeleteChannelRaw
from slack_web_python_sdk.paths.admin_conversations_disconnect_shared.post import DisconnectSharedChannelRaw
from slack_web_python_sdk.paths.admin_conversations_get_conversation_prefs.get import GetConversationPrefsRaw
from slack_web_python_sdk.paths.admin_conversations_get_teams.get import GetTeamsListRaw
from slack_web_python_sdk.paths.admin_conversations_invite.post import InviteUserToChannelRaw
from slack_web_python_sdk.paths.admin_conversations_rename.post import RenameChannelRaw
from slack_web_python_sdk.paths.admin_conversations_search.get import SearchChannelsRaw
from slack_web_python_sdk.paths.admin_conversations_set_conversation_prefs.post import SetConversationPrefsRaw
from slack_web_python_sdk.paths.admin_conversations_set_teams.post import SetTeamsWorkspaceConnectionRaw
from slack_web_python_sdk.paths.admin_conversations_unarchive.post import UnarchiveChannelRaw


class AdminConversationsApiRaw(
    ArchiveChannelRaw,
    ConvertToPrivateChannelRaw,
    CreateChannelBasedConversationRaw,
    DeleteChannelRaw,
    DisconnectSharedChannelRaw,
    GetConversationPrefsRaw,
    GetTeamsListRaw,
    InviteUserToChannelRaw,
    RenameChannelRaw,
    SearchChannelsRaw,
    SetConversationPrefsRaw,
    SetTeamsWorkspaceConnectionRaw,
    UnarchiveChannelRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
