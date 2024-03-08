# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

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


class ObjsIcon(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            image_102 = schemas.StrSchema
            image_132 = schemas.StrSchema
            image_230 = schemas.StrSchema
            image_34 = schemas.StrSchema
            image_44 = schemas.StrSchema
            image_68 = schemas.StrSchema
            image_88 = schemas.StrSchema
            image_default = schemas.BoolSchema
            __annotations__ = {
                "image_102": image_102,
                "image_132": image_132,
                "image_230": image_230,
                "image_34": image_34,
                "image_44": image_44,
                "image_68": image_68,
                "image_88": image_88,
                "image_default": image_default,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_102"]) -> MetaOapg.properties.image_102: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_132"]) -> MetaOapg.properties.image_132: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_230"]) -> MetaOapg.properties.image_230: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_34"]) -> MetaOapg.properties.image_34: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_44"]) -> MetaOapg.properties.image_44: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_68"]) -> MetaOapg.properties.image_68: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_88"]) -> MetaOapg.properties.image_88: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_default"]) -> MetaOapg.properties.image_default: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["image_102", "image_132", "image_230", "image_34", "image_44", "image_68", "image_88", "image_default", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_102"]) -> typing.Union[MetaOapg.properties.image_102, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_132"]) -> typing.Union[MetaOapg.properties.image_132, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_230"]) -> typing.Union[MetaOapg.properties.image_230, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_34"]) -> typing.Union[MetaOapg.properties.image_34, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_44"]) -> typing.Union[MetaOapg.properties.image_44, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_68"]) -> typing.Union[MetaOapg.properties.image_68, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_88"]) -> typing.Union[MetaOapg.properties.image_88, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_default"]) -> typing.Union[MetaOapg.properties.image_default, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["image_102", "image_132", "image_230", "image_34", "image_44", "image_68", "image_88", "image_default", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        image_102: typing.Union[MetaOapg.properties.image_102, str, schemas.Unset] = schemas.unset,
        image_132: typing.Union[MetaOapg.properties.image_132, str, schemas.Unset] = schemas.unset,
        image_230: typing.Union[MetaOapg.properties.image_230, str, schemas.Unset] = schemas.unset,
        image_34: typing.Union[MetaOapg.properties.image_34, str, schemas.Unset] = schemas.unset,
        image_44: typing.Union[MetaOapg.properties.image_44, str, schemas.Unset] = schemas.unset,
        image_68: typing.Union[MetaOapg.properties.image_68, str, schemas.Unset] = schemas.unset,
        image_88: typing.Union[MetaOapg.properties.image_88, str, schemas.Unset] = schemas.unset,
        image_default: typing.Union[MetaOapg.properties.image_default, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjsIcon':
        return super().__new__(
            cls,
            *args,
            image_102=image_102,
            image_132=image_132,
            image_230=image_230,
            image_34=image_34,
            image_44=image_44,
            image_68=image_68,
            image_88=image_88,
            image_default=image_default,
            _configuration=_configuration,
            **kwargs,
        )
