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


class DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers(object):
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
        'advertiser_type': 'str',
        'advertiser_id': 'int',
        'contact_ids': 'list[int]',
        'agent_ids': 'list[str]',
        'conjunction_contact_ids': 'list[int]',
        'conjunction_agent_ids': 'list[str]'
    }

    attribute_map = {
        'advertiser_type': 'advertiserType',
        'advertiser_id': 'advertiserId',
        'contact_ids': 'contactIds',
        'agent_ids': 'agentIds',
        'conjunction_contact_ids': 'conjunctionContactIds',
        'conjunction_agent_ids': 'conjunctionAgentIds'
    }

    def __init__(self, advertiser_type=None, advertiser_id=None, contact_ids=None, agent_ids=None, conjunction_contact_ids=None, conjunction_agent_ids=None):  # noqa: E501
        """DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers - a model defined in Swagger"""  # noqa: E501

        self._advertiser_type = None
        self._advertiser_id = None
        self._contact_ids = None
        self._agent_ids = None
        self._conjunction_contact_ids = None
        self._conjunction_agent_ids = None
        self.discriminator = None

        if advertiser_type is not None:
            self.advertiser_type = advertiser_type
        if advertiser_id is not None:
            self.advertiser_id = advertiser_id
        if contact_ids is not None:
            self.contact_ids = contact_ids
        if agent_ids is not None:
            self.agent_ids = agent_ids
        if conjunction_contact_ids is not None:
            self.conjunction_contact_ids = conjunction_contact_ids
        if conjunction_agent_ids is not None:
            self.conjunction_agent_ids = conjunction_agent_ids

    @property
    def advertiser_type(self):
        """Gets the advertiser_type of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501


        :return: The advertiser_type of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_type

    @advertiser_type.setter
    def advertiser_type(self, advertiser_type):
        """Sets the advertiser_type of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.


        :param advertiser_type: The advertiser_type of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :type: str
        """
        allowed_values = ["agency", "private"]  # noqa: E501
        if advertiser_type not in allowed_values:
            raise ValueError(
                "Invalid value for `advertiser_type` ({0}), must be one of {1}"  # noqa: E501
                .format(advertiser_type, allowed_values)
            )

        self._advertiser_type = advertiser_type

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501


        :return: The advertiser_id of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :rtype: int
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.


        :param advertiser_id: The advertiser_id of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :type: int
        """

        self._advertiser_id = advertiser_id

    @property
    def contact_ids(self):
        """Gets the contact_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501


        :return: The contact_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :rtype: list[int]
        """
        return self._contact_ids

    @contact_ids.setter
    def contact_ids(self, contact_ids):
        """Sets the contact_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.


        :param contact_ids: The contact_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :type: list[int]
        """

        self._contact_ids = contact_ids

    @property
    def agent_ids(self):
        """Gets the agent_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501


        :return: The agent_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        """Sets the agent_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.


        :param agent_ids: The agent_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :type: list[str]
        """

        self._agent_ids = agent_ids

    @property
    def conjunction_contact_ids(self):
        """Gets the conjunction_contact_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501


        :return: The conjunction_contact_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :rtype: list[int]
        """
        return self._conjunction_contact_ids

    @conjunction_contact_ids.setter
    def conjunction_contact_ids(self, conjunction_contact_ids):
        """Sets the conjunction_contact_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.


        :param conjunction_contact_ids: The conjunction_contact_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :type: list[int]
        """

        self._conjunction_contact_ids = conjunction_contact_ids

    @property
    def conjunction_agent_ids(self):
        """Gets the conjunction_agent_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501


        :return: The conjunction_agent_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :rtype: list[str]
        """
        return self._conjunction_agent_ids

    @conjunction_agent_ids.setter
    def conjunction_agent_ids(self, conjunction_agent_ids):
        """Sets the conjunction_agent_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.


        :param conjunction_agent_ids: The conjunction_agent_ids of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.  # noqa: E501
        :type: list[str]
        """

        self._conjunction_agent_ids = conjunction_agent_ids

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
        if issubclass(DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers, dict):
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
        if not isinstance(other, DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
