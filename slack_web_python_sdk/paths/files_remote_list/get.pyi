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

from slack_web_python_sdk.model.filesremote_list_remote_files_response import FilesremoteListRemoteFilesResponse as FilesremoteListRemoteFilesResponseSchema
from slack_web_python_sdk.model.filesremote_list_remote_filesdefault_response import FilesremoteListRemoteFilesdefaultResponse as FilesremoteListRemoteFilesdefaultResponseSchema

from slack_web_python_sdk.type.filesremote_list_remote_files_response import FilesremoteListRemoteFilesResponse
from slack_web_python_sdk.type.filesremote_list_remote_filesdefault_response import FilesremoteListRemoteFilesdefaultResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.filesremote_list_remote_files_response import FilesremoteListRemoteFilesResponse as FilesremoteListRemoteFilesResponsePydantic
from slack_web_python_sdk.pydantic.filesremote_list_remote_filesdefault_response import FilesremoteListRemoteFilesdefaultResponse as FilesremoteListRemoteFilesdefaultResponsePydantic

# Query params
TokenSchema = schemas.StrSchema
ChannelSchema = schemas.StrSchema
TsFromSchema = schemas.NumberSchema
TsToSchema = schemas.NumberSchema
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
        'ts_from': typing.Union[TsFromSchema, decimal.Decimal, int, float, ],
        'ts_to': typing.Union[TsToSchema, decimal.Decimal, int, float, ],
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
request_query_ts_from = api_client.QueryParameter(
    name="ts_from",
    style=api_client.ParameterStyle.FORM,
    schema=TsFromSchema,
    explode=True,
)
request_query_ts_to = api_client.QueryParameter(
    name="ts_to",
    style=api_client.ParameterStyle.FORM,
    schema=TsToSchema,
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
SchemaFor200ResponseBodyApplicationJson = FilesremoteListRemoteFilesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FilesremoteListRemoteFilesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FilesremoteListRemoteFilesResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = FilesremoteListRemoteFilesdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: FilesremoteListRemoteFilesdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: FilesremoteListRemoteFilesdefaultResponse


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

    def _list_remote_files_mapped_args(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if token is not None:
            _query_params["token"] = token
        if channel is not None:
            _query_params["channel"] = channel
        if ts_from is not None:
            _query_params["ts_from"] = ts_from
        if ts_to is not None:
            _query_params["ts_to"] = ts_to
        if limit is not None:
            _query_params["limit"] = limit
        if cursor is not None:
            _query_params["cursor"] = cursor
        args.query = _query_params
        return args

    async def _alist_remote_files_oapg(
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
            request_query_ts_from,
            request_query_ts_to,
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
            path_template='/files.remote.list',
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


    def _list_remote_files_oapg(
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
            request_query_ts_from,
            request_query_ts_to,
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
            path_template='/files.remote.list',
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


class ListRemoteFilesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_remote_files(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_remote_files_mapped_args(
            token=token,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            limit=limit,
            cursor=cursor,
        )
        return await self._alist_remote_files_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_remote_files(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_remote_files_mapped_args(
            token=token,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            limit=limit,
            cursor=cursor,
        )
        return self._list_remote_files_oapg(
            query_params=args.query,
        )

class ListRemoteFiles(BaseApi):

    async def alist_remote_files(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FilesremoteListRemoteFilesResponsePydantic:
        raw_response = await self.raw.alist_remote_files(
            token=token,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            limit=limit,
            cursor=cursor,
            **kwargs,
        )
        if validate:
            return FilesremoteListRemoteFilesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesremoteListRemoteFilesResponsePydantic, raw_response.body)
    
    
    def list_remote_files(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FilesremoteListRemoteFilesResponsePydantic:
        raw_response = self.raw.list_remote_files(
            token=token,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            limit=limit,
            cursor=cursor,
        )
        if validate:
            return FilesremoteListRemoteFilesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesremoteListRemoteFilesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_remote_files_mapped_args(
            token=token,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            limit=limit,
            cursor=cursor,
        )
        return await self._alist_remote_files_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        token: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_remote_files_mapped_args(
            token=token,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            limit=limit,
            cursor=cursor,
        )
        return self._list_remote_files_oapg(
            query_params=args.query,
        )

