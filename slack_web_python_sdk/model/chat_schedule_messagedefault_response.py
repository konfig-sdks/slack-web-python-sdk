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


class ChatScheduleMessagedefaultResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Schema for error response chat.scheduleMessage method
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
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "invalid_time": "INVALID_TIME",
                        "time_in_past": "TIME_IN_PAST",
                        "time_too_far": "TIME_TOO_FAR",
                        "channel_not_found": "CHANNEL_NOT_FOUND",
                        "not_in_channel": "NOT_IN_CHANNEL",
                        "is_archived": "IS_ARCHIVED",
                        "msg_too_long": "MSG_TOO_LONG",
                        "no_text": "NO_TEXT",
                        "restricted_action": "RESTRICTED_ACTION",
                        "restricted_action_read_only_channel": "RESTRICTED_ACTION_READ_ONLY_CHANNEL",
                        "restricted_action_thread_only_channel": "RESTRICTED_ACTION_THREAD_ONLY_CHANNEL",
                        "restricted_action_non_threadable_channel": "RESTRICTED_ACTION_NON_THREADABLE_CHANNEL",
                        "too_many_attachments": "TOO_MANY_ATTACHMENTS",
                        "rate_limited": "RATE_LIMITED",
                        "not_authed": "NOT_AUTHED",
                        "invalid_auth": "INVALID_AUTH",
                        "account_inactive": "ACCOUNT_INACTIVE",
                        "token_revoked": "TOKEN_REVOKED",
                        "no_permission": "NO_PERMISSION",
                        "org_login_required": "ORG_LOGIN_REQUIRED",
                        "ekm_access_denied": "EKM_ACCESS_DENIED",
                        "missing_scope": "MISSING_SCOPE",
                        "invalid_arguments": "INVALID_ARGUMENTS",
                        "invalid_arg_name": "INVALID_ARG_NAME",
                        "invalid_charset": "INVALID_CHARSET",
                        "invalid_form_data": "INVALID_FORM_DATA",
                        "invalid_post_type": "INVALID_POST_TYPE",
                        "missing_post_type": "MISSING_POST_TYPE",
                        "team_added_to_org": "TEAM_ADDED_TO_ORG",
                        "invalid_json": "INVALID_JSON",
                        "json_not_object": "JSON_NOT_OBJECT",
                        "request_timeout": "REQUEST_TIMEOUT",
                        "upgrade_required": "UPGRADE_REQUIRED",
                        "fatal_error": "FATAL_ERROR",
                    }
                
                @schemas.classproperty
                def INVALID_TIME(cls):
                    return cls("invalid_time")
                
                @schemas.classproperty
                def TIME_IN_PAST(cls):
                    return cls("time_in_past")
                
                @schemas.classproperty
                def TIME_TOO_FAR(cls):
                    return cls("time_too_far")
                
                @schemas.classproperty
                def CHANNEL_NOT_FOUND(cls):
                    return cls("channel_not_found")
                
                @schemas.classproperty
                def NOT_IN_CHANNEL(cls):
                    return cls("not_in_channel")
                
                @schemas.classproperty
                def IS_ARCHIVED(cls):
                    return cls("is_archived")
                
                @schemas.classproperty
                def MSG_TOO_LONG(cls):
                    return cls("msg_too_long")
                
                @schemas.classproperty
                def NO_TEXT(cls):
                    return cls("no_text")
                
                @schemas.classproperty
                def RESTRICTED_ACTION(cls):
                    return cls("restricted_action")
                
                @schemas.classproperty
                def RESTRICTED_ACTION_READ_ONLY_CHANNEL(cls):
                    return cls("restricted_action_read_only_channel")
                
                @schemas.classproperty
                def RESTRICTED_ACTION_THREAD_ONLY_CHANNEL(cls):
                    return cls("restricted_action_thread_only_channel")
                
                @schemas.classproperty
                def RESTRICTED_ACTION_NON_THREADABLE_CHANNEL(cls):
                    return cls("restricted_action_non_threadable_channel")
                
                @schemas.classproperty
                def TOO_MANY_ATTACHMENTS(cls):
                    return cls("too_many_attachments")
                
                @schemas.classproperty
                def RATE_LIMITED(cls):
                    return cls("rate_limited")
                
                @schemas.classproperty
                def NOT_AUTHED(cls):
                    return cls("not_authed")
                
                @schemas.classproperty
                def INVALID_AUTH(cls):
                    return cls("invalid_auth")
                
                @schemas.classproperty
                def ACCOUNT_INACTIVE(cls):
                    return cls("account_inactive")
                
                @schemas.classproperty
                def TOKEN_REVOKED(cls):
                    return cls("token_revoked")
                
                @schemas.classproperty
                def NO_PERMISSION(cls):
                    return cls("no_permission")
                
                @schemas.classproperty
                def ORG_LOGIN_REQUIRED(cls):
                    return cls("org_login_required")
                
                @schemas.classproperty
                def EKM_ACCESS_DENIED(cls):
                    return cls("ekm_access_denied")
                
                @schemas.classproperty
                def MISSING_SCOPE(cls):
                    return cls("missing_scope")
                
                @schemas.classproperty
                def INVALID_ARGUMENTS(cls):
                    return cls("invalid_arguments")
                
                @schemas.classproperty
                def INVALID_ARG_NAME(cls):
                    return cls("invalid_arg_name")
                
                @schemas.classproperty
                def INVALID_CHARSET(cls):
                    return cls("invalid_charset")
                
                @schemas.classproperty
                def INVALID_FORM_DATA(cls):
                    return cls("invalid_form_data")
                
                @schemas.classproperty
                def INVALID_POST_TYPE(cls):
                    return cls("invalid_post_type")
                
                @schemas.classproperty
                def MISSING_POST_TYPE(cls):
                    return cls("missing_post_type")
                
                @schemas.classproperty
                def TEAM_ADDED_TO_ORG(cls):
                    return cls("team_added_to_org")
                
                @schemas.classproperty
                def INVALID_JSON(cls):
                    return cls("invalid_json")
                
                @schemas.classproperty
                def JSON_NOT_OBJECT(cls):
                    return cls("json_not_object")
                
                @schemas.classproperty
                def REQUEST_TIMEOUT(cls):
                    return cls("request_timeout")
                
                @schemas.classproperty
                def UPGRADE_REQUIRED(cls):
                    return cls("upgrade_required")
                
                @schemas.classproperty
                def FATAL_ERROR(cls):
                    return cls("fatal_error")
        
            @staticmethod
            def ok() -> typing.Type['DefsOkFalse']:
                return DefsOkFalse
            callstack = schemas.StrSchema
            __annotations__ = {
                "error": error,
                "ok": ok,
                "callstack": callstack,
            }
    
    error: MetaOapg.properties.error
    ok: 'DefsOkFalse'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkFalse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callstack"]) -> MetaOapg.properties.callstack: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["error", "ok", "callstack", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ok"]) -> 'DefsOkFalse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callstack"]) -> typing.Union[MetaOapg.properties.callstack, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["error", "ok", "callstack", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        error: typing.Union[MetaOapg.properties.error, str, ],
        ok: 'DefsOkFalse',
        callstack: typing.Union[MetaOapg.properties.callstack, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChatScheduleMessagedefaultResponse':
        return super().__new__(
            cls,
            *args,
            error=error,
            ok=ok,
            callstack=callstack,
            _configuration=_configuration,
            **kwargs,
        )

from slack_web_python_sdk.model.defs_ok_false import DefsOkFalse
