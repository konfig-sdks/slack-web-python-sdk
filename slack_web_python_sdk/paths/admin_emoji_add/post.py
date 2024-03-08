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

from slack_web_python_sdk.model.adminemoji_add_emoji_response import AdminemojiAddEmojiResponse as AdminemojiAddEmojiResponseSchema
from slack_web_python_sdk.model.adminemoji_add_emoji_request import AdminemojiAddEmojiRequest as AdminemojiAddEmojiRequestSchema
from slack_web_python_sdk.model.adminemoji_add_emojidefault_response import AdminemojiAddEmojidefaultResponse as AdminemojiAddEmojidefaultResponseSchema

from slack_web_python_sdk.type.adminemoji_add_emoji_response import AdminemojiAddEmojiResponse
from slack_web_python_sdk.type.adminemoji_add_emojidefault_response import AdminemojiAddEmojidefaultResponse
from slack_web_python_sdk.type.adminemoji_add_emoji_request import AdminemojiAddEmojiRequest

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.adminemoji_add_emojidefault_response import AdminemojiAddEmojidefaultResponse as AdminemojiAddEmojidefaultResponsePydantic
from slack_web_python_sdk.pydantic.adminemoji_add_emoji_response import AdminemojiAddEmojiResponse as AdminemojiAddEmojiResponsePydantic
from slack_web_python_sdk.pydantic.adminemoji_add_emoji_request import AdminemojiAddEmojiRequest as AdminemojiAddEmojiRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = AdminemojiAddEmojiRequestSchema


request_body_adminemoji_add_emoji_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
_auth = [
    'slackAuth',
]
SchemaFor200ResponseBodyApplicationJson = AdminemojiAddEmojiResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AdminemojiAddEmojiResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AdminemojiAddEmojiResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = AdminemojiAddEmojidefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: AdminemojiAddEmojidefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: AdminemojiAddEmojidefaultResponse


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

    def _add_emoji_mapped_args(
        self,
        name: str,
        token: str,
        url: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if name is not None:
            _body["name"] = name
        if token is not None:
            _body["token"] = token
        if url is not None:
            _body["url"] = url
        args.body = _body
        return args

    async def _aadd_emoji_oapg(
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/admin.emoji.add',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_adminemoji_add_emoji_request.serialize(body, content_type)
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


    def _add_emoji_oapg(
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/admin.emoji.add',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_adminemoji_add_emoji_request.serialize(body, content_type)
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


class AddEmojiRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_emoji(
        self,
        name: str,
        token: str,
        url: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_emoji_mapped_args(
            name=name,
            token=token,
            url=url,
        )
        return await self._aadd_emoji_oapg(
            body=args.body,
            **kwargs,
        )
    
    def add_emoji(
        self,
        name: str,
        token: str,
        url: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_emoji_mapped_args(
            name=name,
            token=token,
            url=url,
        )
        return self._add_emoji_oapg(
            body=args.body,
        )

class AddEmoji(BaseApi):

    async def aadd_emoji(
        self,
        name: str,
        token: str,
        url: str,
        validate: bool = False,
        **kwargs,
    ) -> AdminemojiAddEmojiResponsePydantic:
        raw_response = await self.raw.aadd_emoji(
            name=name,
            token=token,
            url=url,
            **kwargs,
        )
        if validate:
            return AdminemojiAddEmojiResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminemojiAddEmojiResponsePydantic, raw_response.body)
    
    
    def add_emoji(
        self,
        name: str,
        token: str,
        url: str,
        validate: bool = False,
    ) -> AdminemojiAddEmojiResponsePydantic:
        raw_response = self.raw.add_emoji(
            name=name,
            token=token,
            url=url,
        )
        if validate:
            return AdminemojiAddEmojiResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminemojiAddEmojiResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        token: str,
        url: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_emoji_mapped_args(
            name=name,
            token=token,
            url=url,
        )
        return await self._aadd_emoji_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        token: str,
        url: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_emoji_mapped_args(
            name=name,
            token=token,
            url=url,
        )
        return self._add_emoji_oapg(
            body=args.body,
        )

