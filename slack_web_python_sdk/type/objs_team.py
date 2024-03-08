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

from slack_web_python_sdk.type.defs_enterprise_id import DefsEnterpriseId
from slack_web_python_sdk.type.defs_workspace_id import DefsWorkspaceId
from slack_web_python_sdk.type.objs_external_org_migrations import ObjsExternalOrgMigrations
from slack_web_python_sdk.type.objs_icon import ObjsIcon
from slack_web_python_sdk.type.objs_primary_owner import ObjsPrimaryOwner
from slack_web_python_sdk.type.objs_team_sso_provider import ObjsTeamSsoProvider

class RequiredObjsTeam(TypedDict):
    domain: str

    email_domain: str

    icon: ObjsIcon

    id: DefsWorkspaceId

    name: str

class OptionalObjsTeam(TypedDict, total=False):
    description: typing.Optional[str]

    archived: bool

    avatar_base_url: str

    created: int

    date_create: int

    deleted: bool

    discoverable: typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[str]]]

    enterprise_id: DefsEnterpriseId

    enterprise_name: str

    external_org_migrations: ObjsExternalOrgMigrations

    has_compliance_export: bool

    is_assigned: bool

    is_enterprise: int

    is_over_storage_limit: bool

    limit_ts: int

    locale: str

    messages_count: int

    msg_edit_window_mins: int

    over_integrations_limit: bool

    over_storage_limit: bool

    pay_prod_cur: str

    plan: str

    primary_owner: ObjsPrimaryOwner

    sso_provider: ObjsTeamSsoProvider

class ObjsTeam(RequiredObjsTeam, OptionalObjsTeam):
    pass
