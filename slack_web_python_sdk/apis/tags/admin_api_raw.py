# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.admin_usergroups_add_channels.post import AddDefaultChannelsRaw
from slack_web_python_sdk.paths.admin_emoji_add.post import AddEmojiRaw
from slack_web_python_sdk.paths.admin_conversations_restrict_access_add_group.post import AddGroupIdpGroupsRaw
from slack_web_python_sdk.paths.admin_users_assign.post import AddWorkspaceUserRaw
from slack_web_python_sdk.paths.admin_emoji_add_alias.post import AliasAddRaw
from slack_web_python_sdk.paths.admin_apps_approve.post import ApproveAppInstallationRaw
from slack_web_python_sdk.paths.admin_invite_requests_approve.post import ApproveRequestRaw
from slack_web_python_sdk.paths.admin_conversations_archive.post import ArchiveChannelRaw
from slack_web_python_sdk.paths.admin_usergroups_add_teams.post import AssociateDefaultWorkspacesRaw
from slack_web_python_sdk.paths.admin_conversations_convert_to_private.post import ConvertToPrivateChannelRaw
from slack_web_python_sdk.paths.admin_conversations_create.post import CreateChannelBasedConversationRaw
from slack_web_python_sdk.paths.admin_teams_create.post import CreateEnterpriseTeamRaw
from slack_web_python_sdk.paths.admin_conversations_delete.post import DeleteChannelRaw
from slack_web_python_sdk.paths.admin_invite_requests_deny.post import DenyRequestRaw
from slack_web_python_sdk.paths.admin_conversations_disconnect_shared.post import DisconnectSharedChannelRaw
from slack_web_python_sdk.paths.admin_teams_admins_list.get import GetAllRaw
from slack_web_python_sdk.paths.admin_conversations_get_conversation_prefs.get import GetConversationPrefsRaw
from slack_web_python_sdk.paths.admin_teams_settings_info.get import GetInfoRaw
from slack_web_python_sdk.paths.admin_apps_restricted_list.get import GetListRaw
from slack_web_python_sdk.paths.admin_conversations_get_teams.get import GetTeamsListRaw
from slack_web_python_sdk.paths.admin_users_session_invalidate.post import InvalidateSessionRaw
from slack_web_python_sdk.paths.admin_conversations_invite.post import InviteUserToChannelRaw
from slack_web_python_sdk.paths.admin_users_invite.post import InviteUserToWorkspaceRaw
from slack_web_python_sdk.paths.admin_apps_approved_list.get import ListRaw
from slack_web_python_sdk.paths.admin_apps_requests_list.get import List0Raw
from slack_web_python_sdk.paths.admin_invite_requests_approved_list.get import List1Raw
from slack_web_python_sdk.paths.admin_invite_requests_denied_list.get import List2Raw
from slack_web_python_sdk.paths.admin_teams_list.get import ListAllRaw
from slack_web_python_sdk.paths.admin_usergroups_list_channels.get import ListChannelsGetRaw
from slack_web_python_sdk.paths.admin_emoji_list.get import ListEnterpriseEmojiRaw
from slack_web_python_sdk.paths.admin_conversations_restrict_access_list_groups.get import ListGroupsRaw
from slack_web_python_sdk.paths.admin_conversations_ekm_list_original_connected_channel_info.get import ListOriginalConnectedChannelInfoRaw
from slack_web_python_sdk.paths.admin_teams_owners_list.get import ListOwnersRaw
from slack_web_python_sdk.paths.admin_invite_requests_list.get import ListPendingWorkspaceInviteRequestsRaw
from slack_web_python_sdk.paths.admin_users_list.get import ListWorkspaceUsersRaw
from slack_web_python_sdk.paths.admin_usergroups_remove_channels.post import RemoveChannelsRaw
from slack_web_python_sdk.paths.admin_emoji_remove.post import RemoveEnterpriseEmojiRaw
from slack_web_python_sdk.paths.admin_conversations_restrict_access_remove_group.post import RemoveIdpGroupRaw
from slack_web_python_sdk.paths.admin_users_remove.post import RemoveUserFromWorkspaceRaw
from slack_web_python_sdk.paths.admin_conversations_rename.post import RenameChannelRaw
from slack_web_python_sdk.paths.admin_emoji_rename.post import RenameEmojiRaw
from slack_web_python_sdk.paths.admin_users_session_reset.post import ResetSessionsRaw
from slack_web_python_sdk.paths.admin_apps_restrict.post import RestrictAppRaw
from slack_web_python_sdk.paths.admin_conversations_search.get import SearchChannelsRaw
from slack_web_python_sdk.paths.admin_users_set_admin.post import SetAdminUserRaw
from slack_web_python_sdk.paths.admin_conversations_set_conversation_prefs.post import SetConversationPrefsRaw
from slack_web_python_sdk.paths.admin_teams_settings_set_default_channels.post import SetDefaultChannelsRaw
from slack_web_python_sdk.paths.admin_teams_settings_set_description.post import SetDescriptionRaw
from slack_web_python_sdk.paths.admin_teams_settings_set_discoverability.post import SetDiscoverabilityOfWorkspaceRaw
from slack_web_python_sdk.paths.admin_users_set_expiration.post import SetExpirationGuestRaw
from slack_web_python_sdk.paths.admin_teams_settings_set_icon.post import SetIconRaw
from slack_web_python_sdk.paths.admin_teams_settings_set_name.post import SetNameRaw
from slack_web_python_sdk.paths.admin_users_set_regular.post import SetRegularUserRaw
from slack_web_python_sdk.paths.admin_conversations_set_teams.post import SetTeamsWorkspaceConnectionRaw
from slack_web_python_sdk.paths.admin_users_set_owner.post import SetWorkspaceOwnerRaw
from slack_web_python_sdk.paths.admin_conversations_unarchive.post import UnarchiveChannelRaw


