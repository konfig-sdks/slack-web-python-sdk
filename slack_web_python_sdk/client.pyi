# coding: utf-8
"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

import typing
import inspect
from datetime import date, datetime
from slack_web_python_sdk.client_custom import ClientCustom
from slack_web_python_sdk.configuration import Configuration
from slack_web_python_sdk.api_client import ApiClient
from slack_web_python_sdk.type_util import copy_signature
from slack_web_python_sdk.apis.tags.admin_api import AdminApi
from slack_web_python_sdk.apis.tags.admin_apps_api import AdminAppsApi
from slack_web_python_sdk.apis.tags.admin_apps_approved_api import AdminAppsApprovedApi
from slack_web_python_sdk.apis.tags.admin_apps_requests_api import AdminAppsRequestsApi
from slack_web_python_sdk.apis.tags.admin_apps_restricted_api import AdminAppsRestrictedApi
from slack_web_python_sdk.apis.tags.admin_conversations_api import AdminConversationsApi
from slack_web_python_sdk.apis.tags.admin_conversations_ekm_api import AdminConversationsEkmApi
from slack_web_python_sdk.apis.tags.admin_conversations_restrict_access_api import AdminConversationsRestrictAccessApi
from slack_web_python_sdk.apis.tags.admin_emoji_api import AdminEmojiApi
from slack_web_python_sdk.apis.tags.admin_invite_requests_api import AdminInviteRequestsApi
from slack_web_python_sdk.apis.tags.admin_invite_requests_approved_api import AdminInviteRequestsApprovedApi
from slack_web_python_sdk.apis.tags.admin_invite_requests_denied_api import AdminInviteRequestsDeniedApi
from slack_web_python_sdk.apis.tags.admin_teams_api import AdminTeamsApi
from slack_web_python_sdk.apis.tags.admin_teams_admins_api import AdminTeamsAdminsApi
from slack_web_python_sdk.apis.tags.admin_teams_owners_api import AdminTeamsOwnersApi
from slack_web_python_sdk.apis.tags.admin_teams_settings_api import AdminTeamsSettingsApi
from slack_web_python_sdk.apis.tags.admin_usergroups_api import AdminUsergroupsApi
from slack_web_python_sdk.apis.tags.admin_users_api import AdminUsersApi
from slack_web_python_sdk.apis.tags.admin_users_session_api import AdminUsersSessionApi
from slack_web_python_sdk.apis.tags.api_api import ApiApi
from slack_web_python_sdk.apis.tags.apps_api import AppsApi
from slack_web_python_sdk.apis.tags.apps_event_authorizations_api import AppsEventAuthorizationsApi
from slack_web_python_sdk.apis.tags.apps_permissions_api import AppsPermissionsApi
from slack_web_python_sdk.apis.tags.apps_permissions_resources_api import AppsPermissionsResourcesApi
from slack_web_python_sdk.apis.tags.apps_permissions_scopes_api import AppsPermissionsScopesApi
from slack_web_python_sdk.apis.tags.apps_permissions_users_api import AppsPermissionsUsersApi
from slack_web_python_sdk.apis.tags.auth_api import AuthApi
from slack_web_python_sdk.apis.tags.bots_api import BotsApi
from slack_web_python_sdk.apis.tags.calls_api import CallsApi
from slack_web_python_sdk.apis.tags.calls_participants_api import CallsParticipantsApi
from slack_web_python_sdk.apis.tags.chat_api import ChatApi
from slack_web_python_sdk.apis.tags.chat_scheduled_messages_api import ChatScheduledMessagesApi
from slack_web_python_sdk.apis.tags.conversations_api import ConversationsApi
from slack_web_python_sdk.apis.tags.dialog_api import DialogApi
from slack_web_python_sdk.apis.tags.dnd_api import DndApi
from slack_web_python_sdk.apis.tags.emoji_api import EmojiApi
from slack_web_python_sdk.apis.tags.files_api import FilesApi
from slack_web_python_sdk.apis.tags.files_comments_api import FilesCommentsApi
from slack_web_python_sdk.apis.tags.files_remote_api import FilesRemoteApi
from slack_web_python_sdk.apis.tags.migration_api import MigrationApi
from slack_web_python_sdk.apis.tags.oauth_api import OauthApi
from slack_web_python_sdk.apis.tags.oauth_v2_api import OauthV2Api
from slack_web_python_sdk.apis.tags.pins_api import PinsApi
from slack_web_python_sdk.apis.tags.reactions_api import ReactionsApi
from slack_web_python_sdk.apis.tags.reminders_api import RemindersApi
from slack_web_python_sdk.apis.tags.rtm_api import RtmApi
from slack_web_python_sdk.apis.tags.search_api import SearchApi
from slack_web_python_sdk.apis.tags.stars_api import StarsApi
from slack_web_python_sdk.apis.tags.team_api import TeamApi
from slack_web_python_sdk.apis.tags.team_profile_api import TeamProfileApi
from slack_web_python_sdk.apis.tags.usergroups_api import UsergroupsApi
from slack_web_python_sdk.apis.tags.usergroups_users_api import UsergroupsUsersApi
from slack_web_python_sdk.apis.tags.users_api import UsersApi
from slack_web_python_sdk.apis.tags.users_profile_api import UsersProfileApi
from slack_web_python_sdk.apis.tags.views_api import ViewsApi
from slack_web_python_sdk.apis.tags.workflows_api import WorkflowsApi



