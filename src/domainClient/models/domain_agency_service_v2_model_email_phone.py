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


class DomainAgencyServiceV2ModelEmailPhone(object):
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
        'email': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'email': 'email',
        'phone': 'phone'
    }

    def __init__(self, email=None, phone=None):  # noqa: E501
        """DomainAgencyServiceV2ModelEmailPhone - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._phone = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this DomainAgencyServiceV2ModelEmailPhone.  # noqa: E501


        :return: The email of this DomainAgencyServiceV2ModelEmailPhone.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DomainAgencyServiceV2ModelEmailPhone.


        :param email: The email of this DomainAgencyServiceV2ModelEmailPhone.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this DomainAgencyServiceV2ModelEmailPhone.  # noqa: E501


        :return: The phone of this DomainAgencyServiceV2ModelEmailPhone.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this DomainAgencyServiceV2ModelEmailPhone.


        :param phone: The phone of this DomainAgencyServiceV2ModelEmailPhone.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if issubclass(DomainAgencyServiceV2ModelEmailPhone, dict):
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
        if not isinstance(other, DomainAgencyServiceV2ModelEmailPhone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other