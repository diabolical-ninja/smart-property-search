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


class DomainSearchServiceV2ModelDomainSearchContractsV2Media(object):
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
        'category': 'str',
        'url': 'str'
    }

    attribute_map = {
        'category': 'category',
        'url': 'url'
    }

    def __init__(self, category=None, url=None):  # noqa: E501
        """DomainSearchServiceV2ModelDomainSearchContractsV2Media - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._url = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if url is not None:
            self.url = url

    @property
    def category(self):
        """Gets the category of this DomainSearchServiceV2ModelDomainSearchContractsV2Media.  # noqa: E501


        :return: The category of this DomainSearchServiceV2ModelDomainSearchContractsV2Media.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this DomainSearchServiceV2ModelDomainSearchContractsV2Media.


        :param category: The category of this DomainSearchServiceV2ModelDomainSearchContractsV2Media.  # noqa: E501
        :type: str
        """
        allowed_values = ["Image"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def url(self):
        """Gets the url of this DomainSearchServiceV2ModelDomainSearchContractsV2Media.  # noqa: E501


        :return: The url of this DomainSearchServiceV2ModelDomainSearchContractsV2Media.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DomainSearchServiceV2ModelDomainSearchContractsV2Media.


        :param url: The url of this DomainSearchServiceV2ModelDomainSearchContractsV2Media.  # noqa: E501
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
        if issubclass(DomainSearchServiceV2ModelDomainSearchContractsV2Media, dict):
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
        if not isinstance(other, DomainSearchServiceV2ModelDomainSearchContractsV2Media):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other