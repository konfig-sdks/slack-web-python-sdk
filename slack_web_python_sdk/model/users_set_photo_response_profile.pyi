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


class UsersSetPhotoResponseProfile(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "image_32",
            "image_original",
            "image_1024",
            "image_24",
            "image_192",
            "image_48",
            "avatar_hash",
            "image_72",
            "image_512",
        }
        
        class properties:
            
            
            class avatar_hash(
                schemas.StrSchema
            ):
                pass
            image_1024 = schemas.StrSchema
            image_192 = schemas.StrSchema
            image_24 = schemas.StrSchema
            image_32 = schemas.StrSchema
            image_48 = schemas.StrSchema
            image_512 = schemas.StrSchema
            image_72 = schemas.StrSchema
            image_original = schemas.StrSchema
            __annotations__ = {
                "avatar_hash": avatar_hash,
                "image_1024": image_1024,
                "image_192": image_192,
                "image_24": image_24,
                "image_32": image_32,
                "image_48": image_48,
                "image_512": image_512,
                "image_72": image_72,
                "image_original": image_original,
            }
    
    image_32: MetaOapg.properties.image_32
    image_original: MetaOapg.properties.image_original
    image_1024: MetaOapg.properties.image_1024
    image_24: MetaOapg.properties.image_24
    image_192: MetaOapg.properties.image_192
    image_48: MetaOapg.properties.image_48
    avatar_hash: MetaOapg.properties.avatar_hash
    image_72: MetaOapg.properties.image_72
    image_512: MetaOapg.properties.image_512
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar_hash"]) -> MetaOapg.properties.avatar_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_1024"]) -> MetaOapg.properties.image_1024: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_192"]) -> MetaOapg.properties.image_192: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_24"]) -> MetaOapg.properties.image_24: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_32"]) -> MetaOapg.properties.image_32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_48"]) -> MetaOapg.properties.image_48: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_512"]) -> MetaOapg.properties.image_512: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_72"]) -> MetaOapg.properties.image_72: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_original"]) -> MetaOapg.properties.image_original: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["avatar_hash", "image_1024", "image_192", "image_24", "image_32", "image_48", "image_512", "image_72", "image_original", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar_hash"]) -> MetaOapg.properties.avatar_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_1024"]) -> MetaOapg.properties.image_1024: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_192"]) -> MetaOapg.properties.image_192: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_24"]) -> MetaOapg.properties.image_24: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_32"]) -> MetaOapg.properties.image_32: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_48"]) -> MetaOapg.properties.image_48: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_512"]) -> MetaOapg.properties.image_512: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_72"]) -> MetaOapg.properties.image_72: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_original"]) -> MetaOapg.properties.image_original: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["avatar_hash", "image_1024", "image_192", "image_24", "image_32", "image_48", "image_512", "image_72", "image_original", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        image_32: typing.Union[MetaOapg.properties.image_32, str, ],
        image_original: typing.Union[MetaOapg.properties.image_original, str, ],
        image_1024: typing.Union[MetaOapg.properties.image_1024, str, ],
        image_24: typing.Union[MetaOapg.properties.image_24, str, ],
        image_192: typing.Union[MetaOapg.properties.image_192, str, ],
        image_48: typing.Union[MetaOapg.properties.image_48, str, ],
        avatar_hash: typing.Union[MetaOapg.properties.avatar_hash, str, ],
        image_72: typing.Union[MetaOapg.properties.image_72, str, ],
        image_512: typing.Union[MetaOapg.properties.image_512, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersSetPhotoResponseProfile':
        return super().__new__(
            cls,
            *args,
            image_32=image_32,
            image_original=image_original,
            image_1024=image_1024,
            image_24=image_24,
            image_192=image_192,
            image_48=image_48,
            avatar_hash=avatar_hash,
            image_72=image_72,
            image_512=image_512,
            _configuration=_configuration,
            **kwargs,
        )