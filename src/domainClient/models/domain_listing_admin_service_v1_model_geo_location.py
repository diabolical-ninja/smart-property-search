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


class DomainListingAdminServiceV1ModelGeoLocation(object):
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
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, latitude=None, longitude=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelGeoLocation - a model defined in Swagger"""  # noqa: E501

        self._latitude = None
        self._longitude = None
        self.discriminator = None

        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this DomainListingAdminServiceV1ModelGeoLocation.  # noqa: E501

        Latitude  # noqa: E501

        :return: The latitude of this DomainListingAdminServiceV1ModelGeoLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this DomainListingAdminServiceV1ModelGeoLocation.

        Latitude  # noqa: E501

        :param latitude: The latitude of this DomainListingAdminServiceV1ModelGeoLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this DomainListingAdminServiceV1ModelGeoLocation.  # noqa: E501

        Longitude  # noqa: E501

        :return: The longitude of this DomainListingAdminServiceV1ModelGeoLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this DomainListingAdminServiceV1ModelGeoLocation.

        Longitude  # noqa: E501

        :param longitude: The longitude of this DomainListingAdminServiceV1ModelGeoLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

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
        if issubclass(DomainListingAdminServiceV1ModelGeoLocation, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelGeoLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
