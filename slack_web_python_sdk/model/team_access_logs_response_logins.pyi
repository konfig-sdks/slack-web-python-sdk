# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from slack_web_python_sdk import schemas  # noqa: F401


class TeamAccessLogsResponseLogins(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TeamAccessLogsResponseLoginsItem']:
            return TeamAccessLogsResponseLoginsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TeamAccessLogsResponseLoginsItem'], typing.List['TeamAccessLogsResponseLoginsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TeamAccessLogsResponseLogins':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TeamAccessLogsResponseLoginsItem':
        return super().__getitem__(i)

from slack_web_python_sdk.model.team_access_logs_response_logins_item import TeamAccessLogsResponseLoginsItem
