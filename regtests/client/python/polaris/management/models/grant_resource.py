#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# coding: utf-8

"""
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from polaris.management.models.catalog_grant import CatalogGrant
    from polaris.management.models.namespace_grant import NamespaceGrant
    from polaris.management.models.table_grant import TableGrant
    from polaris.management.models.view_grant import ViewGrant

class GrantResource(BaseModel):
    """
    GrantResource
    """ # noqa: E501
    type: StrictStr
    __properties: ClassVar[List[str]] = ["type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['catalog', 'namespace', 'table', 'view']):
            raise ValueError("must be one of enum values ('catalog', 'namespace', 'table', 'view')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'catalog': 'CatalogGrant','namespace': 'NamespaceGrant','table': 'TableGrant','view': 'ViewGrant'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[CatalogGrant, NamespaceGrant, TableGrant, ViewGrant]]:
        """Create an instance of GrantResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[CatalogGrant, NamespaceGrant, TableGrant, ViewGrant]]:
        """Create an instance of GrantResource from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'CatalogGrant':
            return import_module("polaris.management.models.catalog_grant").CatalogGrant.from_dict(obj)
        if object_type ==  'NamespaceGrant':
            return import_module("polaris.management.models.namespace_grant").NamespaceGrant.from_dict(obj)
        if object_type ==  'TableGrant':
            return import_module("polaris.management.models.table_grant").TableGrant.from_dict(obj)
        if object_type ==  'ViewGrant':
            return import_module("polaris.management.models.view_grant").ViewGrant.from_dict(obj)

        raise ValueError("GrantResource failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


