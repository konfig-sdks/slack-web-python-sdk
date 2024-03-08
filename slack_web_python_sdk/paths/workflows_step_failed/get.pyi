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

from slack_web_python_sdk.model.workflows_step_failed_response import WorkflowsStepFailedResponse as WorkflowsStepFailedResponseSchema
from slack_web_python_sdk.model.workflows_step_faileddefault_response import WorkflowsStepFaileddefaultResponse as WorkflowsStepFaileddefaultResponseSchema

from slack_web_python_sdk.type.workflows_step_failed_response import WorkflowsStepFailedResponse
from slack_web_python_sdk.type.workflows_step_faileddefault_response import WorkflowsStepFaileddefaultResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.workflows_step_failed_response import WorkflowsStepFailedResponse as WorkflowsStepFailedResponsePydantic
from slack_web_python_sdk.pydantic.workflows_step_faileddefault_response import WorkflowsStepFaileddefaultResponse as WorkflowsStepFaileddefaultResponsePydantic

# Query params
WorkflowStepExecuteIdSchema = schemas.StrSchema
ErrorSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'workflow_step_execute_id': typing.Union[WorkflowStepExecuteIdSchema, str, ],
        'error': typing.Union[ErrorSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_workflow_step_execute_id = api_client.QueryParameter(
    name="workflow_step_execute_id",
    style=api_client.ParameterStyle.FORM,
    schema=WorkflowStepExecuteIdSchema,
    required=True,
    explode=True,
)
request_query_error = api_client.QueryParameter(
    name="error",
    style=api_client.ParameterStyle.FORM,
    schema=ErrorSchema,
    required=True,
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
SchemaFor200ResponseBodyApplicationJson = WorkflowsStepFailedResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: WorkflowsStepFailedResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: WorkflowsStepFailedResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = WorkflowsStepFaileddefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: WorkflowsStepFaileddefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: WorkflowsStepFaileddefaultResponse


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

    def _step_failed_mapped_args(
        self,
        token: str,
        workflow_step_execute_id: str,
        error: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if workflow_step_execute_id is not None:
            _query_params["workflow_step_execute_id"] = workflow_step_execute_id
        if error is not None:
            _query_params["error"] = error
        if token is not None:
            _header_params["token"] = token
        args.query = _query_params
        args.header = _header_params
        return args

    async def _astep_failed_oapg(
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
            request_query_workflow_step_execute_id,
            request_query_error,
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
            path_template='/workflows.stepFailed',
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


    def _step_failed_oapg(
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
            request_query_workflow_step_execute_id,
            request_query_error,
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
            path_template='/workflows.stepFailed',
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


class StepFailedRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def astep_failed(
        self,
        token: str,
        workflow_step_execute_id: str,
        error: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._step_failed_mapped_args(
            token=token,
            workflow_step_execute_id=workflow_step_execute_id,
            error=error,
        )
        return await self._astep_failed_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def step_failed(
        self,
        token: str,
        workflow_step_execute_id: str,
        error: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._step_failed_mapped_args(
            token=token,
            workflow_step_execute_id=workflow_step_execute_id,
            error=error,
        )
        return self._step_failed_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class StepFailed(BaseApi):

    async def astep_failed(
        self,
        token: str,
        workflow_step_execute_id: str,
        error: str,
        validate: bool = False,
        **kwargs,
    ) -> WorkflowsStepFailedResponsePydantic:
        raw_response = await self.raw.astep_failed(
            token=token,
            workflow_step_execute_id=workflow_step_execute_id,
            error=error,
            **kwargs,
        )
        if validate:
            return WorkflowsStepFailedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkflowsStepFailedResponsePydantic, raw_response.body)
    
    
    def step_failed(
        self,
        token: str,
        workflow_step_execute_id: str,
        error: str,
        validate: bool = False,
    ) -> WorkflowsStepFailedResponsePydantic:
        raw_response = self.raw.step_failed(
            token=token,
            workflow_step_execute_id=workflow_step_execute_id,
            error=error,
        )
        if validate:
            return WorkflowsStepFailedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkflowsStepFailedResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        token: str,
        workflow_step_execute_id: str,
        error: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._step_failed_mapped_args(
            token=token,
            workflow_step_execute_id=workflow_step_execute_id,
            error=error,
        )
        return await self._astep_failed_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        token: str,
        workflow_step_execute_id: str,
        error: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._step_failed_mapped_args(
            token=token,
            workflow_step_execute_id=workflow_step_execute_id,
            error=error,
        )
        return self._step_failed_oapg(
            query_params=args.query,
            header_params=args.header,
        )
