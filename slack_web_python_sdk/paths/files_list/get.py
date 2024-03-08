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

from slack_web_python_sdk.model.files_list_response import FilesListResponse as FilesListResponseSchema
from slack_web_python_sdk.model.files_listdefault_response import FilesListdefaultResponse as FilesListdefaultResponseSchema

from slack_web_python_sdk.type.files_listdefault_response import FilesListdefaultResponse
from slack_web_python_sdk.type.files_list_response import FilesListResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.files_listdefault_response import FilesListdefaultResponse as FilesListdefaultResponsePydantic
from slack_web_python_sdk.pydantic.files_list_response import FilesListResponse as FilesListResponsePydantic

from . import path

# Query params
TokenSchema = schemas.StrSchema
UserSchema = schemas.StrSchema
ChannelSchema = schemas.StrSchema
TsFromSchema = schemas.NumberSchema
TsToSchema = schemas.NumberSchema
TypesSchema = schemas.StrSchema
CountSchema = schemas.StrSchema
PageSchema = schemas.StrSchema
ShowFilesHiddenByLimitSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'token': typing.Union[TokenSchema, str, ],
        'user': typing.Union[UserSchema, str, ],
        'channel': typing.Union[ChannelSchema, str, ],
        'ts_from': typing.Union[TsFromSchema, decimal.Decimal, int, float, ],
        'ts_to': typing.Union[TsToSchema, decimal.Decimal, int, float, ],
        'types': typing.Union[TypesSchema, str, ],
        'count': typing.Union[CountSchema, str, ],
        'page': typing.Union[PageSchema, str, ],
        'show_files_hidden_by_limit': typing.Union[ShowFilesHiddenByLimitSchema, bool, ],
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
request_query_user = api_client.QueryParameter(
    name="user",
    style=api_client.ParameterStyle.FORM,
    schema=UserSchema,
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
request_query_types = api_client.QueryParameter(
    name="types",
    style=api_client.ParameterStyle.FORM,
    schema=TypesSchema,
    explode=True,
)
request_query_count = api_client.QueryParameter(
    name="count",
    style=api_client.ParameterStyle.FORM,
    schema=CountSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_show_files_hidden_by_limit = api_client.QueryParameter(
    name="show_files_hidden_by_limit",
    style=api_client.ParameterStyle.FORM,
    schema=ShowFilesHiddenByLimitSchema,
    explode=True,
)
_auth = [
    'slackAuth',
]
SchemaFor200ResponseBodyApplicationJson = FilesListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FilesListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FilesListResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = FilesListdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: FilesListdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: FilesListdefaultResponse


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
        user: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        types: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        show_files_hidden_by_limit: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if token is not None:
            _query_params["token"] = token
        if user is not None:
            _query_params["user"] = user
        if channel is not None:
            _query_params["channel"] = channel
        if ts_from is not None:
            _query_params["ts_from"] = ts_from
        if ts_to is not None:
            _query_params["ts_to"] = ts_to
        if types is not None:
            _query_params["types"] = types
        if count is not None:
            _query_params["count"] = count
        if page is not None:
            _query_params["page"] = page
        if show_files_hidden_by_limit is not None:
            _query_params["show_files_hidden_by_limit"] = show_files_hidden_by_limit
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
            request_query_user,
            request_query_channel,
            request_query_ts_from,
            request_query_ts_to,
            request_query_types,
            request_query_count,
            request_query_page,
            request_query_show_files_hidden_by_limit,
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
            path_template='/files.list',
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
            request_query_user,
            request_query_channel,
            request_query_ts_from,
            request_query_ts_to,
            request_query_types,
            request_query_count,
            request_query_page,
            request_query_show_files_hidden_by_limit,
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
            path_template='/files.list',
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
        user: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        types: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        show_files_hidden_by_limit: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            token=token,
            user=user,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            types=types,
            count=count,
            page=page,
            show_files_hidden_by_limit=show_files_hidden_by_limit,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        token: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        types: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        show_files_hidden_by_limit: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            token=token,
            user=user,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            types=types,
            count=count,
            page=page,
            show_files_hidden_by_limit=show_files_hidden_by_limit,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        token: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        types: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        show_files_hidden_by_limit: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> FilesListResponsePydantic:
        raw_response = await self.raw.alist(
            token=token,
            user=user,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            types=types,
            count=count,
            page=page,
            show_files_hidden_by_limit=show_files_hidden_by_limit,
            **kwargs,
        )
        if validate:
            return FilesListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesListResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        token: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        types: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        show_files_hidden_by_limit: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> FilesListResponsePydantic:
        raw_response = self.raw.list(
            token=token,
            user=user,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            types=types,
            count=count,
            page=page,
            show_files_hidden_by_limit=show_files_hidden_by_limit,
        )
        if validate:
            return FilesListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        types: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        show_files_hidden_by_limit: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            token=token,
            user=user,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            types=types,
            count=count,
            page=page,
            show_files_hidden_by_limit=show_files_hidden_by_limit,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        token: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        ts_from: typing.Optional[typing.Union[int, float]] = None,
        ts_to: typing.Optional[typing.Union[int, float]] = None,
        types: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        show_files_hidden_by_limit: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            token=token,
            user=user,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            types=types,
            count=count,
            page=page,
            show_files_hidden_by_limit=show_files_hidden_by_limit,
        )
        return self._list_oapg(
            query_params=args.query,
        )

