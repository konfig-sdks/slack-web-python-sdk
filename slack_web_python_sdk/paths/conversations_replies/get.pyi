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

from slack_web_python_sdk.model.conversations_repliesdefault_response import ConversationsRepliesdefaultResponse as ConversationsRepliesdefaultResponseSchema
from slack_web_python_sdk.model.conversations_replies_response import ConversationsRepliesResponse as ConversationsRepliesResponseSchema

from slack_web_python_sdk.type.conversations_replies_response import ConversationsRepliesResponse
from slack_web_python_sdk.type.conversations_repliesdefault_response import ConversationsRepliesdefaultResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.conversations_repliesdefault_response import ConversationsRepliesdefaultResponse as ConversationsRepliesdefaultResponsePydantic
from slack_web_python_sdk.pydantic.conversations_replies_response import ConversationsRepliesResponse as ConversationsRepliesResponsePydantic

# Query params
TokenSchema = schemas.StrSchema
ChannelSchema = schemas.StrSchema
TsSchema = schemas.NumberSchema
LatestSchema = schemas.NumberSchema
OldestSchema = schemas.NumberSchema
InclusiveSchema = schemas.BoolSchema
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
        'channel': typing.Union[ChannelSchema, str, ],
        'ts': typing.Union[TsSchema, decimal.Decimal, int, float, ],
        'latest': typing.Union[LatestSchema, decimal.Decimal, int, float, ],
        'oldest': typing.Union[OldestSchema, decimal.Decimal, int, float, ],
        'inclusive': typing.Union[InclusiveSchema, bool, ],
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
request_query_channel = api_client.QueryParameter(
    name="channel",
    style=api_client.ParameterStyle.FORM,
    schema=ChannelSchema,
    explode=True,
)
request_query_ts = api_client.QueryParameter(
    name="ts",
    style=api_client.ParameterStyle.FORM,
    schema=TsSchema,
    explode=True,
)
request_query_latest = api_client.QueryParameter(
    name="latest",
    style=api_client.ParameterStyle.FORM,
    schema=LatestSchema,
    explode=True,
)
request_query_oldest = api_client.QueryParameter(
    name="oldest",
    style=api_client.ParameterStyle.FORM,
    schema=OldestSchema,
    explode=True,
)
request_query_inclusive = api_client.QueryParameter(
    name="inclusive",
    style=api_client.ParameterStyle.FORM,
    schema=InclusiveSchema,
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
SchemaFor200ResponseBodyApplicationJson = ConversationsRepliesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ConversationsRepliesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ConversationsRepliesResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ConversationsRepliesdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ConversationsRepliesdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ConversationsRepliesdefaultResponse


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

    def _replies_mapped_args(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts: typing.Optional[typing.Union[int, float]] = None,
        latest: typing.Optional[typing.Union[int, float]] = None,
        oldest: typing.Optional[typing.Union[int, float]] = None,
        inclusive: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if token is not None:
            _query_params["token"] = token
        if channel is not None:
            _query_params["channel"] = channel
        if ts is not None:
            _query_params["ts"] = ts
        if latest is not None:
            _query_params["latest"] = latest
        if oldest is not None:
            _query_params["oldest"] = oldest
        if inclusive is not None:
            _query_params["inclusive"] = inclusive
        if limit is not None:
            _query_params["limit"] = limit
        if cursor is not None:
            _query_params["cursor"] = cursor
        args.query = _query_params
        return args

    async def _areplies_oapg(
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
            request_query_channel,
            request_query_ts,
            request_query_latest,
            request_query_oldest,
            request_query_inclusive,
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
            path_template='/conversations.replies',
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


    def _replies_oapg(
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
            request_query_channel,
            request_query_ts,
            request_query_latest,
            request_query_oldest,
            request_query_inclusive,
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
            path_template='/conversations.replies',
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


class RepliesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def areplies(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts: typing.Optional[typing.Union[int, float]] = None,
        latest: typing.Optional[typing.Union[int, float]] = None,
        oldest: typing.Optional[typing.Union[int, float]] = None,
        inclusive: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._replies_mapped_args(
            token=token,
            channel=channel,
            ts=ts,
            latest=latest,
            oldest=oldest,
            inclusive=inclusive,
            limit=limit,
            cursor=cursor,
        )
        return await self._areplies_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def replies(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts: typing.Optional[typing.Union[int, float]] = None,
        latest: typing.Optional[typing.Union[int, float]] = None,
        oldest: typing.Optional[typing.Union[int, float]] = None,
        inclusive: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._replies_mapped_args(
            token=token,
            channel=channel,
            ts=ts,
            latest=latest,
            oldest=oldest,
            inclusive=inclusive,
            limit=limit,
            cursor=cursor,
        )
        return self._replies_oapg(
            query_params=args.query,
        )

class Replies(BaseApi):

    async def areplies(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts: typing.Optional[typing.Union[int, float]] = None,
        latest: typing.Optional[typing.Union[int, float]] = None,
        oldest: typing.Optional[typing.Union[int, float]] = None,
        inclusive: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConversationsRepliesResponsePydantic:
        raw_response = await self.raw.areplies(
            token=token,
            channel=channel,
            ts=ts,
            latest=latest,
            oldest=oldest,
            inclusive=inclusive,
            limit=limit,
            cursor=cursor,
            **kwargs,
        )
        if validate:
            return ConversationsRepliesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ConversationsRepliesResponsePydantic, raw_response.body)
    
    
    def replies(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts: typing.Optional[typing.Union[int, float]] = None,
        latest: typing.Optional[typing.Union[int, float]] = None,
        oldest: typing.Optional[typing.Union[int, float]] = None,
        inclusive: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ConversationsRepliesResponsePydantic:
        raw_response = self.raw.replies(
            token=token,
            channel=channel,
            ts=ts,
            latest=latest,
            oldest=oldest,
            inclusive=inclusive,
            limit=limit,
            cursor=cursor,
        )
        if validate:
            return ConversationsRepliesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ConversationsRepliesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts: typing.Optional[typing.Union[int, float]] = None,
        latest: typing.Optional[typing.Union[int, float]] = None,
        oldest: typing.Optional[typing.Union[int, float]] = None,
        inclusive: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._replies_mapped_args(
            token=token,
            channel=channel,
            ts=ts,
            latest=latest,
            oldest=oldest,
            inclusive=inclusive,
            limit=limit,
            cursor=cursor,
        )
        return await self._areplies_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts: typing.Optional[typing.Union[int, float]] = None,
        latest: typing.Optional[typing.Union[int, float]] = None,
        oldest: typing.Optional[typing.Union[int, float]] = None,
        inclusive: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._replies_mapped_args(
            token=token,
            channel=channel,
            ts=ts,
            latest=latest,
            oldest=oldest,
            inclusive=inclusive,
            limit=limit,
            cursor=cursor,
        )
        return self._replies_oapg(
            query_params=args.query,
        )