class SlackWeb(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.admin: AdminApi = AdminApi(api_client)
        self.admin/apps: AdminAppsApi = AdminAppsApi(api_client)
        self.admin/apps/approved: AdminAppsApprovedApi = AdminAppsApprovedApi(api_client)
        self.admin/apps/requests: AdminAppsRequestsApi = AdminAppsRequestsApi(api_client)
        self.admin/apps/restricted: AdminAppsRestrictedApi = AdminAppsRestrictedApi(api_client)
        self.admin/conversations: AdminConversationsApi = AdminConversationsApi(api_client)
        self.admin/conversations/ekm: AdminConversationsEkmApi = AdminConversationsEkmApi(api_client)
        self.admin/conversations/restrict_access: AdminConversationsRestrictAccessApi = AdminConversationsRestrictAccessApi(api_client)
        self.admin/emoji: AdminEmojiApi = AdminEmojiApi(api_client)
        self.admin/invite_requests: AdminInviteRequestsApi = AdminInviteRequestsApi(api_client)
        self.admin/invite_requests/approved: AdminInviteRequestsApprovedApi = AdminInviteRequestsApprovedApi(api_client)
        self.admin/invite_requests/denied: AdminInviteRequestsDeniedApi = AdminInviteRequestsDeniedApi(api_client)
        self.admin/teams: AdminTeamsApi = AdminTeamsApi(api_client)
        self.admin/teams/admins: AdminTeamsAdminsApi = AdminTeamsAdminsApi(api_client)
        self.admin/teams/owners: AdminTeamsOwnersApi = AdminTeamsOwnersApi(api_client)
        self.admin/teams/settings: AdminTeamsSettingsApi = AdminTeamsSettingsApi(api_client)
        self.admin/usergroups: AdminUsergroupsApi = AdminUsergroupsApi(api_client)
        self.admin/users: AdminUsersApi = AdminUsersApi(api_client)
        self.admin/users/session: AdminUsersSessionApi = AdminUsersSessionApi(api_client)
        self.api: ApiApi = ApiApi(api_client)
        self.apps: AppsApi = AppsApi(api_client)
        self.apps/event/authorizations: AppsEventAuthorizationsApi = AppsEventAuthorizationsApi(api_client)
        self.apps/permissions: AppsPermissionsApi = AppsPermissionsApi(api_client)
        self.apps/permissions/resources: AppsPermissionsResourcesApi = AppsPermissionsResourcesApi(api_client)
        self.apps/permissions/scopes: AppsPermissionsScopesApi = AppsPermissionsScopesApi(api_client)
        self.apps/permissions/users: AppsPermissionsUsersApi = AppsPermissionsUsersApi(api_client)
        self.auth: AuthApi = AuthApi(api_client)
        self.bots: BotsApi = BotsApi(api_client)
        self.calls: CallsApi = CallsApi(api_client)
        self.calls/participants: CallsParticipantsApi = CallsParticipantsApi(api_client)
        self.chat: ChatApi = ChatApi(api_client)
        self.chat/scheduled_messages: ChatScheduledMessagesApi = ChatScheduledMessagesApi(api_client)
        self.conversations: ConversationsApi = ConversationsApi(api_client)
        self.dialog: DialogApi = DialogApi(api_client)
        self.dnd: DndApi = DndApi(api_client)
        self.emoji: EmojiApi = EmojiApi(api_client)
        self.files: FilesApi = FilesApi(api_client)
        self.files/comments: FilesCommentsApi = FilesCommentsApi(api_client)
        self.files/remote: FilesRemoteApi = FilesRemoteApi(api_client)
        self.migration: MigrationApi = MigrationApi(api_client)
        self.oauth: OauthApi = OauthApi(api_client)
        self.oauth/v2: OauthV2Api = OauthV2Api(api_client)
        self.pins: PinsApi = PinsApi(api_client)
        self.reactions: ReactionsApi = ReactionsApi(api_client)
        self.reminders: RemindersApi = RemindersApi(api_client)
        self.rtm: RtmApi = RtmApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
        self.stars: StarsApi = StarsApi(api_client)
        self.team: TeamApi = TeamApi(api_client)
        self.team/profile: TeamProfileApi = TeamProfileApi(api_client)
        self.usergroups: UsergroupsApi = UsergroupsApi(api_client)
        self.usergroups/users: UsergroupsUsersApi = UsergroupsUsersApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
        self.users/profile: UsersProfileApi = UsersProfileApi(api_client)
        self.views: ViewsApi = ViewsApi(api_client)
        self.workflows: WorkflowsApi = WorkflowsApi(api_client)
