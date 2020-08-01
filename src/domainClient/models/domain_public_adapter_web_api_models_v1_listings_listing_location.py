# coding: utf-8

"""
    Domain Group API V1

    Provides public access to Domain's microservices  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DomainPublicAdapterWebApiModelsV1ListingsListingLocation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'state': 'str',
        'postcode': 'str',
        'area': 'str',
        'region': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'state': 'state',
        'postcode': 'postcode',
        'area': 'area',
        'region': 'region',
        'type': 'type'
    }

    def __init__(self, name=None, state=None, postcode=None, area=None, region=None, type=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1ListingsListingLocation - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._state = None
        self._postcode = None
        self._area = None
        self._region = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if postcode is not None:
            self.postcode = postcode
        if area is not None:
            self.area = area
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.

        Name  # noqa: E501

        :param name: The name of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501

        State  # noqa: E501

        :return: The state of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.

        State  # noqa: E501

        :param state: The state of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def postcode(self):
        """Gets the postcode of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501

        Postcode  # noqa: E501

        :return: The postcode of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.

        Postcode  # noqa: E501

        :param postcode: The postcode of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def area(self):
        """Gets the area of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501

        Area  # noqa: E501

        :return: The area of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.

        Area  # noqa: E501

        :param area: The area of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def region(self):
        """Gets the region of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501

        Region  # noqa: E501

        :return: The region of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.

        Region  # noqa: E501

        :param region: The region of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def type(self):
        """Gets the type of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501

        Type  # noqa: E501

        :return: The type of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.

        Type  # noqa: E501

        :param type: The type of this DomainPublicAdapterWebApiModelsV1ListingsListingLocation.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DomainPublicAdapterWebApiModelsV1ListingsListingLocation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1ListingsListingLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
