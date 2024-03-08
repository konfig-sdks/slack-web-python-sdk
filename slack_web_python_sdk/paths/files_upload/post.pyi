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

from slack_web_python_sdk.model.files_upload_response import FilesUploadResponse as FilesUploadResponseSchema
from slack_web_python_sdk.model.files_upload_request import FilesUploadRequest as FilesUploadRequestSchema
from slack_web_python_sdk.model.files_uploaddefault_response import FilesUploaddefaultResponse as FilesUploaddefaultResponseSchema

from slack_web_python_sdk.type.files_upload_request import FilesUploadRequest
from slack_web_python_sdk.type.files_uploaddefault_response import FilesUploaddefaultResponse
from slack_web_python_sdk.type.files_upload_response import FilesUploadResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.files_uploaddefault_response import FilesUploaddefaultResponse as FilesUploaddefaultResponsePydantic
from slack_web_python_sdk.pydantic.files_upload_request import FilesUploadRequest as FilesUploadRequestPydantic
from slack_web_python_sdk.pydantic.files_upload_response import FilesUploadResponse as FilesUploadResponsePydantic

# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = FilesUploadRequestSchema


request_body_files_upload_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
)
SchemaFor200ResponseBodyApplicationJson = FilesUploadResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FilesUploadResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FilesUploadResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = FilesUploaddefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: FilesUploaddefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: FilesUploaddefaultResponse


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

    def _upload_mapped_args(
        self,
        title: typing.Optional[str] = None,
        channels: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        file: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        filetype: typing.Optional[str] = None,
        initial_comment: typing.Optional[str] = None,
        thread_ts: typing.Optional[typing.Union[int, float]] = None,
        token: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if title is not None:
            _body["title"] = title
        if channels is not None:
            _body["channels"] = channels
        if content is not None:
            _body["content"] = content
        if file is not None:
            _body["file"] = file
        if filename is not None:
            _body["filename"] = filename
        if filetype is not None:
            _body["filetype"] = filetype
        if initial_comment is not None:
            _body["initial_comment"] = initial_comment
        if thread_ts is not None:
            _body["thread_ts"] = thread_ts
        if token is not None:
            _body["token"] = token
        args.body = _body
        return args

    async def _aupload_oapg(
        self,
        body: typing.Any = None,
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
        used_path = path.value
    
        _headers = HTTPHeaderDict()
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
            path_template='/files.upload',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_files_upload_request.serialize(body, content_type)
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


    def _upload_oapg(
        self,
        body: typing.Any = None,
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
        used_path = path.value
    
        _headers = HTTPHeaderDict()
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
            path_template='/files.upload',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_files_upload_request.serialize(body, content_type)
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


class UploadRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupload(
        self,
        title: typing.Optional[str] = None,
        channels: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        file: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        filetype: typing.Optional[str] = None,
        initial_comment: typing.Optional[str] = None,
        thread_ts: typing.Optional[typing.Union[int, float]] = None,
        token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_mapped_args(
            title=title,
            channels=channels,
            content=content,
            file=file,
            filename=filename,
            filetype=filetype,
            initial_comment=initial_comment,
            thread_ts=thread_ts,
            token=token,
        )
        return await self._aupload_oapg(
            body=args.body,
            **kwargs,
        )
    
    def upload(
        self,
        title: typing.Optional[str] = None,
        channels: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        file: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        filetype: typing.Optional[str] = None,
        initial_comment: typing.Optional[str] = None,
        thread_ts: typing.Optional[typing.Union[int, float]] = None,
        token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_mapped_args(
            title=title,
            channels=channels,
            content=content,
            file=file,
            filename=filename,
            filetype=filetype,
            initial_comment=initial_comment,
            thread_ts=thread_ts,
            token=token,
        )
        return self._upload_oapg(
            body=args.body,
        )

class Upload(BaseApi):

    async def aupload(
        self,
        title: typing.Optional[str] = None,
        channels: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        file: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        filetype: typing.Optional[str] = None,
        initial_comment: typing.Optional[str] = None,
        thread_ts: typing.Optional[typing.Union[int, float]] = None,
        token: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FilesUploadResponsePydantic:
        raw_response = await self.raw.aupload(
            title=title,
            channels=channels,
            content=content,
            file=file,
            filename=filename,
            filetype=filetype,
            initial_comment=initial_comment,
            thread_ts=thread_ts,
            token=token,
            **kwargs,
        )
        if validate:
            return FilesUploadResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesUploadResponsePydantic, raw_response.body)
    
    
    def upload(
        self,
        title: typing.Optional[str] = None,
        channels: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        file: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        filetype: typing.Optional[str] = None,
        initial_comment: typing.Optional[str] = None,
        thread_ts: typing.Optional[typing.Union[int, float]] = None,
        token: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FilesUploadResponsePydantic:
        raw_response = self.raw.upload(
            title=title,
            channels=channels,
            content=content,
            file=file,
            filename=filename,
            filetype=filetype,
            initial_comment=initial_comment,
            thread_ts=thread_ts,
            token=token,
        )
        if validate:
            return FilesUploadResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesUploadResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        title: typing.Optional[str] = None,
        channels: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        file: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        filetype: typing.Optional[str] = None,
        initial_comment: typing.Optional[str] = None,
        thread_ts: typing.Optional[typing.Union[int, float]] = None,
        token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_mapped_args(
            title=title,
            channels=channels,
            content=content,
            file=file,
            filename=filename,
            filetype=filetype,
            initial_comment=initial_comment,
            thread_ts=thread_ts,
            token=token,
        )
        return await self._aupload_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        title: typing.Optional[str] = None,
        channels: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        file: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        filetype: typing.Optional[str] = None,
        initial_comment: typing.Optional[str] = None,
        thread_ts: typing.Optional[typing.Union[int, float]] = None,
        token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_mapped_args(
            title=title,
            channels=channels,
            content=content,
            file=file,
            filename=filename,
            filetype=filetype,
            initial_comment=initial_comment,
            thread_ts=thread_ts,
            token=token,
        )
        return self._upload_oapg(
            body=args.body,
        )

