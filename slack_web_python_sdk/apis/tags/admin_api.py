# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.admin_usergroups_add_channels.post import AddDefaultChannels
from slack_web_python_sdk.paths.admin_emoji_add.post import AddEmoji
from slack_web_python_sdk.paths.admin_conversations_restrict_access_add_group.post import AddGroupIdpGroups
from slack_web_python_sdk.paths.admin_users_assign.post import AddWorkspaceUser
from slack_web_python_sdk.paths.admin_emoji_add_alias.post import AliasAdd
from slack_web_python_sdk.paths.admin_apps_approve.post import ApproveAppInstallation
from slack_web_python_sdk.paths.admin_invite_requests_approve.post import ApproveRequest
from slack_web_python_sdk.paths.admin_conversations_archive.post import ArchiveChannel
from slack_web_python_sdk.paths.admin_usergroups_add_teams.post import AssociateDefaultWorkspaces
from slack_web_python_sdk.paths.admin_conversations_convert_to_private.post import ConvertToPrivateChannel
from slack_web_python_sdk.paths.admin_conversations_create.post import CreateChannelBasedConversation
from slack_web_python_sdk.paths.admin_teams_create.post import CreateEnterpriseTeam
from slack_web_python_sdk.paths.admin_conversations_delete.post import DeleteChannel
from slack_web_python_sdk.paths.admin_invite_requests_deny.post import DenyRequest
from slack_web_python_sdk.paths.admin_conversations_disconnect_shared.post import DisconnectSharedChannel
from slack_web_python_sdk.paths.admin_teams_admins_list.get import GetAll
from slack_web_python_sdk.paths.admin_conversations_get_conversation_prefs.get import GetConversationPrefs
from slack_web_python_sdk.paths.admin_teams_settings_info.get import GetInfo
from slack_web_python_sdk.paths.admin_apps_restricted_list.get import GetList
from slack_web_python_sdk.paths.admin_conversations_get_teams.get import GetTeamsList
from slack_web_python_sdk.paths.admin_users_session_invalidate.post import InvalidateSession
from slack_web_python_sdk.paths.admin_conversations_invite.post import InviteUserToChannel
from slack_web_python_sdk.paths.admin_users_invite.post import InviteUserToWorkspace
from slack_web_python_sdk.paths.admin_apps_approved_list.get import List
from slack_web_python_sdk.paths.admin_apps_requests_list.get import List0
from slack_web_python_sdk.paths.admin_invite_requests_approved_list.get import List1
from slack_web_python_sdk.paths.admin_invite_requests_denied_list.get import List2
from slack_web_python_sdk.paths.admin_teams_list.get import ListAll
from slack_web_python_sdk.paths.admin_usergroups_list_channels.get import ListChannelsGet
from slack_web_python_sdk.paths.admin_emoji_list.get import ListEnterpriseEmoji
from slack_web_python_sdk.paths.admin_conversations_restrict_access_list_groups.get import ListGroups
from slack_web_python_sdk.paths.admin_conversations_ekm_list_original_connected_channel_info.get import ListOriginalConnectedChannelInfo
from slack_web_python_sdk.paths.admin_teams_owners_list.get import ListOwners
from slack_web_python_sdk.paths.admin_invite_requests_list.get import ListPendingWorkspaceInviteRequests
from slack_web_python_sdk.paths.admin_users_list.get import ListWorkspaceUsers
from slack_web_python_sdk.paths.admin_usergroups_remove_channels.post import RemoveChannels
from slack_web_python_sdk.paths.admin_emoji_remove.post import RemoveEnterpriseEmoji
from slack_web_python_sdk.paths.admin_conversations_restrict_access_remove_group.post import RemoveIdpGroup
from slack_web_python_sdk.paths.admin_users_remove.post import RemoveUserFromWorkspace
from slack_web_python_sdk.paths.admin_conversations_rename.post import RenameChannel
from slack_web_python_sdk.paths.admin_emoji_rename.post import RenameEmoji
from slack_web_python_sdk.paths.admin_users_session_reset.post import ResetSessions
from slack_web_python_sdk.paths.admin_apps_restrict.post import RestrictApp
from slack_web_python_sdk.paths.admin_conversations_search.get import SearchChannels
from slack_web_python_sdk.paths.admin_users_set_admin.post import SetAdminUser
from slack_web_python_sdk.paths.admin_conversations_set_conversation_prefs.post import SetConversationPrefs
from slack_web_python_sdk.paths.admin_teams_settings_set_default_channels.post import SetDefaultChannels
from slack_web_python_sdk.paths.admin_teams_settings_set_description.post import SetDescription
from slack_web_python_sdk.paths.admin_teams_settings_set_discoverability.post import SetDiscoverabilityOfWorkspace
from slack_web_python_sdk.paths.admin_users_set_expiration.post import SetExpirationGuest
from slack_web_python_sdk.paths.admin_teams_settings_set_icon.post import SetIcon
from slack_web_python_sdk.paths.admin_teams_settings_set_name.post import SetName
from slack_web_python_sdk.paths.admin_users_set_regular.post import SetRegularUser
from slack_web_python_sdk.paths.admin_conversations_set_teams.post import SetTeamsWorkspaceConnection
from slack_web_python_sdk.paths.admin_users_set_owner.post import SetWorkspaceOwner
from slack_web_python_sdk.paths.admin_conversations_unarchive.post import UnarchiveChannel
from slack_web_python_sdk.apis.tags.admin_api_raw import AdminApiRaw


class AdminApi(
    AddDefaultChannels,
    AddEmoji,
    AddGroupIdpGroups,
    AddWorkspaceUser,
    AliasAdd,
    ApproveAppInstallation,
    ApproveRequest,
    ArchiveChannel,
    AssociateDefaultWorkspaces,
    ConvertToPrivateChannel,
    CreateChannelBasedConversation,
    CreateEnterpriseTeam,
    DeleteChannel,
    DenyRequest,
    DisconnectSharedChannel,
    GetAll,
    GetConversationPrefs,
    GetInfo,
    GetList,
    GetTeamsList,
    InvalidateSession,
    InviteUserToChannel,
    InviteUserToWorkspace,
    List,
    List0,
    List1,
    List2,
    ListAll,
    ListChannelsGet,
    ListEnterpriseEmoji,
    ListGroups,
    ListOriginalConnectedChannelInfo,
    ListOwners,
    ListPendingWorkspaceInviteRequests,
    ListWorkspaceUsers,
    RemoveChannels,
    RemoveEnterpriseEmoji,
    RemoveIdpGroup,
    RemoveUserFromWorkspace,
    RenameChannel,
    RenameEmoji,
    ResetSessions,
    RestrictApp,
    SearchChannels,
    SetAdminUser,
    SetConversationPrefs,
    SetDefaultChannels,
    SetDescription,
    SetDiscoverabilityOfWorkspace,
    SetExpirationGuest,
    SetIcon,
    SetName,
    SetRegularUser,
    SetTeamsWorkspaceConnection,
    SetWorkspaceOwner,
    UnarchiveChannel,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AdminApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AdminApiRaw(api_client)
