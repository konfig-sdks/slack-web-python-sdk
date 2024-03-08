# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from slack_web_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from slack_web_python_sdk.api_response import AsyncGeneratorResponse
from slack_web_python_sdk import api_client, exceptions
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

from slack_web_python_sdk.model.appspermissionsusers_request_modaldefault_response import AppspermissionsusersRequestModaldefaultResponse as AppspermissionsusersRequestModaldefaultResponseSchema
from slack_web_python_sdk.model.appspermissionsusers_request_modal_response import AppspermissionsusersRequestModalResponse as AppspermissionsusersRequestModalResponseSchema

from slack_web_python_sdk.type.appspermissionsusers_request_modal_response import AppspermissionsusersRequestModalResponse
from slack_web_python_sdk.type.appspermissionsusers_request_modaldefault_response import AppspermissionsusersRequestModaldefaultResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.appspermissionsusers_request_modal_response import AppspermissionsusersRequestModalResponse as AppspermissionsusersRequestModalResponsePydantic
from slack_web_python_sdk.pydantic.appspermissionsusers_request_modaldefault_response import AppspermissionsusersRequestModaldefaultResponse as AppspermissionsusersRequestModaldefaultResponsePydantic

# Query params
TokenSchema = schemas.StrSchema
ScopesSchema = schemas.StrSchema
TriggerIdSchema = schemas.StrSchema
UserSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'token': typing.Union[TokenSchema, str, ],
        'scopes': typing.Union[ScopesSchema, str, ],
        'trigger_id': typing.Union[TriggerIdSchema, str, ],
        'user': typing.Union[UserSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_token = api_client.QueryParameter(
    name="token",
    style=api_client.ParameterStyle.FORM,
    schema=TokenSchema,
    required=True,
    explode=True,
)
request_query_scopes = api_client.QueryParameter(
    name="scopes",
    style=api_client.ParameterStyle.FORM,
    schema=ScopesSchema,
    required=True,
    explode=True,
)
request_query_trigger_id = api_client.QueryParameter(
    name="trigger_id",
    style=api_client.ParameterStyle.FORM,
    schema=TriggerIdSchema,
    required=True,
    explode=True,
)
request_query_user = api_client.QueryParameter(
    name="user",
    style=api_client.ParameterStyle.FORM,
    schema=UserSchema,
    required=True,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = AppspermissionsusersRequestModalResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AppspermissionsusersRequestModalResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AppspermissionsusersRequestModalResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = AppspermissionsusersRequestModaldefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: AppspermissionsusersRequestModaldefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: AppspermissionsusersRequestModaldefaultResponse


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _request_modal_mapped_args(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if token is not None:
            _query_params["token"] = token
        if scopes is not None:
            _query_params["scopes"] = scopes
        if trigger_id is not None:
            _query_params["trigger_id"] = trigger_id
        if user is not None:
            _query_params["user"] = user
        args.query = _query_params
        return args

    async def _arequest_modal_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_token,
            request_query_scopes,
            request_query_trigger_id,
            request_query_user,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/apps.permissions.users.request',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _request_modal_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_token,
            request_query_scopes,
            request_query_trigger_id,
            request_query_user,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/apps.permissions.users.request',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class RequestModalRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arequest_modal(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._request_modal_mapped_args(
            token=token,
            scopes=scopes,
            trigger_id=trigger_id,
            user=user,
        )
        return await self._arequest_modal_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def request_modal(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._request_modal_mapped_args(
            token=token,
            scopes=scopes,
            trigger_id=trigger_id,
            user=user,
        )
        return self._request_modal_oapg(
            query_params=args.query,
        )

class RequestModal(BaseApi):

    async def arequest_modal(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
        validate: bool = False,
        **kwargs,
    ) -> AppspermissionsusersRequestModalResponsePydantic:
        raw_response = await self.raw.arequest_modal(
            token=token,
            scopes=scopes,
            trigger_id=trigger_id,
            user=user,
            **kwargs,
        )
        if validate:
            return AppspermissionsusersRequestModalResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AppspermissionsusersRequestModalResponsePydantic, raw_response.body)
    
    
    def request_modal(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
        validate: bool = False,
    ) -> AppspermissionsusersRequestModalResponsePydantic:
        raw_response = self.raw.request_modal(
            token=token,
            scopes=scopes,
            trigger_id=trigger_id,
            user=user,
        )
        if validate:
            return AppspermissionsusersRequestModalResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AppspermissionsusersRequestModalResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._request_modal_mapped_args(
            token=token,
            scopes=scopes,
            trigger_id=trigger_id,
            user=user,
        )
        return await self._arequest_modal_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._request_modal_mapped_args(
            token=token,
            scopes=scopes,
            trigger_id=trigger_id,
            user=user,
        )
        return self._request_modal_oapg(
            query_params=args.query,
        )

