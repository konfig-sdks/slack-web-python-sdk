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

from slack_web_python_sdk.model.adminconversations_search_channelsdefault_response import AdminconversationsSearchChannelsdefaultResponse as AdminconversationsSearchChannelsdefaultResponseSchema
from slack_web_python_sdk.model.adminconversations_search_channels_response import AdminconversationsSearchChannelsResponse as AdminconversationsSearchChannelsResponseSchema

from slack_web_python_sdk.type.adminconversations_search_channelsdefault_response import AdminconversationsSearchChannelsdefaultResponse
from slack_web_python_sdk.type.adminconversations_search_channels_response import AdminconversationsSearchChannelsResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.adminconversations_search_channels_response import AdminconversationsSearchChannelsResponse as AdminconversationsSearchChannelsResponsePydantic
from slack_web_python_sdk.pydantic.adminconversations_search_channelsdefault_response import AdminconversationsSearchChannelsdefaultResponse as AdminconversationsSearchChannelsdefaultResponsePydantic

# Query params
TeamIdsSchema = schemas.StrSchema
QuerySchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
CursorSchema = schemas.StrSchema
SearchChannelTypesSchema = schemas.StrSchema
SortSchema = schemas.StrSchema
SortDirSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'team_ids': typing.Union[TeamIdsSchema, str, ],
        'query': typing.Union[QuerySchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'cursor': typing.Union[CursorSchema, str, ],
        'search_channel_types': typing.Union[SearchChannelTypesSchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
        'sort_dir': typing.Union[SortDirSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_team_ids = api_client.QueryParameter(
    name="team_ids",
    style=api_client.ParameterStyle.FORM,
    schema=TeamIdsSchema,
    explode=True,
)
request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_cursor = api_client.QueryParameter(
    name="cursor",
    style=api_client.ParameterStyle.FORM,
    schema=CursorSchema,
    explode=True,
)
request_query_search_channel_types = api_client.QueryParameter(
    name="search_channel_types",
    style=api_client.ParameterStyle.FORM,
    schema=SearchChannelTypesSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_sort_dir = api_client.QueryParameter(
    name="sort_dir",
    style=api_client.ParameterStyle.FORM,
    schema=SortDirSchema,
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
SchemaFor200ResponseBodyApplicationJson = AdminconversationsSearchChannelsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AdminconversationsSearchChannelsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AdminconversationsSearchChannelsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = AdminconversationsSearchChannelsdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: AdminconversationsSearchChannelsdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: AdminconversationsSearchChannelsdefaultResponse


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

    def _search_channels_mapped_args(
        self,
        token: str,
        team_ids: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        search_channel_types: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if team_ids is not None:
            _query_params["team_ids"] = team_ids
        if query is not None:
            _query_params["query"] = query
        if limit is not None:
            _query_params["limit"] = limit
        if cursor is not None:
            _query_params["cursor"] = cursor
        if search_channel_types is not None:
            _query_params["search_channel_types"] = search_channel_types
        if sort is not None:
            _query_params["sort"] = sort
        if sort_dir is not None:
            _query_params["sort_dir"] = sort_dir
        if token is not None:
            _header_params["token"] = token
        args.query = _query_params
        args.header = _header_params
        return args

    async def _asearch_channels_oapg(
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
            request_query_team_ids,
            request_query_query,
            request_query_limit,
            request_query_cursor,
            request_query_search_channel_types,
            request_query_sort,
            request_query_sort_dir,
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
            path_template='/admin.conversations.search',
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


    def _search_channels_oapg(
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
            request_query_team_ids,
            request_query_query,
            request_query_limit,
            request_query_cursor,
            request_query_search_channel_types,
            request_query_sort,
            request_query_sort_dir,
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
            path_template='/admin.conversations.search',
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


class SearchChannelsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_channels(
        self,
        token: str,
        team_ids: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        search_channel_types: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_channels_mapped_args(
            token=token,
            team_ids=team_ids,
            query=query,
            limit=limit,
            cursor=cursor,
            search_channel_types=search_channel_types,
            sort=sort,
            sort_dir=sort_dir,
        )
        return await self._asearch_channels_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def search_channels(
        self,
        token: str,
        team_ids: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        search_channel_types: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_channels_mapped_args(
            token=token,
            team_ids=team_ids,
            query=query,
            limit=limit,
            cursor=cursor,
            search_channel_types=search_channel_types,
            sort=sort,
            sort_dir=sort_dir,
        )
        return self._search_channels_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class SearchChannels(BaseApi):

    async def asearch_channels(
        self,
        token: str,
        team_ids: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        search_channel_types: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AdminconversationsSearchChannelsResponsePydantic:
        raw_response = await self.raw.asearch_channels(
            token=token,
            team_ids=team_ids,
            query=query,
            limit=limit,
            cursor=cursor,
            search_channel_types=search_channel_types,
            sort=sort,
            sort_dir=sort_dir,
            **kwargs,
        )
        if validate:
            return AdminconversationsSearchChannelsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminconversationsSearchChannelsResponsePydantic, raw_response.body)
    
    
    def search_channels(
        self,
        token: str,
        team_ids: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        search_channel_types: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AdminconversationsSearchChannelsResponsePydantic:
        raw_response = self.raw.search_channels(
            token=token,
            team_ids=team_ids,
            query=query,
            limit=limit,
            cursor=cursor,
            search_channel_types=search_channel_types,
            sort=sort,
            sort_dir=sort_dir,
        )
        if validate:
            return AdminconversationsSearchChannelsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminconversationsSearchChannelsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: str,
        team_ids: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        search_channel_types: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_channels_mapped_args(
            token=token,
            team_ids=team_ids,
            query=query,
            limit=limit,
            cursor=cursor,
            search_channel_types=search_channel_types,
            sort=sort,
            sort_dir=sort_dir,
        )
        return await self._asearch_channels_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        token: str,
        team_ids: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        search_channel_types: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_channels_mapped_args(
            token=token,
            team_ids=team_ids,
            query=query,
            limit=limit,
            cursor=cursor,
            search_channel_types=search_channel_types,
            sort=sort,
            sort_dir=sort_dir,
        )
        return self._search_channels_oapg(
            query_params=args.query,
            header_params=args.header,
        )

