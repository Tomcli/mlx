# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.api_model_framework import ApiModelFramework  # noqa: F401,E501
from swagger_server.models.api_parameter import ApiParameter  # noqa: F401,E501
from swagger_server import util


class ApiModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, created_at: datetime=None, name: str=None, description: str=None, featured: bool=None, publish_approved: bool=None, related_assets: List[str]=None, domain: str=None, labels: Dict[str, str]=None, framework: ApiModelFramework=None, trainable: bool=None, trainable_tested_platforms: List[str]=None, trainable_credentials_required: bool=None, trainable_parameters: List[ApiParameter]=None, servable: bool=None, servable_tested_platforms: List[str]=None, servable_credentials_required: bool=None, servable_parameters: List[ApiParameter]=None):  # noqa: E501
        """ApiModel - a model defined in Swagger

        :param id: The id of this ApiModel.  # noqa: E501
        :type id: str
        :param created_at: The created_at of this ApiModel.  # noqa: E501
        :type created_at: datetime
        :param name: The name of this ApiModel.  # noqa: E501
        :type name: str
        :param description: The description of this ApiModel.  # noqa: E501
        :type description: str
        :param featured: The featured of this ApiModel.  # noqa: E501
        :type featured: bool
        :param publish_approved: The publish_approved of this ApiModel.  # noqa: E501
        :type publish_approved: bool
        :param related_assets: The related_assets of this ApiModel.  # noqa: E501
        :type related_assets: List[str]
        :param domain: The domain of this ApiModel.  # noqa: E501
        :type domain: str
        :param labels: The labels of this ApiModel.  # noqa: E501
        :type labels: Dict[str, str]
        :param framework: The framework of this ApiModel.  # noqa: E501
        :type framework: ApiModelFramework
        :param trainable: The trainable of this ApiModel.  # noqa: E501
        :type trainable: bool
        :param trainable_tested_platforms: The trainable_tested_platforms of this ApiModel.  # noqa: E501
        :type trainable_tested_platforms: List[str]
        :param trainable_credentials_required: The trainable_credentials_required of this ApiModel.  # noqa: E501
        :type trainable_credentials_required: bool
        :param trainable_parameters: The trainable_parameters of this ApiModel.  # noqa: E501
        :type trainable_parameters: List[ApiParameter]
        :param servable: The servable of this ApiModel.  # noqa: E501
        :type servable: bool
        :param servable_tested_platforms: The servable_tested_platforms of this ApiModel.  # noqa: E501
        :type servable_tested_platforms: List[str]
        :param servable_credentials_required: The servable_credentials_required of this ApiModel.  # noqa: E501
        :type servable_credentials_required: bool
        :param servable_parameters: The servable_parameters of this ApiModel.  # noqa: E501
        :type servable_parameters: List[ApiParameter]
        """
        self.swagger_types = {
            'id': str,
            'created_at': datetime,
            'name': str,
            'description': str,
            'featured': bool,
            'publish_approved': bool,
            'related_assets': List[str],
            'domain': str,
            'labels': Dict[str, str],
            'framework': ApiModelFramework,
            'trainable': bool,
            'trainable_tested_platforms': List[str],
            'trainable_credentials_required': bool,
            'trainable_parameters': List[ApiParameter],
            'servable': bool,
            'servable_tested_platforms': List[str],
            'servable_credentials_required': bool,
            'servable_parameters': List[ApiParameter]
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'name': 'name',
            'description': 'description',
            'featured': 'featured',
            'publish_approved': 'publish_approved',
            'related_assets': 'related_assets',
            'domain': 'domain',
            'labels': 'labels',
            'framework': 'framework',
            'trainable': 'trainable',
            'trainable_tested_platforms': 'trainable_tested_platforms',
            'trainable_credentials_required': 'trainable_credentials_required',
            'trainable_parameters': 'trainable_parameters',
            'servable': 'servable',
            'servable_tested_platforms': 'servable_tested_platforms',
            'servable_credentials_required': 'servable_credentials_required',
            'servable_parameters': 'servable_parameters'
        }

        self._id = id
        self._created_at = created_at
        self._name = name
        self._description = description
        self._featured = featured
        self._publish_approved = publish_approved
        self._related_assets = related_assets
        self._domain = domain
        self._labels = labels
        self._framework = framework
        self._trainable = trainable
        self._trainable_tested_platforms = trainable_tested_platforms
        self._trainable_credentials_required = trainable_credentials_required
        self._trainable_parameters = trainable_parameters
        self._servable = servable
        self._servable_tested_platforms = servable_tested_platforms
        self._servable_credentials_required = servable_credentials_required
        self._servable_parameters = servable_parameters

    @classmethod
    def from_dict(cls, dikt) -> 'ApiModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiModel of this ApiModel.  # noqa: E501
        :rtype: ApiModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ApiModel.


        :return: The id of this ApiModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ApiModel.


        :param id: The id of this ApiModel.
        :type id: str
        """

        self._id = id

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this ApiModel.


        :return: The created_at of this ApiModel.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this ApiModel.


        :param created_at: The created_at of this ApiModel.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def name(self) -> str:
        """Gets the name of this ApiModel.


        :return: The name of this ApiModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ApiModel.


        :param name: The name of this ApiModel.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this ApiModel.


        :return: The description of this ApiModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ApiModel.


        :param description: The description of this ApiModel.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def featured(self) -> bool:
        """Gets the featured of this ApiModel.


        :return: The featured of this ApiModel.
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured: bool):
        """Sets the featured of this ApiModel.


        :param featured: The featured of this ApiModel.
        :type featured: bool
        """

        self._featured = featured

    @property
    def publish_approved(self) -> bool:
        """Gets the publish_approved of this ApiModel.


        :return: The publish_approved of this ApiModel.
        :rtype: bool
        """
        return self._publish_approved

    @publish_approved.setter
    def publish_approved(self, publish_approved: bool):
        """Sets the publish_approved of this ApiModel.


        :param publish_approved: The publish_approved of this ApiModel.
        :type publish_approved: bool
        """

        self._publish_approved = publish_approved

    @property
    def related_assets(self) -> List[str]:
        """Gets the related_assets of this ApiModel.


        :return: The related_assets of this ApiModel.
        :rtype: List[str]
        """
        return self._related_assets

    @related_assets.setter
    def related_assets(self, related_assets: List[str]):
        """Sets the related_assets of this ApiModel.


        :param related_assets: The related_assets of this ApiModel.
        :type related_assets: List[str]
        """

        self._related_assets = related_assets

    @property
    def domain(self) -> str:
        """Gets the domain of this ApiModel.


        :return: The domain of this ApiModel.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain: str):
        """Sets the domain of this ApiModel.


        :param domain: The domain of this ApiModel.
        :type domain: str
        """

        self._domain = domain

    @property
    def labels(self) -> Dict[str, str]:
        """Gets the labels of this ApiModel.


        :return: The labels of this ApiModel.
        :rtype: Dict[str, str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels: Dict[str, str]):
        """Sets the labels of this ApiModel.


        :param labels: The labels of this ApiModel.
        :type labels: Dict[str, str]
        """

        self._labels = labels

    @property
    def framework(self) -> ApiModelFramework:
        """Gets the framework of this ApiModel.


        :return: The framework of this ApiModel.
        :rtype: ApiModelFramework
        """
        return self._framework

    @framework.setter
    def framework(self, framework: ApiModelFramework):
        """Sets the framework of this ApiModel.


        :param framework: The framework of this ApiModel.
        :type framework: ApiModelFramework
        """
        if framework is None:
            raise ValueError("Invalid value for `framework`, must not be `None`")  # noqa: E501

        self._framework = framework

    @property
    def trainable(self) -> bool:
        """Gets the trainable of this ApiModel.


        :return: The trainable of this ApiModel.
        :rtype: bool
        """
        return self._trainable

    @trainable.setter
    def trainable(self, trainable: bool):
        """Sets the trainable of this ApiModel.


        :param trainable: The trainable of this ApiModel.
        :type trainable: bool
        """

        self._trainable = trainable

    @property
    def trainable_tested_platforms(self) -> List[str]:
        """Gets the trainable_tested_platforms of this ApiModel.


        :return: The trainable_tested_platforms of this ApiModel.
        :rtype: List[str]
        """
        return self._trainable_tested_platforms

    @trainable_tested_platforms.setter
    def trainable_tested_platforms(self, trainable_tested_platforms: List[str]):
        """Sets the trainable_tested_platforms of this ApiModel.


        :param trainable_tested_platforms: The trainable_tested_platforms of this ApiModel.
        :type trainable_tested_platforms: List[str]
        """

        self._trainable_tested_platforms = trainable_tested_platforms

    @property
    def trainable_credentials_required(self) -> bool:
        """Gets the trainable_credentials_required of this ApiModel.


        :return: The trainable_credentials_required of this ApiModel.
        :rtype: bool
        """
        return self._trainable_credentials_required

    @trainable_credentials_required.setter
    def trainable_credentials_required(self, trainable_credentials_required: bool):
        """Sets the trainable_credentials_required of this ApiModel.


        :param trainable_credentials_required: The trainable_credentials_required of this ApiModel.
        :type trainable_credentials_required: bool
        """

        self._trainable_credentials_required = trainable_credentials_required

    @property
    def trainable_parameters(self) -> List[ApiParameter]:
        """Gets the trainable_parameters of this ApiModel.


        :return: The trainable_parameters of this ApiModel.
        :rtype: List[ApiParameter]
        """
        return self._trainable_parameters

    @trainable_parameters.setter
    def trainable_parameters(self, trainable_parameters: List[ApiParameter]):
        """Sets the trainable_parameters of this ApiModel.


        :param trainable_parameters: The trainable_parameters of this ApiModel.
        :type trainable_parameters: List[ApiParameter]
        """

        self._trainable_parameters = trainable_parameters

    @property
    def servable(self) -> bool:
        """Gets the servable of this ApiModel.


        :return: The servable of this ApiModel.
        :rtype: bool
        """
        return self._servable

    @servable.setter
    def servable(self, servable: bool):
        """Sets the servable of this ApiModel.


        :param servable: The servable of this ApiModel.
        :type servable: bool
        """

        self._servable = servable

    @property
    def servable_tested_platforms(self) -> List[str]:
        """Gets the servable_tested_platforms of this ApiModel.


        :return: The servable_tested_platforms of this ApiModel.
        :rtype: List[str]
        """
        return self._servable_tested_platforms

    @servable_tested_platforms.setter
    def servable_tested_platforms(self, servable_tested_platforms: List[str]):
        """Sets the servable_tested_platforms of this ApiModel.


        :param servable_tested_platforms: The servable_tested_platforms of this ApiModel.
        :type servable_tested_platforms: List[str]
        """

        self._servable_tested_platforms = servable_tested_platforms

    @property
    def servable_credentials_required(self) -> bool:
        """Gets the servable_credentials_required of this ApiModel.


        :return: The servable_credentials_required of this ApiModel.
        :rtype: bool
        """
        return self._servable_credentials_required

    @servable_credentials_required.setter
    def servable_credentials_required(self, servable_credentials_required: bool):
        """Sets the servable_credentials_required of this ApiModel.


        :param servable_credentials_required: The servable_credentials_required of this ApiModel.
        :type servable_credentials_required: bool
        """

        self._servable_credentials_required = servable_credentials_required

    @property
    def servable_parameters(self) -> List[ApiParameter]:
        """Gets the servable_parameters of this ApiModel.


        :return: The servable_parameters of this ApiModel.
        :rtype: List[ApiParameter]
        """
        return self._servable_parameters

    @servable_parameters.setter
    def servable_parameters(self, servable_parameters: List[ApiParameter]):
        """Sets the servable_parameters of this ApiModel.


        :param servable_parameters: The servable_parameters of this ApiModel.
        :type servable_parameters: List[ApiParameter]
        """

        self._servable_parameters = servable_parameters
