# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slack_web_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ADMIN_APPS_APPROVE = "/admin.apps.approve"
    ADMIN_APPS_APPROVED_LIST = "/admin.apps.approved.list"
    ADMIN_APPS_REQUESTS_LIST = "/admin.apps.requests.list"
    ADMIN_APPS_RESTRICT = "/admin.apps.restrict"
    ADMIN_APPS_RESTRICTED_LIST = "/admin.apps.restricted.list"
    ADMIN_CONVERSATIONS_ARCHIVE = "/admin.conversations.archive"
    ADMIN_CONVERSATIONS_CONVERT_TO_PRIVATE = "/admin.conversations.convertToPrivate"
    ADMIN_CONVERSATIONS_CREATE = "/admin.conversations.create"
    ADMIN_CONVERSATIONS_DELETE = "/admin.conversations.delete"
    ADMIN_CONVERSATIONS_DISCONNECT_SHARED = "/admin.conversations.disconnectShared"
    ADMIN_CONVERSATIONS_EKM_LIST_ORIGINAL_CONNECTED_CHANNEL_INFO = "/admin.conversations.ekm.listOriginalConnectedChannelInfo"
    ADMIN_CONVERSATIONS_GET_CONVERSATION_PREFS = "/admin.conversations.getConversationPrefs"
    ADMIN_CONVERSATIONS_GET_TEAMS = "/admin.conversations.getTeams"
    ADMIN_CONVERSATIONS_INVITE = "/admin.conversations.invite"
    ADMIN_CONVERSATIONS_RENAME = "/admin.conversations.rename"
    ADMIN_CONVERSATIONS_RESTRICT_ACCESS_ADD_GROUP = "/admin.conversations.restrictAccess.addGroup"
    ADMIN_CONVERSATIONS_RESTRICT_ACCESS_LIST_GROUPS = "/admin.conversations.restrictAccess.listGroups"
    ADMIN_CONVERSATIONS_RESTRICT_ACCESS_REMOVE_GROUP = "/admin.conversations.restrictAccess.removeGroup"
    ADMIN_CONVERSATIONS_SEARCH = "/admin.conversations.search"
    ADMIN_CONVERSATIONS_SET_CONVERSATION_PREFS = "/admin.conversations.setConversationPrefs"
    ADMIN_CONVERSATIONS_SET_TEAMS = "/admin.conversations.setTeams"
    ADMIN_CONVERSATIONS_UNARCHIVE = "/admin.conversations.unarchive"
    ADMIN_EMOJI_ADD = "/admin.emoji.add"
    ADMIN_EMOJI_ADD_ALIAS = "/admin.emoji.addAlias"
    ADMIN_EMOJI_LIST = "/admin.emoji.list"
    ADMIN_EMOJI_REMOVE = "/admin.emoji.remove"
    ADMIN_EMOJI_RENAME = "/admin.emoji.rename"
    ADMIN_INVITE_REQUESTS_APPROVE = "/admin.inviteRequests.approve"
    ADMIN_INVITE_REQUESTS_APPROVED_LIST = "/admin.inviteRequests.approved.list"
    ADMIN_INVITE_REQUESTS_DENIED_LIST = "/admin.inviteRequests.denied.list"
    ADMIN_INVITE_REQUESTS_DENY = "/admin.inviteRequests.deny"
    ADMIN_INVITE_REQUESTS_LIST = "/admin.inviteRequests.list"
    ADMIN_TEAMS_ADMINS_LIST = "/admin.teams.admins.list"
    ADMIN_TEAMS_CREATE = "/admin.teams.create"
    ADMIN_TEAMS_LIST = "/admin.teams.list"
    ADMIN_TEAMS_OWNERS_LIST = "/admin.teams.owners.list"
    ADMIN_TEAMS_SETTINGS_INFO = "/admin.teams.settings.info"
    ADMIN_TEAMS_SETTINGS_SET_DEFAULT_CHANNELS = "/admin.teams.settings.setDefaultChannels"
    ADMIN_TEAMS_SETTINGS_SET_DESCRIPTION = "/admin.teams.settings.setDescription"
    ADMIN_TEAMS_SETTINGS_SET_DISCOVERABILITY = "/admin.teams.settings.setDiscoverability"
    ADMIN_TEAMS_SETTINGS_SET_ICON = "/admin.teams.settings.setIcon"
    ADMIN_TEAMS_SETTINGS_SET_NAME = "/admin.teams.settings.setName"
    ADMIN_USERGROUPS_ADD_CHANNELS = "/admin.usergroups.addChannels"
    ADMIN_USERGROUPS_ADD_TEAMS = "/admin.usergroups.addTeams"
    ADMIN_USERGROUPS_LIST_CHANNELS = "/admin.usergroups.listChannels"
    ADMIN_USERGROUPS_REMOVE_CHANNELS = "/admin.usergroups.removeChannels"
    ADMIN_USERS_ASSIGN = "/admin.users.assign"
    ADMIN_USERS_INVITE = "/admin.users.invite"
    ADMIN_USERS_LIST = "/admin.users.list"
    ADMIN_USERS_REMOVE = "/admin.users.remove"
    ADMIN_USERS_SESSION_INVALIDATE = "/admin.users.session.invalidate"
    ADMIN_USERS_SESSION_RESET = "/admin.users.session.reset"
    ADMIN_USERS_SET_ADMIN = "/admin.users.setAdmin"
    ADMIN_USERS_SET_EXPIRATION = "/admin.users.setExpiration"
    ADMIN_USERS_SET_OWNER = "/admin.users.setOwner"
    ADMIN_USERS_SET_REGULAR = "/admin.users.setRegular"
    API_TEST = "/api.test"
    APPS_EVENT_AUTHORIZATIONS_LIST = "/apps.event.authorizations.list"
    APPS_PERMISSIONS_INFO = "/apps.permissions.info"
    APPS_PERMISSIONS_REQUEST = "/apps.permissions.request"
    APPS_PERMISSIONS_RESOURCES_LIST = "/apps.permissions.resources.list"
    APPS_PERMISSIONS_SCOPES_LIST = "/apps.permissions.scopes.list"
    APPS_PERMISSIONS_USERS_LIST = "/apps.permissions.users.list"
    APPS_PERMISSIONS_USERS_REQUEST = "/apps.permissions.users.request"
    APPS_UNINSTALL = "/apps.uninstall"
    AUTH_REVOKE = "/auth.revoke"
    AUTH_TEST = "/auth.test"
    BOTS_INFO = "/bots.info"
    CALLS_ADD = "/calls.add"
    CALLS_END = "/calls.end"
    CALLS_INFO = "/calls.info"
    CALLS_PARTICIPANTS_ADD = "/calls.participants.add"
    CALLS_PARTICIPANTS_REMOVE = "/calls.participants.remove"
    CALLS_UPDATE = "/calls.update"
    CHAT_DELETE = "/chat.delete"
    CHAT_DELETE_SCHEDULED_MESSAGE = "/chat.deleteScheduledMessage"
    CHAT_GET_PERMALINK = "/chat.getPermalink"
    CHAT_ME_MESSAGE = "/chat.meMessage"
    CHAT_POST_EPHEMERAL = "/chat.postEphemeral"
    CHAT_POST_MESSAGE = "/chat.postMessage"
    CHAT_SCHEDULE_MESSAGE = "/chat.scheduleMessage"
    CHAT_SCHEDULED_MESSAGES_LIST = "/chat.scheduledMessages.list"
    CHAT_UNFURL = "/chat.unfurl"
    CHAT_UPDATE = "/chat.update"
    CONVERSATIONS_ARCHIVE = "/conversations.archive"
    CONVERSATIONS_CLOSE = "/conversations.close"
    CONVERSATIONS_CREATE = "/conversations.create"
    CONVERSATIONS_HISTORY = "/conversations.history"
    CONVERSATIONS_INFO = "/conversations.info"
    CONVERSATIONS_INVITE = "/conversations.invite"
    CONVERSATIONS_JOIN = "/conversations.join"
    CONVERSATIONS_KICK = "/conversations.kick"
    CONVERSATIONS_LEAVE = "/conversations.leave"
    CONVERSATIONS_LIST = "/conversations.list"
    CONVERSATIONS_MARK = "/conversations.mark"
    CONVERSATIONS_MEMBERS = "/conversations.members"
    CONVERSATIONS_OPEN = "/conversations.open"
    CONVERSATIONS_RENAME = "/conversations.rename"
    CONVERSATIONS_REPLIES = "/conversations.replies"
    CONVERSATIONS_SET_PURPOSE = "/conversations.setPurpose"
    CONVERSATIONS_SET_TOPIC = "/conversations.setTopic"
    CONVERSATIONS_UNARCHIVE = "/conversations.unarchive"
    DIALOG_OPEN = "/dialog.open"
    DND_END_DND = "/dnd.endDnd"
    DND_END_SNOOZE = "/dnd.endSnooze"
    DND_INFO = "/dnd.info"
    DND_SET_SNOOZE = "/dnd.setSnooze"
    DND_TEAM_INFO = "/dnd.teamInfo"
    EMOJI_LIST = "/emoji.list"
    FILES_COMMENTS_DELETE = "/files.comments.delete"
    FILES_DELETE = "/files.delete"
    FILES_INFO = "/files.info"
    FILES_LIST = "/files.list"
    FILES_REMOTE_ADD = "/files.remote.add"
    FILES_REMOTE_INFO = "/files.remote.info"
    FILES_REMOTE_LIST = "/files.remote.list"
    FILES_REMOTE_REMOVE = "/files.remote.remove"
    FILES_REMOTE_SHARE = "/files.remote.share"
    FILES_REMOTE_UPDATE = "/files.remote.update"
    FILES_REVOKE_PUBLIC_URL = "/files.revokePublicURL"
    FILES_SHARED_PUBLIC_URL = "/files.sharedPublicURL"
    FILES_UPLOAD = "/files.upload"
    MIGRATION_EXCHANGE = "/migration.exchange"
    OAUTH_ACCESS = "/oauth.access"
    OAUTH_TOKEN = "/oauth.token"
    OAUTH_V2_ACCESS = "/oauth.v2.access"
    PINS_ADD = "/pins.add"
    PINS_LIST = "/pins.list"
    PINS_REMOVE = "/pins.remove"
    REACTIONS_ADD = "/reactions.add"
    REACTIONS_GET = "/reactions.get"
    REACTIONS_LIST = "/reactions.list"
    REACTIONS_REMOVE = "/reactions.remove"
    REMINDERS_ADD = "/reminders.add"
    REMINDERS_COMPLETE = "/reminders.complete"
    REMINDERS_DELETE = "/reminders.delete"
    REMINDERS_INFO = "/reminders.info"
    REMINDERS_LIST = "/reminders.list"
    RTM_CONNECT = "/rtm.connect"
    SEARCH_MESSAGES = "/search.messages"
    STARS_ADD = "/stars.add"
    STARS_LIST = "/stars.list"
    STARS_REMOVE = "/stars.remove"
    TEAM_ACCESS_LOGS = "/team.accessLogs"
    TEAM_BILLABLE_INFO = "/team.billableInfo"
    TEAM_INFO = "/team.info"
    TEAM_INTEGRATION_LOGS = "/team.integrationLogs"
    TEAM_PROFILE_GET = "/team.profile.get"
    USERGROUPS_CREATE = "/usergroups.create"
    USERGROUPS_DISABLE = "/usergroups.disable"
    USERGROUPS_ENABLE = "/usergroups.enable"
    USERGROUPS_LIST = "/usergroups.list"
    USERGROUPS_UPDATE = "/usergroups.update"
    USERGROUPS_USERS_LIST = "/usergroups.users.list"
    USERGROUPS_USERS_UPDATE = "/usergroups.users.update"
    USERS_CONVERSATIONS = "/users.conversations"
    USERS_DELETE_PHOTO = "/users.deletePhoto"
    USERS_GET_PRESENCE = "/users.getPresence"
    USERS_IDENTITY = "/users.identity"
    USERS_INFO = "/users.info"
    USERS_LIST = "/users.list"
    USERS_LOOKUP_BY_EMAIL = "/users.lookupByEmail"
    USERS_PROFILE_GET = "/users.profile.get"
    USERS_PROFILE_SET = "/users.profile.set"
    USERS_SET_ACTIVE = "/users.setActive"
    USERS_SET_PHOTO = "/users.setPhoto"
    USERS_SET_PRESENCE = "/users.setPresence"
    VIEWS_OPEN = "/views.open"
    VIEWS_PUBLISH = "/views.publish"
    VIEWS_PUSH = "/views.push"
    VIEWS_UPDATE = "/views.update"
    WORKFLOWS_STEP_COMPLETED = "/workflows.stepCompleted"
    WORKFLOWS_STEP_FAILED = "/workflows.stepFailed"
    WORKFLOWS_UPDATE_STEP = "/workflows.updateStep"