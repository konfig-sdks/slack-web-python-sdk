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

from slack_web_python_sdk.model.rtm_connect_response import RtmConnectResponse as RtmConnectResponseSchema
from slack_web_python_sdk.model.rtm_connectdefault_response import RtmConnectdefaultResponse as RtmConnectdefaultResponseSchema

from slack_web_python_sdk.type.rtm_connect_response import RtmConnectResponse
from slack_web_python_sdk.type.rtm_connectdefault_response import RtmConnectdefaultResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.rtm_connectdefault_response import RtmConnectdefaultResponse as RtmConnectdefaultResponsePydantic
from slack_web_python_sdk.pydantic.rtm_connect_response import RtmConnectResponse as RtmConnectResponsePydantic

from . import path

# Query params
TokenSchema = schemas.StrSchema
BatchPresenceAwareSchema = schemas.BoolSchema
PresenceSubSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'token': typing.Union[TokenSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'batch_presence_aware': typing.Union[BatchPresenceAwareSchema, bool, ],
        'presence_sub': typing.Union[PresenceSubSchema, bool, ],
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
request_query_batch_presence_aware = api_client.QueryParameter(
    name="batch_presence_aware",
    style=api_client.ParameterStyle.FORM,
    schema=BatchPresenceAwareSchema,
    explode=True,
)
request_query_presence_sub = api_client.QueryParameter(
    name="presence_sub",
    style=api_client.ParameterStyle.FORM,
    schema=PresenceSubSchema,
    explode=True,
)
_auth = [
    'slackAuth',
]
SchemaFor200ResponseBodyApplicationJson = RtmConnectResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RtmConnectResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RtmConnectResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = RtmConnectdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: RtmConnectdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: RtmConnectdefaultResponse


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

    def _connect_mapped_args(
        self,
        token: str,
        batch_presence_aware: typing.Optional[bool] = None,
        presence_sub: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if token is not None:
            _query_params["token"] = token
        if batch_presence_aware is not None:
            _query_params["batch_presence_aware"] = batch_presence_aware
        if presence_sub is not None:
            _query_params["presence_sub"] = presence_sub
        args.query = _query_params
        return args

    async def _aconnect_oapg(
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
            request_query_batch_presence_aware,
            request_query_presence_sub,
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
            path_template='/rtm.connect',
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


    def _connect_oapg(
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
            request_query_batch_presence_aware,
            request_query_presence_sub,
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
            path_template='/rtm.connect',
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


class ConnectRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aconnect(
        self,
        token: str,
        batch_presence_aware: typing.Optional[bool] = None,
        presence_sub: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._connect_mapped_args(
            token=token,
            batch_presence_aware=batch_presence_aware,
            presence_sub=presence_sub,
        )
        return await self._aconnect_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def connect(
        self,
        token: str,
        batch_presence_aware: typing.Optional[bool] = None,
        presence_sub: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._connect_mapped_args(
            token=token,
            batch_presence_aware=batch_presence_aware,
            presence_sub=presence_sub,
        )
        return self._connect_oapg(
            query_params=args.query,
        )

class Connect(BaseApi):

    async def aconnect(
        self,
        token: str,
        batch_presence_aware: typing.Optional[bool] = None,
        presence_sub: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> RtmConnectResponsePydantic:
        raw_response = await self.raw.aconnect(
            token=token,
            batch_presence_aware=batch_presence_aware,
            presence_sub=presence_sub,
            **kwargs,
        )
        if validate:
            return RtmConnectResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RtmConnectResponsePydantic, raw_response.body)
    
    
    def connect(
        self,
        token: str,
        batch_presence_aware: typing.Optional[bool] = None,
        presence_sub: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> RtmConnectResponsePydantic:
        raw_response = self.raw.connect(
            token=token,
            batch_presence_aware=batch_presence_aware,
            presence_sub=presence_sub,
        )
        if validate:
            return RtmConnectResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RtmConnectResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: str,
        batch_presence_aware: typing.Optional[bool] = None,
        presence_sub: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._connect_mapped_args(
            token=token,
            batch_presence_aware=batch_presence_aware,
            presence_sub=presence_sub,
        )
        return await self._aconnect_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        token: str,
        batch_presence_aware: typing.Optional[bool] = None,
        presence_sub: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._connect_mapped_args(
            token=token,
            batch_presence_aware=batch_presence_aware,
            presence_sub=presence_sub,
        )
        return self._connect_oapg(
            query_params=args.query,
        )

