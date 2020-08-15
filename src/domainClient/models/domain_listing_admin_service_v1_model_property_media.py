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


class DomainListingAdminServiceV1ModelPropertyMedia(object):
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
        'resource_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'resource_type': 'resourceType',
        'url': 'url'
    }

    def __init__(self, resource_type=None, url=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelPropertyMedia - a model defined in Swagger"""  # noqa: E501

        self._resource_type = None
        self._url = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if url is not None:
            self.url = url

    @property
    def resource_type(self):
        """Gets the resource_type of this DomainListingAdminServiceV1ModelPropertyMedia.  # noqa: E501

        Type of the resource  # noqa: E501

        :return: The resource_type of this DomainListingAdminServiceV1ModelPropertyMedia.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DomainListingAdminServiceV1ModelPropertyMedia.

        Type of the resource  # noqa: E501

        :param resource_type: The resource_type of this DomainListingAdminServiceV1ModelPropertyMedia.  # noqa: E501
        :type: str
        """
        allowed_values = ["photograph", "floorPlan", "video", "virtualTour", "webLink"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def url(self):
        """Gets the url of this DomainListingAdminServiceV1ModelPropertyMedia.  # noqa: E501

        shows the place from where file can be downloaded  # noqa: E501

        :return: The url of this DomainListingAdminServiceV1ModelPropertyMedia.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DomainListingAdminServiceV1ModelPropertyMedia.

        shows the place from where file can be downloaded  # noqa: E501

        :param url: The url of this DomainListingAdminServiceV1ModelPropertyMedia.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(DomainListingAdminServiceV1ModelPropertyMedia, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelPropertyMedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other