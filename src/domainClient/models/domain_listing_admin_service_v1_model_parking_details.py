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


class DomainListingAdminServiceV1ModelParkingDetails(object):
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
        'parking_type': 'str',
        'number_of_spaces': 'int'
    }

    attribute_map = {
        'parking_type': 'parkingType',
        'number_of_spaces': 'numberOfSpaces'
    }

    def __init__(self, parking_type=None, number_of_spaces=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelParkingDetails - a model defined in Swagger"""  # noqa: E501

        self._parking_type = None
        self._number_of_spaces = None
        self.discriminator = None

        if parking_type is not None:
            self.parking_type = parking_type
        if number_of_spaces is not None:
            self.number_of_spaces = number_of_spaces

    @property
    def parking_type(self):
        """Gets the parking_type of this DomainListingAdminServiceV1ModelParkingDetails.  # noqa: E501

        Can have the value \\\"OnSite\\\", \\\"OnStreet\\\", \\\"NoParking\\\". Default: \\\"NoParking\\\"  # noqa: E501

        :return: The parking_type of this DomainListingAdminServiceV1ModelParkingDetails.  # noqa: E501
        :rtype: str
        """
        return self._parking_type

    @parking_type.setter
    def parking_type(self, parking_type):
        """Sets the parking_type of this DomainListingAdminServiceV1ModelParkingDetails.

        Can have the value \\\"OnSite\\\", \\\"OnStreet\\\", \\\"NoParking\\\". Default: \\\"NoParking\\\"  # noqa: E501

        :param parking_type: The parking_type of this DomainListingAdminServiceV1ModelParkingDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["onSite", "onStreet", "noParking", "garage", "carport", "outdoor"]  # noqa: E501
        if parking_type not in allowed_values:
            raise ValueError(
                "Invalid value for `parking_type` ({0}), must be one of {1}"  # noqa: E501
                .format(parking_type, allowed_values)
            )

        self._parking_type = parking_type

    @property
    def number_of_spaces(self):
        """Gets the number_of_spaces of this DomainListingAdminServiceV1ModelParkingDetails.  # noqa: E501

        Number of parking spaces on site  # noqa: E501

        :return: The number_of_spaces of this DomainListingAdminServiceV1ModelParkingDetails.  # noqa: E501
        :rtype: int
        """
        return self._number_of_spaces

    @number_of_spaces.setter
    def number_of_spaces(self, number_of_spaces):
        """Sets the number_of_spaces of this DomainListingAdminServiceV1ModelParkingDetails.

        Number of parking spaces on site  # noqa: E501

        :param number_of_spaces: The number_of_spaces of this DomainListingAdminServiceV1ModelParkingDetails.  # noqa: E501
        :type: int
        """

        self._number_of_spaces = number_of_spaces

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
        if issubclass(DomainListingAdminServiceV1ModelParkingDetails, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelParkingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other