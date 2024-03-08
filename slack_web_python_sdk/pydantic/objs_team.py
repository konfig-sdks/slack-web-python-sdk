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
from pydantic import BaseModel, Field, RootModel

from slack_web_python_sdk.pydantic.defs_enterprise_id import DefsEnterpriseId
from slack_web_python_sdk.pydantic.defs_workspace_id import DefsWorkspaceId
from slack_web_python_sdk.pydantic.objs_external_org_migrations import ObjsExternalOrgMigrations
from slack_web_python_sdk.pydantic.objs_icon import ObjsIcon
from slack_web_python_sdk.pydantic.objs_primary_owner import ObjsPrimaryOwner
from slack_web_python_sdk.pydantic.objs_team_sso_provider import ObjsTeamSsoProvider

class ObjsTeam(BaseModel):
    domain: str = Field(alias='domain')

    email_domain: str = Field(alias='email_domain')

    icon: ObjsIcon = Field(alias='icon')

    id: DefsWorkspaceId = Field(alias='id')

    name: str = Field(alias='name')

    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    archived: typing.Optional[bool] = Field(None, alias='archived')

    avatar_base_url: typing.Optional[str] = Field(None, alias='avatar_base_url')

    created: typing.Optional[int] = Field(None, alias='created')

    date_create: typing.Optional[int] = Field(None, alias='date_create')

    deleted: typing.Optional[bool] = Field(None, alias='deleted')

    discoverable: typing.Optional[typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[str]]]] = Field(None, alias='discoverable')

    enterprise_id: typing.Optional[DefsEnterpriseId] = Field(None, alias='enterprise_id')

    enterprise_name: typing.Optional[str] = Field(None, alias='enterprise_name')

    external_org_migrations: typing.Optional[ObjsExternalOrgMigrations] = Field(None, alias='external_org_migrations')

    has_compliance_export: typing.Optional[bool] = Field(None, alias='has_compliance_export')

    is_assigned: typing.Optional[bool] = Field(None, alias='is_assigned')

    is_enterprise: typing.Optional[int] = Field(None, alias='is_enterprise')

    is_over_storage_limit: typing.Optional[bool] = Field(None, alias='is_over_storage_limit')

    limit_ts: typing.Optional[int] = Field(None, alias='limit_ts')

    locale: typing.Optional[str] = Field(None, alias='locale')

    messages_count: typing.Optional[int] = Field(None, alias='messages_count')

    msg_edit_window_mins: typing.Optional[int] = Field(None, alias='msg_edit_window_mins')

    over_integrations_limit: typing.Optional[bool] = Field(None, alias='over_integrations_limit')

    over_storage_limit: typing.Optional[bool] = Field(None, alias='over_storage_limit')

    pay_prod_cur: typing.Optional[str] = Field(None, alias='pay_prod_cur')

    plan: typing.Optional[Literal["", "std", "plus", "compliance", "enterprise"]] = Field(None, alias='plan')

    primary_owner: typing.Optional[ObjsPrimaryOwner] = Field(None, alias='primary_owner')

    sso_provider: typing.Optional[ObjsTeamSsoProvider] = Field(None, alias='sso_provider')
    class Config:
        arbitrary_types_allowed = True
