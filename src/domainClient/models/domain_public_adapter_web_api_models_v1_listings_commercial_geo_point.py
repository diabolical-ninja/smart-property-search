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


class DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint(object):
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
        'lat': 'float',
        'long': 'float'
    }

    attribute_map = {
        'lat': 'lat',
        'long': 'long'
    }

    def __init__(self, lat=None, long=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint - a model defined in Swagger"""  # noqa: E501

        self._lat = None
        self._long = None
        self.discriminator = None

        if lat is not None:
            self.lat = lat
        if long is not None:
            self.long = long

    @property
    def lat(self):
        """Gets the lat of this DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.  # noqa: E501

        Location latitude  # noqa: E501

        :return: The lat of this DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.

        Location latitude  # noqa: E501

        :param lat: The lat of this DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def long(self):
        """Gets the long of this DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.  # noqa: E501

        Location longitude  # noqa: E501

        :return: The long of this DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.  # noqa: E501
        :rtype: float
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.

        Location longitude  # noqa: E501

        :param long: The long of this DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.  # noqa: E501
        :type: float
        """

        self._long = long

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
        if issubclass(DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other