class AdminApiRaw(
    AddDefaultChannelsRaw,
    AddEmojiRaw,
    AddGroupIdpGroupsRaw,
    AddWorkspaceUserRaw,
    AliasAddRaw,
    ApproveAppInstallationRaw,
    ApproveRequestRaw,
    ArchiveChannelRaw,
    AssociateDefaultWorkspacesRaw,
    ConvertToPrivateChannelRaw,
    CreateChannelBasedConversationRaw,
    CreateEnterpriseTeamRaw,
    DeleteChannelRaw,
    DenyRequestRaw,
    DisconnectSharedChannelRaw,
    GetAllRaw,
    GetConversationPrefsRaw,
    GetInfoRaw,
    GetListRaw,
    GetTeamsListRaw,
    InvalidateSessionRaw,
    InviteUserToChannelRaw,
    InviteUserToWorkspaceRaw,
    ListRaw,
    List0Raw,
    List1Raw,
    List2Raw,
    ListAllRaw,
    ListChannelsGetRaw,
    ListEnterpriseEmojiRaw,
    ListGroupsRaw,
    ListOriginalConnectedChannelInfoRaw,
    ListOwnersRaw,
    ListPendingWorkspaceInviteRequestsRaw,
    ListWorkspaceUsersRaw,
    RemoveChannelsRaw,
    RemoveEnterpriseEmojiRaw,
    RemoveIdpGroupRaw,
    RemoveUserFromWorkspaceRaw,
    RenameChannelRaw,
    RenameEmojiRaw,
    ResetSessionsRaw,
    RestrictAppRaw,
    SearchChannelsRaw,
    SetAdminUserRaw,
    SetConversationPrefsRaw,
    SetDefaultChannelsRaw,
    SetDescriptionRaw,
    SetDiscoverabilityOfWorkspaceRaw,
    SetExpirationGuestRaw,
    SetIconRaw,
    SetNameRaw,
    SetRegularUserRaw,
    SetTeamsWorkspaceConnectionRaw,
    SetWorkspaceOwnerRaw,
    UnarchiveChannelRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
