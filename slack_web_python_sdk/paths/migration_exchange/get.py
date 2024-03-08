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

from slack_web_python_sdk.model.migration_exchange_response import MigrationExchangeResponse as MigrationExchangeResponseSchema
from slack_web_python_sdk.model.migration_exchangedefault_response import MigrationExchangedefaultResponse as MigrationExchangedefaultResponseSchema

from slack_web_python_sdk.type.migration_exchangedefault_response import MigrationExchangedefaultResponse
from slack_web_python_sdk.type.migration_exchange_response import MigrationExchangeResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.migration_exchange_response import MigrationExchangeResponse as MigrationExchangeResponsePydantic
from slack_web_python_sdk.pydantic.migration_exchangedefault_response import MigrationExchangedefaultResponse as MigrationExchangedefaultResponsePydantic

from . import path

# Query params
TokenSchema = schemas.StrSchema
UsersSchema = schemas.StrSchema
TeamIdSchema = schemas.StrSchema
ToOldSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'token': typing.Union[TokenSchema, str, ],
        'users': typing.Union[UsersSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'team_id': typing.Union[TeamIdSchema, str, ],
        'to_old': typing.Union[ToOldSchema, bool, ],
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
request_query_users = api_client.QueryParameter(
    name="users",
    style=api_client.ParameterStyle.FORM,
    schema=UsersSchema,
    required=True,
    explode=True,
)
request_query_team_id = api_client.QueryParameter(
    name="team_id",
    style=api_client.ParameterStyle.FORM,
    schema=TeamIdSchema,
    explode=True,
)
request_query_to_old = api_client.QueryParameter(
    name="to_old",
    style=api_client.ParameterStyle.FORM,
    schema=ToOldSchema,
    explode=True,
)
_auth = [
    'slackAuth',
]
SchemaFor200ResponseBodyApplicationJson = MigrationExchangeResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: MigrationExchangeResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: MigrationExchangeResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = MigrationExchangedefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: MigrationExchangedefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: MigrationExchangedefaultResponse


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

    def _exchange_mapped_args(
        self,
        token: str,
        users: str,
        team_id: typing.Optional[str] = None,
        to_old: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if token is not None:
            _query_params["token"] = token
        if users is not None:
            _query_params["users"] = users
        if team_id is not None:
            _query_params["team_id"] = team_id
        if to_old is not None:
            _query_params["to_old"] = to_old
        args.query = _query_params
        return args

    async def _aexchange_oapg(
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
            request_query_users,
            request_query_team_id,
            request_query_to_old,
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
            path_template='/migration.exchange',
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


    def _exchange_oapg(
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
            request_query_users,
            request_query_team_id,
            request_query_to_old,
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
            path_template='/migration.exchange',
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


class ExchangeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aexchange(
        self,
        token: str,
        users: str,
        team_id: typing.Optional[str] = None,
        to_old: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._exchange_mapped_args(
            token=token,
            users=users,
            team_id=team_id,
            to_old=to_old,
        )
        return await self._aexchange_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def exchange(
        self,
        token: str,
        users: str,
        team_id: typing.Optional[str] = None,
        to_old: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._exchange_mapped_args(
            token=token,
            users=users,
            team_id=team_id,
            to_old=to_old,
        )
        return self._exchange_oapg(
            query_params=args.query,
        )

class Exchange(BaseApi):

    async def aexchange(
        self,
        token: str,
        users: str,
        team_id: typing.Optional[str] = None,
        to_old: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> MigrationExchangeResponsePydantic:
        raw_response = await self.raw.aexchange(
            token=token,
            users=users,
            team_id=team_id,
            to_old=to_old,
            **kwargs,
        )
        if validate:
            return MigrationExchangeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MigrationExchangeResponsePydantic, raw_response.body)
    
    
    def exchange(
        self,
        token: str,
        users: str,
        team_id: typing.Optional[str] = None,
        to_old: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> MigrationExchangeResponsePydantic:
        raw_response = self.raw.exchange(
            token=token,
            users=users,
            team_id=team_id,
            to_old=to_old,
        )
        if validate:
            return MigrationExchangeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MigrationExchangeResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: str,
        users: str,
        team_id: typing.Optional[str] = None,
        to_old: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._exchange_mapped_args(
            token=token,
            users=users,
            team_id=team_id,
            to_old=to_old,
        )
        return await self._aexchange_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        token: str,
        users: str,
        team_id: typing.Optional[str] = None,
        to_old: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._exchange_mapped_args(
            token=token,
            users=users,
            team_id=team_id,
            to_old=to_old,
        )
        return self._exchange_oapg(
            query_params=args.query,
        )

