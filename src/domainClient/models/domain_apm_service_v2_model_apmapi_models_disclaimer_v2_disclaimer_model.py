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


class DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel(object):
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
        'version': 'str',
        'text': 'str',
        'imageurl': 'str',
        'authorityname': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'text': 'text',
        'imageurl': 'imageurl',
        'authorityname': 'authorityname'
    }

    def __init__(self, id=None, version=None, text=None, imageurl=None, authorityname=None):  # noqa: E501
        """DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._version = None
        self._text = None
        self._imageurl = None
        self._authorityname = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if text is not None:
            self.text = text
        if imageurl is not None:
            self.imageurl = imageurl
        if authorityname is not None:
            self.authorityname = authorityname

    @property
    def id(self):
        """Gets the id of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501


        :return: The id of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.


        :param id: The id of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501


        :return: The version of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.


        :param version: The version of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def text(self):
        """Gets the text of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501


        :return: The text of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.


        :param text: The text of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def imageurl(self):
        """Gets the imageurl of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501


        :return: The imageurl of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :rtype: str
        """
        return self._imageurl

    @imageurl.setter
    def imageurl(self, imageurl):
        """Sets the imageurl of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.


        :param imageurl: The imageurl of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :type: str
        """

        self._imageurl = imageurl

    @property
    def authorityname(self):
        """Gets the authorityname of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501


        :return: The authorityname of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :rtype: str
        """
        return self._authorityname

    @authorityname.setter
    def authorityname(self, authorityname):
        """Sets the authorityname of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.


        :param authorityname: The authorityname of this DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel.  # noqa: E501
        :type: str
        """

        self._authorityname = authorityname

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
        if issubclass(DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel, dict):
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
        if not isinstance(other, DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
