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


class DomainPropertyReportServiceV1ModelPropertyReportContainer(object):
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
        'mime_type': 'str',
        'content': 'str'
    }

    attribute_map = {
        'mime_type': 'mimeType',
        'content': 'content'
    }

    def __init__(self, mime_type=None, content=None):  # noqa: E501
        """DomainPropertyReportServiceV1ModelPropertyReportContainer - a model defined in Swagger"""  # noqa: E501

        self._mime_type = None
        self._content = None
        self.discriminator = None

        if mime_type is not None:
            self.mime_type = mime_type
        if content is not None:
            self.content = content

    @property
    def mime_type(self):
        """Gets the mime_type of this DomainPropertyReportServiceV1ModelPropertyReportContainer.  # noqa: E501


        :return: The mime_type of this DomainPropertyReportServiceV1ModelPropertyReportContainer.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this DomainPropertyReportServiceV1ModelPropertyReportContainer.


        :param mime_type: The mime_type of this DomainPropertyReportServiceV1ModelPropertyReportContainer.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def content(self):
        """Gets the content of this DomainPropertyReportServiceV1ModelPropertyReportContainer.  # noqa: E501


        :return: The content of this DomainPropertyReportServiceV1ModelPropertyReportContainer.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this DomainPropertyReportServiceV1ModelPropertyReportContainer.


        :param content: The content of this DomainPropertyReportServiceV1ModelPropertyReportContainer.  # noqa: E501
        :type: str
        """
        if content is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', content):  # noqa: E501
            raise ValueError(r"Invalid value for `content`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._content = content

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
        if issubclass(DomainPropertyReportServiceV1ModelPropertyReportContainer, dict):
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
        if not isinstance(other, DomainPropertyReportServiceV1ModelPropertyReportContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
