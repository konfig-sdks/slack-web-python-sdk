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

from slack_web_python_sdk.model.usergroups_list_response import UsergroupsListResponse as UsergroupsListResponseSchema
from slack_web_python_sdk.model.usergroups_listdefault_response import UsergroupsListdefaultResponse as UsergroupsListdefaultResponseSchema

from slack_web_python_sdk.type.usergroups_listdefault_response import UsergroupsListdefaultResponse
from slack_web_python_sdk.type.usergroups_list_response import UsergroupsListResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.usergroups_list_response import UsergroupsListResponse as UsergroupsListResponsePydantic
from slack_web_python_sdk.pydantic.usergroups_listdefault_response import UsergroupsListdefaultResponse as UsergroupsListdefaultResponsePydantic

# Query params
IncludeUsersSchema = schemas.BoolSchema
TokenSchema = schemas.StrSchema
IncludeCountSchema = schemas.BoolSchema
IncludeDisabledSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'token': typing.Union[TokenSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'include_users': typing.Union[IncludeUsersSchema, bool, ],
        'include_count': typing.Union[IncludeCountSchema, bool, ],
        'include_disabled': typing.Union[IncludeDisabledSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_include_users = api_client.QueryParameter(
    name="include_users",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeUsersSchema,
    explode=True,
)
request_query_token = api_client.QueryParameter(
    name="token",
    style=api_client.ParameterStyle.FORM,
    schema=TokenSchema,
    required=True,
    explode=True,
)
request_query_include_count = api_client.QueryParameter(
    name="include_count",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeCountSchema,
    explode=True,
)
request_query_include_disabled = api_client.QueryParameter(
    name="include_disabled",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeDisabledSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = UsergroupsListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UsergroupsListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsergroupsListResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = UsergroupsListdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: UsergroupsListdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: UsergroupsListdefaultResponse


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

    def _list_mapped_args(
        self,
        token: str,
        include_users: typing.Optional[bool] = None,
        include_count: typing.Optional[bool] = None,
        include_disabled: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if include_users is not None:
            _query_params["include_users"] = include_users
        if token is not None:
            _query_params["token"] = token
        if include_count is not None:
            _query_params["include_count"] = include_count
        if include_disabled is not None:
            _query_params["include_disabled"] = include_disabled
        args.query = _query_params
        return args

    async def _alist_oapg(
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
            request_query_include_users,
            request_query_token,
            request_query_include_count,
            request_query_include_disabled,
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
            path_template='/usergroups.list',
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


    def _list_oapg(
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
            request_query_include_users,
            request_query_token,
            request_query_include_count,
            request_query_include_disabled,
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
            path_template='/usergroups.list',
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


class ListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist(
        self,
        token: str,
        include_users: typing.Optional[bool] = None,
        include_count: typing.Optional[bool] = None,
        include_disabled: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            token=token,
            include_users=include_users,
            include_count=include_count,
            include_disabled=include_disabled,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        token: str,
        include_users: typing.Optional[bool] = None,
        include_count: typing.Optional[bool] = None,
        include_disabled: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            token=token,
            include_users=include_users,
            include_count=include_count,
            include_disabled=include_disabled,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        token: str,
        include_users: typing.Optional[bool] = None,
        include_count: typing.Optional[bool] = None,
        include_disabled: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsergroupsListResponsePydantic:
        raw_response = await self.raw.alist(
            token=token,
            include_users=include_users,
            include_count=include_count,
            include_disabled=include_disabled,
            **kwargs,
        )
        if validate:
            return UsergroupsListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UsergroupsListResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        token: str,
        include_users: typing.Optional[bool] = None,
        include_count: typing.Optional[bool] = None,
        include_disabled: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> UsergroupsListResponsePydantic:
        raw_response = self.raw.list(
            token=token,
            include_users=include_users,
            include_count=include_count,
            include_disabled=include_disabled,
        )
        if validate:
            return UsergroupsListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UsergroupsListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: str,
        include_users: typing.Optional[bool] = None,
        include_count: typing.Optional[bool] = None,
        include_disabled: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            token=token,
            include_users=include_users,
            include_count=include_count,
            include_disabled=include_disabled,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        token: str,
        include_users: typing.Optional[bool] = None,
        include_count: typing.Optional[bool] = None,
        include_disabled: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            token=token,
            include_users=include_users,
            include_count=include_count,
            include_disabled=include_disabled,
        )
        return self._list_oapg(
            query_params=args.query,
        )

