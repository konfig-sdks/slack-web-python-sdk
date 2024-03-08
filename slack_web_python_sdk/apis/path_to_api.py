import typing_extensions

from slack_web_python_sdk.paths import PathValues
from slack_web_python_sdk.apis.paths.admin_apps_approve import AdminAppsApprove
from slack_web_python_sdk.apis.paths.admin_apps_approved_list import AdminAppsApprovedList
from slack_web_python_sdk.apis.paths.admin_apps_requests_list import AdminAppsRequestsList
from slack_web_python_sdk.apis.paths.admin_apps_restrict import AdminAppsRestrict
from slack_web_python_sdk.apis.paths.admin_apps_restricted_list import AdminAppsRestrictedList
from slack_web_python_sdk.apis.paths.admin_conversations_archive import AdminConversationsArchive
from slack_web_python_sdk.apis.paths.admin_conversations_convert_to_private import AdminConversationsConvertToPrivate
from slack_web_python_sdk.apis.paths.admin_conversations_create import AdminConversationsCreate
from slack_web_python_sdk.apis.paths.admin_conversations_delete import AdminConversationsDelete
from slack_web_python_sdk.apis.paths.admin_conversations_disconnect_shared import AdminConversationsDisconnectShared
from slack_web_python_sdk.apis.paths.admin_conversations_ekm_list_original_connected_channel_info import AdminConversationsEkmListOriginalConnectedChannelInfo
from slack_web_python_sdk.apis.paths.admin_conversations_get_conversation_prefs import AdminConversationsGetConversationPrefs
from slack_web_python_sdk.apis.paths.admin_conversations_get_teams import AdminConversationsGetTeams
from slack_web_python_sdk.apis.paths.admin_conversations_invite import AdminConversationsInvite
from slack_web_python_sdk.apis.paths.admin_conversations_rename import AdminConversationsRename
from slack_web_python_sdk.apis.paths.admin_conversations_restrict_access_add_group import AdminConversationsRestrictAccessAddGroup
from slack_web_python_sdk.apis.paths.admin_conversations_restrict_access_list_groups import AdminConversationsRestrictAccessListGroups
from slack_web_python_sdk.apis.paths.admin_conversations_restrict_access_remove_group import AdminConversationsRestrictAccessRemoveGroup
from slack_web_python_sdk.apis.paths.admin_conversations_search import AdminConversationsSearch
from slack_web_python_sdk.apis.paths.admin_conversations_set_conversation_prefs import AdminConversationsSetConversationPrefs
from slack_web_python_sdk.apis.paths.admin_conversations_set_teams import AdminConversationsSetTeams
from slack_web_python_sdk.apis.paths.admin_conversations_unarchive import AdminConversationsUnarchive
from slack_web_python_sdk.apis.paths.admin_emoji_add import AdminEmojiAdd
from slack_web_python_sdk.apis.paths.admin_emoji_add_alias import AdminEmojiAddAlias
from slack_web_python_sdk.apis.paths.admin_emoji_list import AdminEmojiList
from slack_web_python_sdk.apis.paths.admin_emoji_remove import AdminEmojiRemove
from slack_web_python_sdk.apis.paths.admin_emoji_rename import AdminEmojiRename
from slack_web_python_sdk.apis.paths.admin_invite_requests_approve import AdminInviteRequestsApprove
from slack_web_python_sdk.apis.paths.admin_invite_requests_approved_list import AdminInviteRequestsApprovedList
from slack_web_python_sdk.apis.paths.admin_invite_requests_denied_list import AdminInviteRequestsDeniedList
from slack_web_python_sdk.apis.paths.admin_invite_requests_deny import AdminInviteRequestsDeny
from slack_web_python_sdk.apis.paths.admin_invite_requests_list import AdminInviteRequestsList
from slack_web_python_sdk.apis.paths.admin_teams_admins_list import AdminTeamsAdminsList
from slack_web_python_sdk.apis.paths.admin_teams_create import AdminTeamsCreate
from slack_web_python_sdk.apis.paths.admin_teams_list import AdminTeamsList
from slack_web_python_sdk.apis.paths.admin_teams_owners_list import AdminTeamsOwnersList
from slack_web_python_sdk.apis.paths.admin_teams_settings_info import AdminTeamsSettingsInfo
from slack_web_python_sdk.apis.paths.admin_teams_settings_set_default_channels import AdminTeamsSettingsSetDefaultChannels
from slack_web_python_sdk.apis.paths.admin_teams_settings_set_description import AdminTeamsSettingsSetDescription
from slack_web_python_sdk.apis.paths.admin_teams_settings_set_discoverability import AdminTeamsSettingsSetDiscoverability
from slack_web_python_sdk.apis.paths.admin_teams_settings_set_icon import AdminTeamsSettingsSetIcon
from slack_web_python_sdk.apis.paths.admin_teams_settings_set_name import AdminTeamsSettingsSetName
from slack_web_python_sdk.apis.paths.admin_usergroups_add_channels import AdminUsergroupsAddChannels
from slack_web_python_sdk.apis.paths.admin_usergroups_add_teams import AdminUsergroupsAddTeams
from slack_web_python_sdk.apis.paths.admin_usergroups_list_channels import AdminUsergroupsListChannels
from slack_web_python_sdk.apis.paths.admin_usergroups_remove_channels import AdminUsergroupsRemoveChannels
from slack_web_python_sdk.apis.paths.admin_users_assign import AdminUsersAssign
from slack_web_python_sdk.apis.paths.admin_users_invite import AdminUsersInvite
from slack_web_python_sdk.apis.paths.admin_users_list import AdminUsersList
from slack_web_python_sdk.apis.paths.admin_users_remove import AdminUsersRemove
from slack_web_python_sdk.apis.paths.admin_users_session_invalidate import AdminUsersSessionInvalidate
from slack_web_python_sdk.apis.paths.admin_users_session_reset import AdminUsersSessionReset
from slack_web_python_sdk.apis.paths.admin_users_set_admin import AdminUsersSetAdmin
from slack_web_python_sdk.apis.paths.admin_users_set_expiration import AdminUsersSetExpiration
from slack_web_python_sdk.apis.paths.admin_users_set_owner import AdminUsersSetOwner
from slack_web_python_sdk.apis.paths.admin_users_set_regular import AdminUsersSetRegular
from slack_web_python_sdk.apis.paths.api_test import ApiTest
from slack_web_python_sdk.apis.paths.apps_event_authorizations_list import AppsEventAuthorizationsList
from slack_web_python_sdk.apis.paths.apps_permissions_info import AppsPermissionsInfo
from slack_web_python_sdk.apis.paths.apps_permissions_request import AppsPermissionsRequest
from slack_web_python_sdk.apis.paths.apps_permissions_resources_list import AppsPermissionsResourcesList
from slack_web_python_sdk.apis.paths.apps_permissions_scopes_list import AppsPermissionsScopesList
from slack_web_python_sdk.apis.paths.apps_permissions_users_list import AppsPermissionsUsersList
from slack_web_python_sdk.apis.paths.apps_permissions_users_request import AppsPermissionsUsersRequest
from slack_web_python_sdk.apis.paths.apps_uninstall import AppsUninstall
from slack_web_python_sdk.apis.paths.auth_revoke import AuthRevoke
from slack_web_python_sdk.apis.paths.auth_test import AuthTest
from slack_web_python_sdk.apis.paths.bots_info import BotsInfo
from slack_web_python_sdk.apis.paths.calls_add import CallsAdd
from slack_web_python_sdk.apis.paths.calls_end import CallsEnd
from slack_web_python_sdk.apis.paths.calls_info import CallsInfo
from slack_web_python_sdk.apis.paths.calls_participants_add import CallsParticipantsAdd
from slack_web_python_sdk.apis.paths.calls_participants_remove import CallsParticipantsRemove
from slack_web_python_sdk.apis.paths.calls_update import CallsUpdate
from slack_web_python_sdk.apis.paths.chat_delete import ChatDelete
from slack_web_python_sdk.apis.paths.chat_delete_scheduled_message import ChatDeleteScheduledMessage
from slack_web_python_sdk.apis.paths.chat_get_permalink import ChatGetPermalink
from slack_web_python_sdk.apis.paths.chat_me_message import ChatMeMessage
from slack_web_python_sdk.apis.paths.chat_post_ephemeral import ChatPostEphemeral
from slack_web_python_sdk.apis.paths.chat_post_message import ChatPostMessage
from slack_web_python_sdk.apis.paths.chat_schedule_message import ChatScheduleMessage
from slack_web_python_sdk.apis.paths.chat_scheduled_messages_list import ChatScheduledMessagesList
from slack_web_python_sdk.apis.paths.chat_unfurl import ChatUnfurl
from slack_web_python_sdk.apis.paths.chat_update import ChatUpdate
from slack_web_python_sdk.apis.paths.conversations_archive import ConversationsArchive
from slack_web_python_sdk.apis.paths.conversations_close import ConversationsClose
from slack_web_python_sdk.apis.paths.conversations_create import ConversationsCreate
from slack_web_python_sdk.apis.paths.conversations_history import ConversationsHistory
from slack_web_python_sdk.apis.paths.conversations_info import ConversationsInfo
from slack_web_python_sdk.apis.paths.conversations_invite import ConversationsInvite
from slack_web_python_sdk.apis.paths.conversations_join import ConversationsJoin
from slack_web_python_sdk.apis.paths.conversations_kick import ConversationsKick
from slack_web_python_sdk.apis.paths.conversations_leave import ConversationsLeave
from slack_web_python_sdk.apis.paths.conversations_list import ConversationsList
from slack_web_python_sdk.apis.paths.conversations_mark import ConversationsMark
from slack_web_python_sdk.apis.paths.conversations_members import ConversationsMembers
from slack_web_python_sdk.apis.paths.conversations_open import ConversationsOpen
from slack_web_python_sdk.apis.paths.conversations_rename import ConversationsRename
from slack_web_python_sdk.apis.paths.conversations_replies import ConversationsReplies
from slack_web_python_sdk.apis.paths.conversations_set_purpose import ConversationsSetPurpose
from slack_web_python_sdk.apis.paths.conversations_set_topic import ConversationsSetTopic
from slack_web_python_sdk.apis.paths.conversations_unarchive import ConversationsUnarchive
from slack_web_python_sdk.apis.paths.dialog_open import DialogOpen
from slack_web_python_sdk.apis.paths.dnd_end_dnd import DndEndDnd
from slack_web_python_sdk.apis.paths.dnd_end_snooze import DndEndSnooze
from slack_web_python_sdk.apis.paths.dnd_info import DndInfo
from slack_web_python_sdk.apis.paths.dnd_set_snooze import DndSetSnooze
from slack_web_python_sdk.apis.paths.dnd_team_info import DndTeamInfo
from slack_web_python_sdk.apis.paths.emoji_list import EmojiList
from slack_web_python_sdk.apis.paths.files_comments_delete import FilesCommentsDelete
from slack_web_python_sdk.apis.paths.files_delete import FilesDelete
from slack_web_python_sdk.apis.paths.files_info import FilesInfo
from slack_web_python_sdk.apis.paths.files_list import FilesList
from slack_web_python_sdk.apis.paths.files_remote_add import FilesRemoteAdd
from slack_web_python_sdk.apis.paths.files_remote_info import FilesRemoteInfo
from slack_web_python_sdk.apis.paths.files_remote_list import FilesRemoteList
from slack_web_python_sdk.apis.paths.files_remote_remove import FilesRemoteRemove
from slack_web_python_sdk.apis.paths.files_remote_share import FilesRemoteShare
from slack_web_python_sdk.apis.paths.files_remote_update import FilesRemoteUpdate
from slack_web_python_sdk.apis.paths.files_revoke_public_url import FilesRevokePublicURL
from slack_web_python_sdk.apis.paths.files_shared_public_url import FilesSharedPublicURL
from slack_web_python_sdk.apis.paths.files_upload import FilesUpload
from slack_web_python_sdk.apis.paths.migration_exchange import MigrationExchange
from slack_web_python_sdk.apis.paths.oauth_access import OauthAccess
from slack_web_python_sdk.apis.paths.oauth_token import OauthToken
from slack_web_python_sdk.apis.paths.oauth_v2_access import OauthV2Access
from slack_web_python_sdk.apis.paths.pins_add import PinsAdd
from slack_web_python_sdk.apis.paths.pins_list import PinsList
from slack_web_python_sdk.apis.paths.pins_remove import PinsRemove
from slack_web_python_sdk.apis.paths.reactions_add import ReactionsAdd
from slack_web_python_sdk.apis.paths.reactions_get import ReactionsGet
from slack_web_python_sdk.apis.paths.reactions_list import ReactionsList
from slack_web_python_sdk.apis.paths.reactions_remove import ReactionsRemove
from slack_web_python_sdk.apis.paths.reminders_add import RemindersAdd
from slack_web_python_sdk.apis.paths.reminders_complete import RemindersComplete
from slack_web_python_sdk.apis.paths.reminders_delete import RemindersDelete
from slack_web_python_sdk.apis.paths.reminders_info import RemindersInfo
from slack_web_python_sdk.apis.paths.reminders_list import RemindersList
from slack_web_python_sdk.apis.paths.rtm_connect import RtmConnect
from slack_web_python_sdk.apis.paths.search_messages import SearchMessages
from slack_web_python_sdk.apis.paths.stars_add import StarsAdd
from slack_web_python_sdk.apis.paths.stars_list import StarsList
from slack_web_python_sdk.apis.paths.stars_remove import StarsRemove
from slack_web_python_sdk.apis.paths.team_access_logs import TeamAccessLogs
from slack_web_python_sdk.apis.paths.team_billable_info import TeamBillableInfo
from slack_web_python_sdk.apis.paths.team_info import TeamInfo
from slack_web_python_sdk.apis.paths.team_integration_logs import TeamIntegrationLogs
from slack_web_python_sdk.apis.paths.team_profile_get import TeamProfileGet
from slack_web_python_sdk.apis.paths.usergroups_create import UsergroupsCreate
from slack_web_python_sdk.apis.paths.usergroups_disable import UsergroupsDisable
from slack_web_python_sdk.apis.paths.usergroups_enable import UsergroupsEnable
from slack_web_python_sdk.apis.paths.usergroups_list import UsergroupsList
from slack_web_python_sdk.apis.paths.usergroups_update import UsergroupsUpdate
from slack_web_python_sdk.apis.paths.usergroups_users_list import UsergroupsUsersList
from slack_web_python_sdk.apis.paths.usergroups_users_update import UsergroupsUsersUpdate
from slack_web_python_sdk.apis.paths.users_conversations import UsersConversations
from slack_web_python_sdk.apis.paths.users_delete_photo import UsersDeletePhoto
from slack_web_python_sdk.apis.paths.users_get_presence import UsersGetPresence
from slack_web_python_sdk.apis.paths.users_identity import UsersIdentity
from slack_web_python_sdk.apis.paths.users_info import UsersInfo
from slack_web_python_sdk.apis.paths.users_list import UsersList
from slack_web_python_sdk.apis.paths.users_lookup_by_email import UsersLookupByEmail
from slack_web_python_sdk.apis.paths.users_profile_get import UsersProfileGet
from slack_web_python_sdk.apis.paths.users_profile_set import UsersProfileSet
from slack_web_python_sdk.apis.paths.users_set_active import UsersSetActive
from slack_web_python_sdk.apis.paths.users_set_photo import UsersSetPhoto
from slack_web_python_sdk.apis.paths.users_set_presence import UsersSetPresence
from slack_web_python_sdk.apis.paths.views_open import ViewsOpen
from slack_web_python_sdk.apis.paths.views_publish import ViewsPublish
from slack_web_python_sdk.apis.paths.views_push import ViewsPush
from slack_web_python_sdk.apis.paths.views_update import ViewsUpdate
from slack_web_python_sdk.apis.paths.workflows_step_completed import WorkflowsStepCompleted
from slack_web_python_sdk.apis.paths.workflows_step_failed import WorkflowsStepFailed
from slack_web_python_sdk.apis.paths.workflows_update_step import WorkflowsUpdateStep

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ADMIN_APPS_APPROVE: AdminAppsApprove,
        PathValues.ADMIN_APPS_APPROVED_LIST: AdminAppsApprovedList,
        PathValues.ADMIN_APPS_REQUESTS_LIST: AdminAppsRequestsList,
        PathValues.ADMIN_APPS_RESTRICT: AdminAppsRestrict,
        PathValues.ADMIN_APPS_RESTRICTED_LIST: AdminAppsRestrictedList,
        PathValues.ADMIN_CONVERSATIONS_ARCHIVE: AdminConversationsArchive,
        PathValues.ADMIN_CONVERSATIONS_CONVERT_TO_PRIVATE: AdminConversationsConvertToPrivate,
        PathValues.ADMIN_CONVERSATIONS_CREATE: AdminConversationsCreate,
        PathValues.ADMIN_CONVERSATIONS_DELETE: AdminConversationsDelete,
        PathValues.ADMIN_CONVERSATIONS_DISCONNECT_SHARED: AdminConversationsDisconnectShared,
        PathValues.ADMIN_CONVERSATIONS_EKM_LIST_ORIGINAL_CONNECTED_CHANNEL_INFO: AdminConversationsEkmListOriginalConnectedChannelInfo,
        PathValues.ADMIN_CONVERSATIONS_GET_CONVERSATION_PREFS: AdminConversationsGetConversationPrefs,
        PathValues.ADMIN_CONVERSATIONS_GET_TEAMS: AdminConversationsGetTeams,
        PathValues.ADMIN_CONVERSATIONS_INVITE: AdminConversationsInvite,
        PathValues.ADMIN_CONVERSATIONS_RENAME: AdminConversationsRename,
        PathValues.ADMIN_CONVERSATIONS_RESTRICT_ACCESS_ADD_GROUP: AdminConversationsRestrictAccessAddGroup,
        PathValues.ADMIN_CONVERSATIONS_RESTRICT_ACCESS_LIST_GROUPS: AdminConversationsRestrictAccessListGroups,
        PathValues.ADMIN_CONVERSATIONS_RESTRICT_ACCESS_REMOVE_GROUP: AdminConversationsRestrictAccessRemoveGroup,
        PathValues.ADMIN_CONVERSATIONS_SEARCH: AdminConversationsSearch,
        PathValues.ADMIN_CONVERSATIONS_SET_CONVERSATION_PREFS: AdminConversationsSetConversationPrefs,
        PathValues.ADMIN_CONVERSATIONS_SET_TEAMS: AdminConversationsSetTeams,
        PathValues.ADMIN_CONVERSATIONS_UNARCHIVE: AdminConversationsUnarchive,
        PathValues.ADMIN_EMOJI_ADD: AdminEmojiAdd,
        PathValues.ADMIN_EMOJI_ADD_ALIAS: AdminEmojiAddAlias,
        PathValues.ADMIN_EMOJI_LIST: AdminEmojiList,
        PathValues.ADMIN_EMOJI_REMOVE: AdminEmojiRemove,
        PathValues.ADMIN_EMOJI_RENAME: AdminEmojiRename,
        PathValues.ADMIN_INVITE_REQUESTS_APPROVE: AdminInviteRequestsApprove,
        PathValues.ADMIN_INVITE_REQUESTS_APPROVED_LIST: AdminInviteRequestsApprovedList,
        PathValues.ADMIN_INVITE_REQUESTS_DENIED_LIST: AdminInviteRequestsDeniedList,
        PathValues.ADMIN_INVITE_REQUESTS_DENY: AdminInviteRequestsDeny,
        PathValues.ADMIN_INVITE_REQUESTS_LIST: AdminInviteRequestsList,
        PathValues.ADMIN_TEAMS_ADMINS_LIST: AdminTeamsAdminsList,
        PathValues.ADMIN_TEAMS_CREATE: AdminTeamsCreate,
        PathValues.ADMIN_TEAMS_LIST: AdminTeamsList,
        PathValues.ADMIN_TEAMS_OWNERS_LIST: AdminTeamsOwnersList,
        PathValues.ADMIN_TEAMS_SETTINGS_INFO: AdminTeamsSettingsInfo,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_DEFAULT_CHANNELS: AdminTeamsSettingsSetDefaultChannels,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_DESCRIPTION: AdminTeamsSettingsSetDescription,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_DISCOVERABILITY: AdminTeamsSettingsSetDiscoverability,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_ICON: AdminTeamsSettingsSetIcon,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_NAME: AdminTeamsSettingsSetName,
        PathValues.ADMIN_USERGROUPS_ADD_CHANNELS: AdminUsergroupsAddChannels,
        PathValues.ADMIN_USERGROUPS_ADD_TEAMS: AdminUsergroupsAddTeams,
        PathValues.ADMIN_USERGROUPS_LIST_CHANNELS: AdminUsergroupsListChannels,
        PathValues.ADMIN_USERGROUPS_REMOVE_CHANNELS: AdminUsergroupsRemoveChannels,
        PathValues.ADMIN_USERS_ASSIGN: AdminUsersAssign,
        PathValues.ADMIN_USERS_INVITE: AdminUsersInvite,
        PathValues.ADMIN_USERS_LIST: AdminUsersList,
        PathValues.ADMIN_USERS_REMOVE: AdminUsersRemove,
        PathValues.ADMIN_USERS_SESSION_INVALIDATE: AdminUsersSessionInvalidate,
        PathValues.ADMIN_USERS_SESSION_RESET: AdminUsersSessionReset,
        PathValues.ADMIN_USERS_SET_ADMIN: AdminUsersSetAdmin,
        PathValues.ADMIN_USERS_SET_EXPIRATION: AdminUsersSetExpiration,
        PathValues.ADMIN_USERS_SET_OWNER: AdminUsersSetOwner,
        PathValues.ADMIN_USERS_SET_REGULAR: AdminUsersSetRegular,
        PathValues.API_TEST: ApiTest,
        PathValues.APPS_EVENT_AUTHORIZATIONS_LIST: AppsEventAuthorizationsList,
        PathValues.APPS_PERMISSIONS_INFO: AppsPermissionsInfo,
        PathValues.APPS_PERMISSIONS_REQUEST: AppsPermissionsRequest,
        PathValues.APPS_PERMISSIONS_RESOURCES_LIST: AppsPermissionsResourcesList,
        PathValues.APPS_PERMISSIONS_SCOPES_LIST: AppsPermissionsScopesList,
        PathValues.APPS_PERMISSIONS_USERS_LIST: AppsPermissionsUsersList,
        PathValues.APPS_PERMISSIONS_USERS_REQUEST: AppsPermissionsUsersRequest,
        PathValues.APPS_UNINSTALL: AppsUninstall,
        PathValues.AUTH_REVOKE: AuthRevoke,
        PathValues.AUTH_TEST: AuthTest,
        PathValues.BOTS_INFO: BotsInfo,
        PathValues.CALLS_ADD: CallsAdd,
        PathValues.CALLS_END: CallsEnd,
        PathValues.CALLS_INFO: CallsInfo,
        PathValues.CALLS_PARTICIPANTS_ADD: CallsParticipantsAdd,
        PathValues.CALLS_PARTICIPANTS_REMOVE: CallsParticipantsRemove,
        PathValues.CALLS_UPDATE: CallsUpdate,
        PathValues.CHAT_DELETE: ChatDelete,
        PathValues.CHAT_DELETE_SCHEDULED_MESSAGE: ChatDeleteScheduledMessage,
        PathValues.CHAT_GET_PERMALINK: ChatGetPermalink,
        PathValues.CHAT_ME_MESSAGE: ChatMeMessage,
        PathValues.CHAT_POST_EPHEMERAL: ChatPostEphemeral,
        PathValues.CHAT_POST_MESSAGE: ChatPostMessage,
        PathValues.CHAT_SCHEDULE_MESSAGE: ChatScheduleMessage,
        PathValues.CHAT_SCHEDULED_MESSAGES_LIST: ChatScheduledMessagesList,
        PathValues.CHAT_UNFURL: ChatUnfurl,
        PathValues.CHAT_UPDATE: ChatUpdate,
        PathValues.CONVERSATIONS_ARCHIVE: ConversationsArchive,
        PathValues.CONVERSATIONS_CLOSE: ConversationsClose,
        PathValues.CONVERSATIONS_CREATE: ConversationsCreate,
        PathValues.CONVERSATIONS_HISTORY: ConversationsHistory,
        PathValues.CONVERSATIONS_INFO: ConversationsInfo,
        PathValues.CONVERSATIONS_INVITE: ConversationsInvite,
        PathValues.CONVERSATIONS_JOIN: ConversationsJoin,
        PathValues.CONVERSATIONS_KICK: ConversationsKick,
        PathValues.CONVERSATIONS_LEAVE: ConversationsLeave,
        PathValues.CONVERSATIONS_LIST: ConversationsList,
        PathValues.CONVERSATIONS_MARK: ConversationsMark,
        PathValues.CONVERSATIONS_MEMBERS: ConversationsMembers,
        PathValues.CONVERSATIONS_OPEN: ConversationsOpen,
        PathValues.CONVERSATIONS_RENAME: ConversationsRename,
        PathValues.CONVERSATIONS_REPLIES: ConversationsReplies,
        PathValues.CONVERSATIONS_SET_PURPOSE: ConversationsSetPurpose,
        PathValues.CONVERSATIONS_SET_TOPIC: ConversationsSetTopic,
        PathValues.CONVERSATIONS_UNARCHIVE: ConversationsUnarchive,
        PathValues.DIALOG_OPEN: DialogOpen,
        PathValues.DND_END_DND: DndEndDnd,
        PathValues.DND_END_SNOOZE: DndEndSnooze,
        PathValues.DND_INFO: DndInfo,
        PathValues.DND_SET_SNOOZE: DndSetSnooze,
        PathValues.DND_TEAM_INFO: DndTeamInfo,
        PathValues.EMOJI_LIST: EmojiList,
        PathValues.FILES_COMMENTS_DELETE: FilesCommentsDelete,
        PathValues.FILES_DELETE: FilesDelete,
        PathValues.FILES_INFO: FilesInfo,
        PathValues.FILES_LIST: FilesList,
        PathValues.FILES_REMOTE_ADD: FilesRemoteAdd,
        PathValues.FILES_REMOTE_INFO: FilesRemoteInfo,
        PathValues.FILES_REMOTE_LIST: FilesRemoteList,
        PathValues.FILES_REMOTE_REMOVE: FilesRemoteRemove,
        PathValues.FILES_REMOTE_SHARE: FilesRemoteShare,
        PathValues.FILES_REMOTE_UPDATE: FilesRemoteUpdate,
        PathValues.FILES_REVOKE_PUBLIC_URL: FilesRevokePublicURL,
        PathValues.FILES_SHARED_PUBLIC_URL: FilesSharedPublicURL,
        PathValues.FILES_UPLOAD: FilesUpload,
        PathValues.MIGRATION_EXCHANGE: MigrationExchange,
        PathValues.OAUTH_ACCESS: OauthAccess,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.OAUTH_V2_ACCESS: OauthV2Access,
        PathValues.PINS_ADD: PinsAdd,
        PathValues.PINS_LIST: PinsList,
        PathValues.PINS_REMOVE: PinsRemove,
        PathValues.REACTIONS_ADD: ReactionsAdd,
        PathValues.REACTIONS_GET: ReactionsGet,
        PathValues.REACTIONS_LIST: ReactionsList,
        PathValues.REACTIONS_REMOVE: ReactionsRemove,
        PathValues.REMINDERS_ADD: RemindersAdd,
        PathValues.REMINDERS_COMPLETE: RemindersComplete,
        PathValues.REMINDERS_DELETE: RemindersDelete,
        PathValues.REMINDERS_INFO: RemindersInfo,
        PathValues.REMINDERS_LIST: RemindersList,
        PathValues.RTM_CONNECT: RtmConnect,
        PathValues.SEARCH_MESSAGES: SearchMessages,
        PathValues.STARS_ADD: StarsAdd,
        PathValues.STARS_LIST: StarsList,
        PathValues.STARS_REMOVE: StarsRemove,
        PathValues.TEAM_ACCESS_LOGS: TeamAccessLogs,
        PathValues.TEAM_BILLABLE_INFO: TeamBillableInfo,
        PathValues.TEAM_INFO: TeamInfo,
        PathValues.TEAM_INTEGRATION_LOGS: TeamIntegrationLogs,
        PathValues.TEAM_PROFILE_GET: TeamProfileGet,
        PathValues.USERGROUPS_CREATE: UsergroupsCreate,
        PathValues.USERGROUPS_DISABLE: UsergroupsDisable,
        PathValues.USERGROUPS_ENABLE: UsergroupsEnable,
        PathValues.USERGROUPS_LIST: UsergroupsList,
        PathValues.USERGROUPS_UPDATE: UsergroupsUpdate,
        PathValues.USERGROUPS_USERS_LIST: UsergroupsUsersList,
        PathValues.USERGROUPS_USERS_UPDATE: UsergroupsUsersUpdate,
        PathValues.USERS_CONVERSATIONS: UsersConversations,
        PathValues.USERS_DELETE_PHOTO: UsersDeletePhoto,
        PathValues.USERS_GET_PRESENCE: UsersGetPresence,
        PathValues.USERS_IDENTITY: UsersIdentity,
        PathValues.USERS_INFO: UsersInfo,
        PathValues.USERS_LIST: UsersList,
        PathValues.USERS_LOOKUP_BY_EMAIL: UsersLookupByEmail,
        PathValues.USERS_PROFILE_GET: UsersProfileGet,
        PathValues.USERS_PROFILE_SET: UsersProfileSet,
        PathValues.USERS_SET_ACTIVE: UsersSetActive,
        PathValues.USERS_SET_PHOTO: UsersSetPhoto,
        PathValues.USERS_SET_PRESENCE: UsersSetPresence,
        PathValues.VIEWS_OPEN: ViewsOpen,
        PathValues.VIEWS_PUBLISH: ViewsPublish,
        PathValues.VIEWS_PUSH: ViewsPush,
        PathValues.VIEWS_UPDATE: ViewsUpdate,
        PathValues.WORKFLOWS_STEP_COMPLETED: WorkflowsStepCompleted,
        PathValues.WORKFLOWS_STEP_FAILED: WorkflowsStepFailed,
        PathValues.WORKFLOWS_UPDATE_STEP: WorkflowsUpdateStep,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ADMIN_APPS_APPROVE: AdminAppsApprove,
        PathValues.ADMIN_APPS_APPROVED_LIST: AdminAppsApprovedList,
        PathValues.ADMIN_APPS_REQUESTS_LIST: AdminAppsRequestsList,
        PathValues.ADMIN_APPS_RESTRICT: AdminAppsRestrict,
        PathValues.ADMIN_APPS_RESTRICTED_LIST: AdminAppsRestrictedList,
        PathValues.ADMIN_CONVERSATIONS_ARCHIVE: AdminConversationsArchive,
        PathValues.ADMIN_CONVERSATIONS_CONVERT_TO_PRIVATE: AdminConversationsConvertToPrivate,
        PathValues.ADMIN_CONVERSATIONS_CREATE: AdminConversationsCreate,
        PathValues.ADMIN_CONVERSATIONS_DELETE: AdminConversationsDelete,
        PathValues.ADMIN_CONVERSATIONS_DISCONNECT_SHARED: AdminConversationsDisconnectShared,
        PathValues.ADMIN_CONVERSATIONS_EKM_LIST_ORIGINAL_CONNECTED_CHANNEL_INFO: AdminConversationsEkmListOriginalConnectedChannelInfo,
        PathValues.ADMIN_CONVERSATIONS_GET_CONVERSATION_PREFS: AdminConversationsGetConversationPrefs,
        PathValues.ADMIN_CONVERSATIONS_GET_TEAMS: AdminConversationsGetTeams,
        PathValues.ADMIN_CONVERSATIONS_INVITE: AdminConversationsInvite,
        PathValues.ADMIN_CONVERSATIONS_RENAME: AdminConversationsRename,
        PathValues.ADMIN_CONVERSATIONS_RESTRICT_ACCESS_ADD_GROUP: AdminConversationsRestrictAccessAddGroup,
        PathValues.ADMIN_CONVERSATIONS_RESTRICT_ACCESS_LIST_GROUPS: AdminConversationsRestrictAccessListGroups,
        PathValues.ADMIN_CONVERSATIONS_RESTRICT_ACCESS_REMOVE_GROUP: AdminConversationsRestrictAccessRemoveGroup,
        PathValues.ADMIN_CONVERSATIONS_SEARCH: AdminConversationsSearch,
        PathValues.ADMIN_CONVERSATIONS_SET_CONVERSATION_PREFS: AdminConversationsSetConversationPrefs,
        PathValues.ADMIN_CONVERSATIONS_SET_TEAMS: AdminConversationsSetTeams,
        PathValues.ADMIN_CONVERSATIONS_UNARCHIVE: AdminConversationsUnarchive,
        PathValues.ADMIN_EMOJI_ADD: AdminEmojiAdd,
        PathValues.ADMIN_EMOJI_ADD_ALIAS: AdminEmojiAddAlias,
        PathValues.ADMIN_EMOJI_LIST: AdminEmojiList,
        PathValues.ADMIN_EMOJI_REMOVE: AdminEmojiRemove,
        PathValues.ADMIN_EMOJI_RENAME: AdminEmojiRename,
        PathValues.ADMIN_INVITE_REQUESTS_APPROVE: AdminInviteRequestsApprove,
        PathValues.ADMIN_INVITE_REQUESTS_APPROVED_LIST: AdminInviteRequestsApprovedList,
        PathValues.ADMIN_INVITE_REQUESTS_DENIED_LIST: AdminInviteRequestsDeniedList,
        PathValues.ADMIN_INVITE_REQUESTS_DENY: AdminInviteRequestsDeny,
        PathValues.ADMIN_INVITE_REQUESTS_LIST: AdminInviteRequestsList,
        PathValues.ADMIN_TEAMS_ADMINS_LIST: AdminTeamsAdminsList,
        PathValues.ADMIN_TEAMS_CREATE: AdminTeamsCreate,
        PathValues.ADMIN_TEAMS_LIST: AdminTeamsList,
        PathValues.ADMIN_TEAMS_OWNERS_LIST: AdminTeamsOwnersList,
        PathValues.ADMIN_TEAMS_SETTINGS_INFO: AdminTeamsSettingsInfo,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_DEFAULT_CHANNELS: AdminTeamsSettingsSetDefaultChannels,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_DESCRIPTION: AdminTeamsSettingsSetDescription,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_DISCOVERABILITY: AdminTeamsSettingsSetDiscoverability,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_ICON: AdminTeamsSettingsSetIcon,
        PathValues.ADMIN_TEAMS_SETTINGS_SET_NAME: AdminTeamsSettingsSetName,
        PathValues.ADMIN_USERGROUPS_ADD_CHANNELS: AdminUsergroupsAddChannels,
        PathValues.ADMIN_USERGROUPS_ADD_TEAMS: AdminUsergroupsAddTeams,
        PathValues.ADMIN_USERGROUPS_LIST_CHANNELS: AdminUsergroupsListChannels,
        PathValues.ADMIN_USERGROUPS_REMOVE_CHANNELS: AdminUsergroupsRemoveChannels,
        PathValues.ADMIN_USERS_ASSIGN: AdminUsersAssign,
        PathValues.ADMIN_USERS_INVITE: AdminUsersInvite,
        PathValues.ADMIN_USERS_LIST: AdminUsersList,
        PathValues.ADMIN_USERS_REMOVE: AdminUsersRemove,
        PathValues.ADMIN_USERS_SESSION_INVALIDATE: AdminUsersSessionInvalidate,
        PathValues.ADMIN_USERS_SESSION_RESET: AdminUsersSessionReset,
        PathValues.ADMIN_USERS_SET_ADMIN: AdminUsersSetAdmin,
        PathValues.ADMIN_USERS_SET_EXPIRATION: AdminUsersSetExpiration,
        PathValues.ADMIN_USERS_SET_OWNER: AdminUsersSetOwner,
        PathValues.ADMIN_USERS_SET_REGULAR: AdminUsersSetRegular,
        PathValues.API_TEST: ApiTest,
        PathValues.APPS_EVENT_AUTHORIZATIONS_LIST: AppsEventAuthorizationsList,
        PathValues.APPS_PERMISSIONS_INFO: AppsPermissionsInfo,
        PathValues.APPS_PERMISSIONS_REQUEST: AppsPermissionsRequest,
        PathValues.APPS_PERMISSIONS_RESOURCES_LIST: AppsPermissionsResourcesList,
        PathValues.APPS_PERMISSIONS_SCOPES_LIST: AppsPermissionsScopesList,
        PathValues.APPS_PERMISSIONS_USERS_LIST: AppsPermissionsUsersList,
        PathValues.APPS_PERMISSIONS_USERS_REQUEST: AppsPermissionsUsersRequest,
        PathValues.APPS_UNINSTALL: AppsUninstall,
        PathValues.AUTH_REVOKE: AuthRevoke,
        PathValues.AUTH_TEST: AuthTest,
        PathValues.BOTS_INFO: BotsInfo,
        PathValues.CALLS_ADD: CallsAdd,
        PathValues.CALLS_END: CallsEnd,
        PathValues.CALLS_INFO: CallsInfo,
        PathValues.CALLS_PARTICIPANTS_ADD: CallsParticipantsAdd,
        PathValues.CALLS_PARTICIPANTS_REMOVE: CallsParticipantsRemove,
        PathValues.CALLS_UPDATE: CallsUpdate,
        PathValues.CHAT_DELETE: ChatDelete,
        PathValues.CHAT_DELETE_SCHEDULED_MESSAGE: ChatDeleteScheduledMessage,
        PathValues.CHAT_GET_PERMALINK: ChatGetPermalink,
        PathValues.CHAT_ME_MESSAGE: ChatMeMessage,
        PathValues.CHAT_POST_EPHEMERAL: ChatPostEphemeral,
        PathValues.CHAT_POST_MESSAGE: ChatPostMessage,
        PathValues.CHAT_SCHEDULE_MESSAGE: ChatScheduleMessage,
        PathValues.CHAT_SCHEDULED_MESSAGES_LIST: ChatScheduledMessagesList,
        PathValues.CHAT_UNFURL: ChatUnfurl,
        PathValues.CHAT_UPDATE: ChatUpdate,
        PathValues.CONVERSATIONS_ARCHIVE: ConversationsArchive,
        PathValues.CONVERSATIONS_CLOSE: ConversationsClose,
        PathValues.CONVERSATIONS_CREATE: ConversationsCreate,
        PathValues.CONVERSATIONS_HISTORY: ConversationsHistory,
        PathValues.CONVERSATIONS_INFO: ConversationsInfo,
        PathValues.CONVERSATIONS_INVITE: ConversationsInvite,
        PathValues.CONVERSATIONS_JOIN: ConversationsJoin,
        PathValues.CONVERSATIONS_KICK: ConversationsKick,
        PathValues.CONVERSATIONS_LEAVE: ConversationsLeave,
        PathValues.CONVERSATIONS_LIST: ConversationsList,
        PathValues.CONVERSATIONS_MARK: ConversationsMark,
        PathValues.CONVERSATIONS_MEMBERS: ConversationsMembers,
        PathValues.CONVERSATIONS_OPEN: ConversationsOpen,
        PathValues.CONVERSATIONS_RENAME: ConversationsRename,
        PathValues.CONVERSATIONS_REPLIES: ConversationsReplies,
        PathValues.CONVERSATIONS_SET_PURPOSE: ConversationsSetPurpose,
        PathValues.CONVERSATIONS_SET_TOPIC: ConversationsSetTopic,
        PathValues.CONVERSATIONS_UNARCHIVE: ConversationsUnarchive,
        PathValues.DIALOG_OPEN: DialogOpen,
        PathValues.DND_END_DND: DndEndDnd,
        PathValues.DND_END_SNOOZE: DndEndSnooze,
        PathValues.DND_INFO: DndInfo,
        PathValues.DND_SET_SNOOZE: DndSetSnooze,
        PathValues.DND_TEAM_INFO: DndTeamInfo,
        PathValues.EMOJI_LIST: EmojiList,
        PathValues.FILES_COMMENTS_DELETE: FilesCommentsDelete,
        PathValues.FILES_DELETE: FilesDelete,
        PathValues.FILES_INFO: FilesInfo,
        PathValues.FILES_LIST: FilesList,
        PathValues.FILES_REMOTE_ADD: FilesRemoteAdd,
        PathValues.FILES_REMOTE_INFO: FilesRemoteInfo,
        PathValues.FILES_REMOTE_LIST: FilesRemoteList,
        PathValues.FILES_REMOTE_REMOVE: FilesRemoteRemove,
        PathValues.FILES_REMOTE_SHARE: FilesRemoteShare,
        PathValues.FILES_REMOTE_UPDATE: FilesRemoteUpdate,
        PathValues.FILES_REVOKE_PUBLIC_URL: FilesRevokePublicURL,
        PathValues.FILES_SHARED_PUBLIC_URL: FilesSharedPublicURL,
        PathValues.FILES_UPLOAD: FilesUpload,
        PathValues.MIGRATION_EXCHANGE: MigrationExchange,
        PathValues.OAUTH_ACCESS: OauthAccess,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.OAUTH_V2_ACCESS: OauthV2Access,
        PathValues.PINS_ADD: PinsAdd,
        PathValues.PINS_LIST: PinsList,
        PathValues.PINS_REMOVE: PinsRemove,
        PathValues.REACTIONS_ADD: ReactionsAdd,
        PathValues.REACTIONS_GET: ReactionsGet,
        PathValues.REACTIONS_LIST: ReactionsList,
        PathValues.REACTIONS_REMOVE: ReactionsRemove,
        PathValues.REMINDERS_ADD: RemindersAdd,
        PathValues.REMINDERS_COMPLETE: RemindersComplete,
        PathValues.REMINDERS_DELETE: RemindersDelete,
        PathValues.REMINDERS_INFO: RemindersInfo,
        PathValues.REMINDERS_LIST: RemindersList,
        PathValues.RTM_CONNECT: RtmConnect,
        PathValues.SEARCH_MESSAGES: SearchMessages,
        PathValues.STARS_ADD: StarsAdd,
        PathValues.STARS_LIST: StarsList,
        PathValues.STARS_REMOVE: StarsRemove,
        PathValues.TEAM_ACCESS_LOGS: TeamAccessLogs,
        PathValues.TEAM_BILLABLE_INFO: TeamBillableInfo,
        PathValues.TEAM_INFO: TeamInfo,
        PathValues.TEAM_INTEGRATION_LOGS: TeamIntegrationLogs,
        PathValues.TEAM_PROFILE_GET: TeamProfileGet,
        PathValues.USERGROUPS_CREATE: UsergroupsCreate,
        PathValues.USERGROUPS_DISABLE: UsergroupsDisable,
        PathValues.USERGROUPS_ENABLE: UsergroupsEnable,
        PathValues.USERGROUPS_LIST: UsergroupsList,
        PathValues.USERGROUPS_UPDATE: UsergroupsUpdate,
        PathValues.USERGROUPS_USERS_LIST: UsergroupsUsersList,
        PathValues.USERGROUPS_USERS_UPDATE: UsergroupsUsersUpdate,
        PathValues.USERS_CONVERSATIONS: UsersConversations,
        PathValues.USERS_DELETE_PHOTO: UsersDeletePhoto,
        PathValues.USERS_GET_PRESENCE: UsersGetPresence,
        PathValues.USERS_IDENTITY: UsersIdentity,
        PathValues.USERS_INFO: UsersInfo,
        PathValues.USERS_LIST: UsersList,
        PathValues.USERS_LOOKUP_BY_EMAIL: UsersLookupByEmail,
        PathValues.USERS_PROFILE_GET: UsersProfileGet,
        PathValues.USERS_PROFILE_SET: UsersProfileSet,
        PathValues.USERS_SET_ACTIVE: UsersSetActive,
        PathValues.USERS_SET_PHOTO: UsersSetPhoto,
        PathValues.USERS_SET_PRESENCE: UsersSetPresence,
        PathValues.VIEWS_OPEN: ViewsOpen,
        PathValues.VIEWS_PUBLISH: ViewsPublish,
        PathValues.VIEWS_PUSH: ViewsPush,
        PathValues.VIEWS_UPDATE: ViewsUpdate,
        PathValues.WORKFLOWS_STEP_COMPLETED: WorkflowsStepCompleted,
        PathValues.WORKFLOWS_STEP_FAILED: WorkflowsStepFailed,
        PathValues.WORKFLOWS_UPDATE_STEP: WorkflowsUpdateStep,
    }
)
