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

from slack_web_python_sdk.model.adminusergroups_list_channels_getdefault_response import AdminusergroupsListChannelsGetdefaultResponse as AdminusergroupsListChannelsGetdefaultResponseSchema
from slack_web_python_sdk.model.adminusergroups_list_channels_get_response import AdminusergroupsListChannelsGetResponse as AdminusergroupsListChannelsGetResponseSchema

from slack_web_python_sdk.type.adminusergroups_list_channels_get_response import AdminusergroupsListChannelsGetResponse
from slack_web_python_sdk.type.adminusergroups_list_channels_getdefault_response import AdminusergroupsListChannelsGetdefaultResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.adminusergroups_list_channels_get_response import AdminusergroupsListChannelsGetResponse as AdminusergroupsListChannelsGetResponsePydantic
from slack_web_python_sdk.pydantic.adminusergroups_list_channels_getdefault_response import AdminusergroupsListChannelsGetdefaultResponse as AdminusergroupsListChannelsGetdefaultResponsePydantic

# Query params
UsergroupIdSchema = schemas.StrSchema
TeamIdSchema = schemas.StrSchema
IncludeNumMembersSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'usergroup_id': typing.Union[UsergroupIdSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'team_id': typing.Union[TeamIdSchema, str, ],
        'include_num_members': typing.Union[IncludeNumMembersSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_usergroup_id = api_client.QueryParameter(
    name="usergroup_id",
    style=api_client.ParameterStyle.FORM,
    schema=UsergroupIdSchema,
    required=True,
    explode=True,
)
request_query_team_id = api_client.QueryParameter(
    name="team_id",
    style=api_client.ParameterStyle.FORM,
    schema=TeamIdSchema,
    explode=True,
)
request_query_include_num_members = api_client.QueryParameter(
    name="include_num_members",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeNumMembersSchema,
    explode=True,
)
# Header params
TokenSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'token': typing.Union[TokenSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_token = api_client.HeaderParameter(
    name="token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TokenSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = AdminusergroupsListChannelsGetResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AdminusergroupsListChannelsGetResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AdminusergroupsListChannelsGetResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = AdminusergroupsListChannelsGetdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: AdminusergroupsListChannelsGetdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: AdminusergroupsListChannelsGetdefaultResponse


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

    def _list_channels_get_mapped_args(
        self,
        token: str,
        usergroup_id: str,
        team_id: typing.Optional[str] = None,
        include_num_members: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if usergroup_id is not None:
            _query_params["usergroup_id"] = usergroup_id
        if team_id is not None:
            _query_params["team_id"] = team_id
        if include_num_members is not None:
            _query_params["include_num_members"] = include_num_members
        if token is not None:
            _header_params["token"] = token
        args.query = _query_params
        args.header = _header_params
        return args

    async def _alist_channels_get_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
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
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_usergroup_id,
            request_query_team_id,
            request_query_include_num_members,
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
        for parameter in (
            request_header_token,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/admin.usergroups.listChannels',
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


    def _list_channels_get_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
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
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_usergroup_id,
            request_query_team_id,
            request_query_include_num_members,
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
        for parameter in (
            request_header_token,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/admin.usergroups.listChannels',
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


class ListChannelsGetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_channels_get(
        self,
        token: str,
        usergroup_id: str,
        team_id: typing.Optional[str] = None,
        include_num_members: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_channels_get_mapped_args(
            token=token,
            usergroup_id=usergroup_id,
            team_id=team_id,
            include_num_members=include_num_members,
        )
        return await self._alist_channels_get_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def list_channels_get(
        self,
        token: str,
        usergroup_id: str,
        team_id: typing.Optional[str] = None,
        include_num_members: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_channels_get_mapped_args(
            token=token,
            usergroup_id=usergroup_id,
            team_id=team_id,
            include_num_members=include_num_members,
        )
        return self._list_channels_get_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class ListChannelsGet(BaseApi):

    async def alist_channels_get(
        self,
        token: str,
        usergroup_id: str,
        team_id: typing.Optional[str] = None,
        include_num_members: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> AdminusergroupsListChannelsGetResponsePydantic:
        raw_response = await self.raw.alist_channels_get(
            token=token,
            usergroup_id=usergroup_id,
            team_id=team_id,
            include_num_members=include_num_members,
            **kwargs,
        )
        if validate:
            return AdminusergroupsListChannelsGetResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminusergroupsListChannelsGetResponsePydantic, raw_response.body)
    
    
    def list_channels_get(
        self,
        token: str,
        usergroup_id: str,
        team_id: typing.Optional[str] = None,
        include_num_members: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> AdminusergroupsListChannelsGetResponsePydantic:
        raw_response = self.raw.list_channels_get(
            token=token,
            usergroup_id=usergroup_id,
            team_id=team_id,
            include_num_members=include_num_members,
        )
        if validate:
            return AdminusergroupsListChannelsGetResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminusergroupsListChannelsGetResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: str,
        usergroup_id: str,
        team_id: typing.Optional[str] = None,
        include_num_members: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_channels_get_mapped_args(
            token=token,
            usergroup_id=usergroup_id,
            team_id=team_id,
            include_num_members=include_num_members,
        )
        return await self._alist_channels_get_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        token: str,
        usergroup_id: str,
        team_id: typing.Optional[str] = None,
        include_num_members: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_channels_get_mapped_args(
            token=token,
            usergroup_id=usergroup_id,
            team_id=team_id,
            include_num_members=include_num_members,
        )
        return self._list_channels_get_oapg(
            query_params=args.query,
            header_params=args.header,
        )

