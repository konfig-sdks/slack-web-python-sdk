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

from slack_web_python_sdk.model.adminapps_approve_app_installation_request import AdminappsApproveAppInstallationRequest as AdminappsApproveAppInstallationRequestSchema
from slack_web_python_sdk.model.adminapps_approve_app_installationdefault_response import AdminappsApproveAppInstallationdefaultResponse as AdminappsApproveAppInstallationdefaultResponseSchema
from slack_web_python_sdk.model.adminapps_approve_app_installation_response import AdminappsApproveAppInstallationResponse as AdminappsApproveAppInstallationResponseSchema

from slack_web_python_sdk.type.adminapps_approve_app_installationdefault_response import AdminappsApproveAppInstallationdefaultResponse
from slack_web_python_sdk.type.adminapps_approve_app_installation_response import AdminappsApproveAppInstallationResponse
from slack_web_python_sdk.type.adminapps_approve_app_installation_request import AdminappsApproveAppInstallationRequest

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.adminapps_approve_app_installation_response import AdminappsApproveAppInstallationResponse as AdminappsApproveAppInstallationResponsePydantic
from slack_web_python_sdk.pydantic.adminapps_approve_app_installationdefault_response import AdminappsApproveAppInstallationdefaultResponse as AdminappsApproveAppInstallationdefaultResponsePydantic
from slack_web_python_sdk.pydantic.adminapps_approve_app_installation_request import AdminappsApproveAppInstallationRequest as AdminappsApproveAppInstallationRequestPydantic

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
SchemaForRequestBodyApplicationXWwwFormUrlencoded = AdminappsApproveAppInstallationRequestSchema


request_body_adminapps_approve_app_installation_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
)
SchemaFor200ResponseBodyApplicationJson = AdminappsApproveAppInstallationResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AdminappsApproveAppInstallationResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AdminappsApproveAppInstallationResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = AdminappsApproveAppInstallationdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: AdminappsApproveAppInstallationdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: AdminappsApproveAppInstallationdefaultResponse


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

    def _approve_app_installation_mapped_args(
        self,
        token: str,
        app_id: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if app_id is not None:
            _body["app_id"] = app_id
        if request_id is not None:
            _body["request_id"] = request_id
        if team_id is not None:
            _body["team_id"] = team_id
        args.body = _body
        if token is not None:
            _header_params["token"] = token
        args.header = _header_params
        return args

    async def _aapprove_app_installation_oapg(
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/admin.apps.approve',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_adminapps_approve_app_installation_request.serialize(body, content_type)
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


    def _approve_app_installation_oapg(
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/admin.apps.approve',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_adminapps_approve_app_installation_request.serialize(body, content_type)
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


class ApproveAppInstallationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aapprove_app_installation(
        self,
        token: str,
        app_id: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._approve_app_installation_mapped_args(
            token=token,
            app_id=app_id,
            request_id=request_id,
            team_id=team_id,
        )
        return await self._aapprove_app_installation_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def approve_app_installation(
        self,
        token: str,
        app_id: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._approve_app_installation_mapped_args(
            token=token,
            app_id=app_id,
            request_id=request_id,
            team_id=team_id,
        )
        return self._approve_app_installation_oapg(
            body=args.body,
            header_params=args.header,
        )

class ApproveAppInstallation(BaseApi):

    async def aapprove_app_installation(
        self,
        token: str,
        app_id: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AdminappsApproveAppInstallationResponsePydantic:
        raw_response = await self.raw.aapprove_app_installation(
            token=token,
            app_id=app_id,
            request_id=request_id,
            team_id=team_id,
            **kwargs,
        )
        if validate:
            return AdminappsApproveAppInstallationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminappsApproveAppInstallationResponsePydantic, raw_response.body)
    
    
    def approve_app_installation(
        self,
        token: str,
        app_id: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AdminappsApproveAppInstallationResponsePydantic:
        raw_response = self.raw.approve_app_installation(
            token=token,
            app_id=app_id,
            request_id=request_id,
            team_id=team_id,
        )
        if validate:
            return AdminappsApproveAppInstallationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminappsApproveAppInstallationResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        token: str,
        app_id: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._approve_app_installation_mapped_args(
            token=token,
            app_id=app_id,
            request_id=request_id,
            team_id=team_id,
        )
        return await self._aapprove_app_installation_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        token: str,
        app_id: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._approve_app_installation_mapped_args(
            token=token,
            app_id=app_id,
            request_id=request_id,
            team_id=team_id,
        )
        return self._approve_app_installation_oapg(
            body=args.body,
            header_params=args.header,
        )

