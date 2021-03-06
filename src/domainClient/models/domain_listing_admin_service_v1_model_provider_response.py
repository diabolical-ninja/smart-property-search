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


class DomainListingAdminServiceV1ModelProviderResponse(object):
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
        'id': 'str',
        'company_name': 'str',
        'contact_name_technical': 'str',
        'email_technical': 'str',
        'phone_technical': 'str',
        'contact_name_business': 'str',
        'email_business': 'str',
        'phone_business': 'str'
    }

    attribute_map = {
        'id': 'id',
        'company_name': 'companyName',
        'contact_name_technical': 'contactNameTechnical',
        'email_technical': 'emailTechnical',
        'phone_technical': 'phoneTechnical',
        'contact_name_business': 'contactNameBusiness',
        'email_business': 'emailBusiness',
        'phone_business': 'phoneBusiness'
    }

    def __init__(self, id=None, company_name=None, contact_name_technical=None, email_technical=None, phone_technical=None, contact_name_business=None, email_business=None, phone_business=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelProviderResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._company_name = None
        self._contact_name_technical = None
        self._email_technical = None
        self._phone_technical = None
        self._contact_name_business = None
        self._email_business = None
        self._phone_business = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if company_name is not None:
            self.company_name = company_name
        if contact_name_technical is not None:
            self.contact_name_technical = contact_name_technical
        if email_technical is not None:
            self.email_technical = email_technical
        if phone_technical is not None:
            self.phone_technical = phone_technical
        if contact_name_business is not None:
            self.contact_name_business = contact_name_business
        if email_business is not None:
            self.email_business = email_business
        if phone_business is not None:
            self.phone_business = phone_business

    @property
    def id(self):
        """Gets the id of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501

        Provider identifier - this will map to the username  # noqa: E501

        :return: The id of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainListingAdminServiceV1ModelProviderResponse.

        Provider identifier - this will map to the username  # noqa: E501

        :param id: The id of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def company_name(self):
        """Gets the company_name of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501

        Company name  # noqa: E501

        :return: The company_name of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this DomainListingAdminServiceV1ModelProviderResponse.

        Company name  # noqa: E501

        :param company_name: The company_name of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def contact_name_technical(self):
        """Gets the contact_name_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501

        Contact person's name for technical related enquiries  # noqa: E501

        :return: The contact_name_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._contact_name_technical

    @contact_name_technical.setter
    def contact_name_technical(self, contact_name_technical):
        """Sets the contact_name_technical of this DomainListingAdminServiceV1ModelProviderResponse.

        Contact person's name for technical related enquiries  # noqa: E501

        :param contact_name_technical: The contact_name_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :type: str
        """

        self._contact_name_technical = contact_name_technical

    @property
    def email_technical(self):
        """Gets the email_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501

        Email address to receive technical related emails  # noqa: E501

        :return: The email_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_technical

    @email_technical.setter
    def email_technical(self, email_technical):
        """Sets the email_technical of this DomainListingAdminServiceV1ModelProviderResponse.

        Email address to receive technical related emails  # noqa: E501

        :param email_technical: The email_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :type: str
        """

        self._email_technical = email_technical

    @property
    def phone_technical(self):
        """Gets the phone_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501

        Phone to be contact for technical related enquiries  # noqa: E501

        :return: The phone_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone_technical

    @phone_technical.setter
    def phone_technical(self, phone_technical):
        """Sets the phone_technical of this DomainListingAdminServiceV1ModelProviderResponse.

        Phone to be contact for technical related enquiries  # noqa: E501

        :param phone_technical: The phone_technical of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :type: str
        """

        self._phone_technical = phone_technical

    @property
    def contact_name_business(self):
        """Gets the contact_name_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501

        Contact person's name for business related enquiries  # noqa: E501

        :return: The contact_name_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._contact_name_business

    @contact_name_business.setter
    def contact_name_business(self, contact_name_business):
        """Sets the contact_name_business of this DomainListingAdminServiceV1ModelProviderResponse.

        Contact person's name for business related enquiries  # noqa: E501

        :param contact_name_business: The contact_name_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :type: str
        """

        self._contact_name_business = contact_name_business

    @property
    def email_business(self):
        """Gets the email_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501

        Email address to receive business related emails  # noqa: E501

        :return: The email_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_business

    @email_business.setter
    def email_business(self, email_business):
        """Sets the email_business of this DomainListingAdminServiceV1ModelProviderResponse.

        Email address to receive business related emails  # noqa: E501

        :param email_business: The email_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :type: str
        """

        self._email_business = email_business

    @property
    def phone_business(self):
        """Gets the phone_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501

        Phone to be contact for business related enquiries  # noqa: E501

        :return: The phone_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone_business

    @phone_business.setter
    def phone_business(self, phone_business):
        """Sets the phone_business of this DomainListingAdminServiceV1ModelProviderResponse.

        Phone to be contact for business related enquiries  # noqa: E501

        :param phone_business: The phone_business of this DomainListingAdminServiceV1ModelProviderResponse.  # noqa: E501
        :type: str
        """

        self._phone_business = phone_business

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
        if issubclass(DomainListingAdminServiceV1ModelProviderResponse, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
