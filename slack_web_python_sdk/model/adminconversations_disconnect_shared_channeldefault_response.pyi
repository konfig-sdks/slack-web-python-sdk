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


class AdminconversationsDisconnectSharedChanneldefaultResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Schema for error response from admin.conversations.disconnectShared
    """


    class MetaOapg:
        required = {
            "error",
            "ok",
        }
        
        class properties:
            
            
            class error(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FEATURE_NOT_ENABLED(cls):
                    return cls("feature_not_enabled")
                
                @schemas.classproperty
                def NOT_AN_ADMIN(cls):
                    return cls("not_an_admin")
                
                @schemas.classproperty
                def NOT_AN_ENTERPRISE(cls):
                    return cls("not_an_enterprise")
                
                @schemas.classproperty
                def CHANNEL_NOT_FOUND(cls):
                    return cls("channel_not_found")
                
                @schemas.classproperty
                def NOT_SUPPORTED(cls):
                    return cls("not_supported")
                
                @schemas.classproperty
                def TEAM_NOT_FOUND(cls):
                    return cls("team_not_found")
                
                @schemas.classproperty
                def RESTRICTED_ACTION(cls):
                    return cls("restricted_action")
                
                @schemas.classproperty
                def MISSING_SCOPE(cls):
                    return cls("missing_scope")
                
                @schemas.classproperty
                def LEAVING_TEAM_NOT_IN_CHANNEL(cls):
                    return cls("leaving_team_not_in_channel")
                
                @schemas.classproperty
                def NO_TEAMS_TO_DISCONNECT(cls):
                    return cls("no_teams_to_disconnect")
                
                @schemas.classproperty
                def LEAVING_TEAM_REQUIRED(cls):
                    return cls("leaving_team_required")
                
                @schemas.classproperty
                def CANNOT_KICK_TEAM(cls):
                    return cls("cannot_kick_team")
                
                @schemas.classproperty
                def CANNOT_KICK_HOME_TEAM(cls):
                    return cls("cannot_kick_home_team")
        
            @staticmethod
            def ok() -> typing.Type['DefsOkFalse']:
                return DefsOkFalse
            __annotations__ = {
                "error": error,
                "ok": ok,
            }
    
    error: MetaOapg.properties.error
    ok: 'DefsOkFalse'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkFalse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["error", "ok", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkFalse': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["error", "ok", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        error: typing.Union[MetaOapg.properties.error, str, ],
        ok: 'DefsOkFalse',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdminconversationsDisconnectSharedChanneldefaultResponse':
        return super().__new__(
            cls,
            *args,
            error=error,
            ok=ok,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.defs_ok_false import DefsOkFalse
