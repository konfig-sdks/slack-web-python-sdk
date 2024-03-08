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

from slack_web_python_sdk.model.users_set_photodefault_response import UsersSetPhotodefaultResponse as UsersSetPhotodefaultResponseSchema
from slack_web_python_sdk.model.users_set_photo_request import UsersSetPhotoRequest as UsersSetPhotoRequestSchema
from slack_web_python_sdk.model.users_set_photo_response import UsersSetPhotoResponse as UsersSetPhotoResponseSchema

from slack_web_python_sdk.type.users_set_photo_request import UsersSetPhotoRequest
from slack_web_python_sdk.type.users_set_photo_response import UsersSetPhotoResponse
from slack_web_python_sdk.type.users_set_photodefault_response import UsersSetPhotodefaultResponse

from ...api_client import Dictionary
from slack_web_python_sdk.pydantic.users_set_photo_request import UsersSetPhotoRequest as UsersSetPhotoRequestPydantic
from slack_web_python_sdk.pydantic.users_set_photo_response import UsersSetPhotoResponse as UsersSetPhotoResponsePydantic
from slack_web_python_sdk.pydantic.users_set_photodefault_response import UsersSetPhotodefaultResponse as UsersSetPhotodefaultResponsePydantic

# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = UsersSetPhotoRequestSchema


request_body_users_set_photo_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = UsersSetPhotoResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UsersSetPhotoResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsersSetPhotoResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = UsersSetPhotodefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: UsersSetPhotodefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: UsersSetPhotodefaultResponse


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

    def _set_photo_mapped_args(
        self,
        token: str,
        crop_w: typing.Optional[str] = None,
        crop_x: typing.Optional[str] = None,
        crop_y: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if crop_w is not None:
            _body["crop_w"] = crop_w
        if crop_x is not None:
            _body["crop_x"] = crop_x
        if crop_y is not None:
            _body["crop_y"] = crop_y
        if image is not None:
            _body["image"] = image
        if token is not None:
            _body["token"] = token
        args.body = _body
        return args

    async def _aset_photo_oapg(
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
            path_template='/users.setPhoto',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_users_set_photo_request.serialize(body, content_type)
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


    def _set_photo_oapg(
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
            path_template='/users.setPhoto',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_users_set_photo_request.serialize(body, content_type)
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


class SetPhotoRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aset_photo(
        self,
        token: str,
        crop_w: typing.Optional[str] = None,
        crop_x: typing.Optional[str] = None,
        crop_y: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_photo_mapped_args(
            token=token,
            crop_w=crop_w,
            crop_x=crop_x,
            crop_y=crop_y,
            image=image,
        )
        return await self._aset_photo_oapg(
            body=args.body,
            **kwargs,
        )
    
    def set_photo(
        self,
        token: str,
        crop_w: typing.Optional[str] = None,
        crop_x: typing.Optional[str] = None,
        crop_y: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_photo_mapped_args(
            token=token,
            crop_w=crop_w,
            crop_x=crop_x,
            crop_y=crop_y,
            image=image,
        )
        return self._set_photo_oapg(
            body=args.body,
        )

class SetPhoto(BaseApi):

    async def aset_photo(
        self,
        token: str,
        crop_w: typing.Optional[str] = None,
        crop_x: typing.Optional[str] = None,
        crop_y: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsersSetPhotoResponsePydantic:
        raw_response = await self.raw.aset_photo(
            token=token,
            crop_w=crop_w,
            crop_x=crop_x,
            crop_y=crop_y,
            image=image,
            **kwargs,
        )
        if validate:
            return UsersSetPhotoResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UsersSetPhotoResponsePydantic, raw_response.body)
    
    
    def set_photo(
        self,
        token: str,
        crop_w: typing.Optional[str] = None,
        crop_x: typing.Optional[str] = None,
        crop_y: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UsersSetPhotoResponsePydantic:
        raw_response = self.raw.set_photo(
            token=token,
            crop_w=crop_w,
            crop_x=crop_x,
            crop_y=crop_y,
            image=image,
        )
        if validate:
            return UsersSetPhotoResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UsersSetPhotoResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        token: str,
        crop_w: typing.Optional[str] = None,
        crop_x: typing.Optional[str] = None,
        crop_y: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_photo_mapped_args(
            token=token,
            crop_w=crop_w,
            crop_x=crop_x,
            crop_y=crop_y,
            image=image,
        )
        return await self._aset_photo_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        token: str,
        crop_w: typing.Optional[str] = None,
        crop_x: typing.Optional[str] = None,
        crop_y: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_photo_mapped_args(
            token=token,
            crop_w=crop_w,
            crop_x=crop_x,
            crop_y=crop_y,
            image=image,
        )
        return self._set_photo_oapg(
            body=args.body,
        )

