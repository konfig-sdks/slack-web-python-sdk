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

from slack_web_python_sdk.model.conversations_listdefault_response import ConversationsListdefaultResponse as ConversationsListdefaultResponseSchema
from slack_web_python_sdk.model.conversations_list_response import ConversationsListResponse as ConversationsListResponseSchema

from slack_web_python_sdk.type.conversations_list_response import ConversationsListResponse
from slack_web_python_sdk.type.conversations_listdefault_response import ConversationsListdefaultResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.conversations_listdefault_response import ConversationsListdefaultResponse as ConversationsListdefaultResponsePydantic
from slack_web_python_sdk.pydantic.conversations_list_response import ConversationsListResponse as ConversationsListResponsePydantic

from . import path

# Query params
TokenSchema = schemas.StrSchema
ExcludeArchivedSchema = schemas.BoolSchema
TypesSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
CursorSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'token': typing.Union[TokenSchema, str, ],
        'exclude_archived': typing.Union[ExcludeArchivedSchema, bool, ],
        'types': typing.Union[TypesSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'cursor': typing.Union[CursorSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_token = api_client.QueryParameter(
    name="token",
    style=api_client.ParameterStyle.FORM,
    schema=TokenSchema,
    explode=True,
)
request_query_exclude_archived = api_client.QueryParameter(
    name="exclude_archived",
    style=api_client.ParameterStyle.FORM,
    schema=ExcludeArchivedSchema,
    explode=True,
)
request_query_types = api_client.QueryParameter(
    name="types",
    style=api_client.ParameterStyle.FORM,
    schema=TypesSchema,
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
_auth = [
    'slackAuth',
]
SchemaFor200ResponseBodyApplicationJson = ConversationsListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ConversationsListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ConversationsListResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ConversationsListdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ConversationsListdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ConversationsListdefaultResponse


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_mapped_args(
        self,
        token: typing.Optional[str] = None,
        exclude_archived: typing.Optional[bool] = None,
        types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if token is not None:
            _query_params["token"] = token
        if exclude_archived is not None:
            _query_params["exclude_archived"] = exclude_archived
        if types is not None:
            _query_params["types"] = types
        if limit is not None:
            _query_params["limit"] = limit
        if cursor is not None:
            _query_params["cursor"] = cursor
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
            request_query_token,
            request_query_exclude_archived,
            request_query_types,
            request_query_limit,
            request_query_cursor,
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
            path_template='/conversations.list',
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
            request_query_token,
            request_query_exclude_archived,
            request_query_types,
            request_query_limit,
            request_query_cursor,
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
            path_template='/conversations.list',
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
        token: typing.Optional[str] = None,
        exclude_archived: typing.Optional[bool] = None,
        types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            token=token,
            exclude_archived=exclude_archived,
            types=types,
            limit=limit,
            cursor=cursor,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        token: typing.Optional[str] = None,
        exclude_archived: typing.Optional[bool] = None,
        types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            token=token,
            exclude_archived=exclude_archived,
            types=types,
            limit=limit,
            cursor=cursor,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        token: typing.Optional[str] = None,
        exclude_archived: typing.Optional[bool] = None,
        types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConversationsListResponsePydantic:
        raw_response = await self.raw.alist(
            token=token,
            exclude_archived=exclude_archived,
            types=types,
            limit=limit,
            cursor=cursor,
            **kwargs,
        )
        if validate:
            return ConversationsListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ConversationsListResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        token: typing.Optional[str] = None,
        exclude_archived: typing.Optional[bool] = None,
        types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ConversationsListResponsePydantic:
        raw_response = self.raw.list(
            token=token,
            exclude_archived=exclude_archived,
            types=types,
            limit=limit,
            cursor=cursor,
        )
        if validate:
            return ConversationsListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ConversationsListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: typing.Optional[str] = None,
        exclude_archived: typing.Optional[bool] = None,
        types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            token=token,
            exclude_archived=exclude_archived,
            types=types,
            limit=limit,
            cursor=cursor,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        token: typing.Optional[str] = None,
        exclude_archived: typing.Optional[bool] = None,
        types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            token=token,
            exclude_archived=exclude_archived,
            types=types,
            limit=limit,
            cursor=cursor,
        )
        return self._list_oapg(
            query_params=args.query,
        )

