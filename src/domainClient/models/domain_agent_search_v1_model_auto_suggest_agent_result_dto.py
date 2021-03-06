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


class DomainAgentSearchV1ModelAutoSuggestAgentResultDto(object):
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
        'agent_id': 'int',
        'name': 'str',
        'agency_name': 'str',
        'suburb': 'str',
        'state': 'str',
        'profile_url': 'str',
        'thumbnail': 'str'
    }

    attribute_map = {
        'agent_id': 'agentId',
        'name': 'name',
        'agency_name': 'agencyName',
        'suburb': 'suburb',
        'state': 'state',
        'profile_url': 'profileUrl',
        'thumbnail': 'thumbnail'
    }

    def __init__(self, agent_id=None, name=None, agency_name=None, suburb=None, state=None, profile_url=None, thumbnail=None):  # noqa: E501
        """DomainAgentSearchV1ModelAutoSuggestAgentResultDto - a model defined in Swagger"""  # noqa: E501

        self._agent_id = None
        self._name = None
        self._agency_name = None
        self._suburb = None
        self._state = None
        self._profile_url = None
        self._thumbnail = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if name is not None:
            self.name = name
        if agency_name is not None:
            self.agency_name = agency_name
        if suburb is not None:
            self.suburb = suburb
        if state is not None:
            self.state = state
        if profile_url is not None:
            self.profile_url = profile_url
        if thumbnail is not None:
            self.thumbnail = thumbnail

    @property
    def agent_id(self):
        """Gets the agent_id of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501


        :return: The agent_id of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :rtype: int
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.


        :param agent_id: The agent_id of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :type: int
        """

        self._agent_id = agent_id

    @property
    def name(self):
        """Gets the name of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501


        :return: The name of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.


        :param name: The name of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def agency_name(self):
        """Gets the agency_name of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501


        :return: The agency_name of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.


        :param agency_name: The agency_name of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :type: str
        """

        self._agency_name = agency_name

    @property
    def suburb(self):
        """Gets the suburb of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501


        :return: The suburb of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.


        :param suburb: The suburb of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

    @property
    def state(self):
        """Gets the state of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501


        :return: The state of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.


        :param state: The state of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def profile_url(self):
        """Gets the profile_url of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501


        :return: The profile_url of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        """Sets the profile_url of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.


        :param profile_url: The profile_url of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :type: str
        """

        self._profile_url = profile_url

    @property
    def thumbnail(self):
        """Gets the thumbnail of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501


        :return: The thumbnail of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.


        :param thumbnail: The thumbnail of this DomainAgentSearchV1ModelAutoSuggestAgentResultDto.  # noqa: E501
        :type: str
        """

        self._thumbnail = thumbnail

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
        if issubclass(DomainAgentSearchV1ModelAutoSuggestAgentResultDto, dict):
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
        if not isinstance(other, DomainAgentSearchV1ModelAutoSuggestAgentResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
