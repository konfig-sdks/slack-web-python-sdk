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

from slack_web_python_sdk.model.calls_adddefault_response import CallsAdddefaultResponse as CallsAdddefaultResponseSchema
from slack_web_python_sdk.model.calls_add_request import CallsAddRequest as CallsAddRequestSchema
from slack_web_python_sdk.model.calls_add_response import CallsAddResponse as CallsAddResponseSchema

from slack_web_python_sdk.type.calls_adddefault_response import CallsAdddefaultResponse
from slack_web_python_sdk.type.calls_add_request import CallsAddRequest
from slack_web_python_sdk.type.calls_add_response import CallsAddResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.calls_adddefault_response import CallsAdddefaultResponse as CallsAdddefaultResponsePydantic
from slack_web_python_sdk.pydantic.calls_add_request import CallsAddRequest as CallsAddRequestPydantic
from slack_web_python_sdk.pydantic.calls_add_response import CallsAddResponse as CallsAddResponsePydantic

from . import path

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
# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = CallsAddRequestSchema


request_body_calls_add_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
_auth = [
    'slackAuth',
]
SchemaFor200ResponseBodyApplicationJson = CallsAddResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CallsAddResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CallsAddResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = CallsAdddefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: CallsAdddefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: CallsAdddefaultResponse


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

    def _add_mapped_args(
        self,
        token: str,
        external_unique_id: str,
        join_url: str,
        title: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        date_start: typing.Optional[int] = None,
        desktop_app_join_url: typing.Optional[str] = None,
        external_display_id: typing.Optional[str] = None,
        users: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if created_by is not None:
            _body["created_by"] = created_by
        if date_start is not None:
            _body["date_start"] = date_start
        if desktop_app_join_url is not None:
            _body["desktop_app_join_url"] = desktop_app_join_url
        if external_display_id is not None:
            _body["external_display_id"] = external_display_id
        if external_unique_id is not None:
            _body["external_unique_id"] = external_unique_id
        if join_url is not None:
            _body["join_url"] = join_url
        if users is not None:
            _body["users"] = users
        args.body = _body
        if token is not None:
            _header_params["token"] = token
        args.header = _header_params
        return args

    async def _aadd_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
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
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/calls.add',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_calls_add_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _add_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
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
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/calls.add',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_calls_add_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class AddRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd(
        self,
        token: str,
        external_unique_id: str,
        join_url: str,
        title: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        date_start: typing.Optional[int] = None,
        desktop_app_join_url: typing.Optional[str] = None,
        external_display_id: typing.Optional[str] = None,
        users: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_mapped_args(
            token=token,
            external_unique_id=external_unique_id,
            join_url=join_url,
            title=title,
            created_by=created_by,
            date_start=date_start,
            desktop_app_join_url=desktop_app_join_url,
            external_display_id=external_display_id,
            users=users,
        )
        return await self._aadd_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def add(
        self,
        token: str,
        external_unique_id: str,
        join_url: str,
        title: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        date_start: typing.Optional[int] = None,
        desktop_app_join_url: typing.Optional[str] = None,
        external_display_id: typing.Optional[str] = None,
        users: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_mapped_args(
            token=token,
            external_unique_id=external_unique_id,
            join_url=join_url,
            title=title,
            created_by=created_by,
            date_start=date_start,
            desktop_app_join_url=desktop_app_join_url,
            external_display_id=external_display_id,
            users=users,
        )
        return self._add_oapg(
            body=args.body,
            header_params=args.header,
        )

class Add(BaseApi):

    async def aadd(
        self,
        token: str,
        external_unique_id: str,
        join_url: str,
        title: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        date_start: typing.Optional[int] = None,
        desktop_app_join_url: typing.Optional[str] = None,
        external_display_id: typing.Optional[str] = None,
        users: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CallsAddResponsePydantic:
        raw_response = await self.raw.aadd(
            token=token,
            external_unique_id=external_unique_id,
            join_url=join_url,
            title=title,
            created_by=created_by,
            date_start=date_start,
            desktop_app_join_url=desktop_app_join_url,
            external_display_id=external_display_id,
            users=users,
            **kwargs,
        )
        if validate:
            return CallsAddResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CallsAddResponsePydantic, raw_response.body)
    
    
    def add(
        self,
        token: str,
        external_unique_id: str,
        join_url: str,
        title: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        date_start: typing.Optional[int] = None,
        desktop_app_join_url: typing.Optional[str] = None,
        external_display_id: typing.Optional[str] = None,
        users: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CallsAddResponsePydantic:
        raw_response = self.raw.add(
            token=token,
            external_unique_id=external_unique_id,
            join_url=join_url,
            title=title,
            created_by=created_by,
            date_start=date_start,
            desktop_app_join_url=desktop_app_join_url,
            external_display_id=external_display_id,
            users=users,
        )
        if validate:
            return CallsAddResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CallsAddResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        token: str,
        external_unique_id: str,
        join_url: str,
        title: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        date_start: typing.Optional[int] = None,
        desktop_app_join_url: typing.Optional[str] = None,
        external_display_id: typing.Optional[str] = None,
        users: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_mapped_args(
            token=token,
            external_unique_id=external_unique_id,
            join_url=join_url,
            title=title,
            created_by=created_by,
            date_start=date_start,
            desktop_app_join_url=desktop_app_join_url,
            external_display_id=external_display_id,
            users=users,
        )
        return await self._aadd_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        token: str,
        external_unique_id: str,
        join_url: str,
        title: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        date_start: typing.Optional[int] = None,
        desktop_app_join_url: typing.Optional[str] = None,
        external_display_id: typing.Optional[str] = None,
        users: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_mapped_args(
            token=token,
            external_unique_id=external_unique_id,
            join_url=join_url,
            title=title,
            created_by=created_by,
            date_start=date_start,
            desktop_app_join_url=desktop_app_join_url,
            external_display_id=external_display_id,
            users=users,
        )
        return self._add_oapg(
            body=args.body,
            header_params=args.header,
        )

