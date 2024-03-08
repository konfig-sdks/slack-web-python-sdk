# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slack_web_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ADMIN = "admin"
    CONVERSATIONS = "conversations"
    ADMIN_CONVERSATIONS = "admin.conversations"
    FILES = "files"
    USERS = "users"
    CHAT = "chat"
    ADMIN_USERS = "admin.users"
    APPS = "apps"
    USERGROUPS = "usergroups"
    ADMIN_TEAMS_SETTINGS = "admin.teams.settings"
    CALLS = "calls"
    FILES_REMOTE = "files.remote"
    ADMIN_EMOJI = "admin.emoji"
    DND = "dnd"
    REMINDERS = "reminders"
    TEAM = "team"
    ADMIN_USERGROUPS = "admin.usergroups"
    REACTIONS = "reactions"
    VIEWS = "views"
    ADMIN_CONVERSATIONS_RESTRICT_ACCESS = "admin.conversations.restrictAccess"
    ADMIN_INVITE_REQUESTS = "admin.inviteRequests"
    OAUTH = "oauth"
    PINS = "pins"
    STARS = "stars"
    WORKFLOWS = "workflows"
    ADMIN_APPS = "admin.apps"
    ADMIN_TEAMS = "admin.teams"
    ADMIN_USERS_SESSION = "admin.users.session"
    APPS_PERMISSIONS = "apps.permissions"
    APPS_PERMISSIONS_USERS = "apps.permissions.users"
    AUTH = "auth"
    CALLS_PARTICIPANTS = "calls.participants"
    USERGROUPS_USERS = "usergroups.users"
    USERS_PROFILE = "users.profile"
    ADMIN_APPS_APPROVED = "admin.apps.approved"
    ADMIN_APPS_REQUESTS = "admin.apps.requests"
    ADMIN_APPS_RESTRICTED = "admin.apps.restricted"
    ADMIN_CONVERSATIONS_EKM = "admin.conversations.ekm"
    ADMIN_INVITE_REQUESTS_APPROVED = "admin.inviteRequests.approved"
    ADMIN_INVITE_REQUESTS_DENIED = "admin.inviteRequests.denied"
    ADMIN_TEAMS_ADMINS = "admin.teams.admins"
    ADMIN_TEAMS_OWNERS = "admin.teams.owners"
    API = "api"
    APPS_EVENT_AUTHORIZATIONS = "apps.event.authorizations"
    APPS_PERMISSIONS_RESOURCES = "apps.permissions.resources"
    APPS_PERMISSIONS_SCOPES = "apps.permissions.scopes"
    BOTS = "bots"
    CHAT_SCHEDULED_MESSAGES = "chat.scheduledMessages"
    DIALOG = "dialog"
    EMOJI = "emoji"
    FILES_COMMENTS = "files.comments"
    MIGRATION = "migration"
    OAUTH_V2 = "oauth.v2"
    RTM = "rtm"
    SEARCH = "search"
    TEAM_PROFILE = "team.profile"