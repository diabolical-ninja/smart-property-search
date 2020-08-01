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


class DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase(object):
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
        'agency': 'DomainPublicAdapterWebApiModelsV1PropertiesTimelineAgency',
        'days_on_market': 'float',
        'event_date': 'datetime',
        'event_price': 'int',
        'price_description': 'str',
        'is_major_event': 'bool',
        'is_price_warning': 'bool',
        'advert_id': 'int'
    }

    attribute_map = {
        'category': 'category',
        'agency': 'agency',
        'days_on_market': 'daysOnMarket',
        'event_date': 'eventDate',
        'event_price': 'eventPrice',
        'price_description': 'priceDescription',
        'is_major_event': 'isMajorEvent',
        'is_price_warning': 'isPriceWarning',
        'advert_id': 'advertId'
    }

    def __init__(self, category=None, agency=None, days_on_market=None, event_date=None, event_price=None, price_description=None, is_major_event=None, is_price_warning=None, advert_id=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._agency = None
        self._days_on_market = None
        self._event_date = None
        self._event_price = None
        self._price_description = None
        self._is_major_event = None
        self._is_price_warning = None
        self._advert_id = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if agency is not None:
            self.agency = agency
        if days_on_market is not None:
            self.days_on_market = days_on_market
        if event_date is not None:
            self.event_date = event_date
        if event_price is not None:
            self.event_price = event_price
        if price_description is not None:
            self.price_description = price_description
        if is_major_event is not None:
            self.is_major_event = is_major_event
        if is_price_warning is not None:
            self.is_price_warning = is_price_warning
        if advert_id is not None:
            self.advert_id = advert_id

    @property
    def category(self):
        """Gets the category of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets the category, whether this is a sale information or rental information.  # noqa: E501

        :return: The category of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets the category, whether this is a sale information or rental information.  # noqa: E501

        :param category: The category of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["Sale", "Rental"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def agency(self):
        """Gets the agency of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets or sets the agency associated with this timeline data.  # noqa: E501

        :return: The agency of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: DomainPublicAdapterWebApiModelsV1PropertiesTimelineAgency
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets or sets the agency associated with this timeline data.  # noqa: E501

        :param agency: The agency of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: DomainPublicAdapterWebApiModelsV1PropertiesTimelineAgency
        """

        self._agency = agency

    @property
    def days_on_market(self):
        """Gets the days_on_market of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets or sets the number of days the advert is on market (if applicable).  # noqa: E501

        :return: The days_on_market of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: float
        """
        return self._days_on_market

    @days_on_market.setter
    def days_on_market(self, days_on_market):
        """Sets the days_on_market of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets or sets the number of days the advert is on market (if applicable).  # noqa: E501

        :param days_on_market: The days_on_market of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: float
        """

        self._days_on_market = days_on_market

    @property
    def event_date(self):
        """Gets the event_date of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets or sets the date related with this timeline data.  # noqa: E501

        :return: The event_date of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: datetime
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets or sets the date related with this timeline data.  # noqa: E501

        :param event_date: The event_date of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: datetime
        """

        self._event_date = event_date

    @property
    def event_price(self):
        """Gets the event_price of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets or sets the price to be displayed for this timeline data.  # noqa: E501

        :return: The event_price of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: int
        """
        return self._event_price

    @event_price.setter
    def event_price(self, event_price):
        """Sets the event_price of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets or sets the price to be displayed for this timeline data.  # noqa: E501

        :param event_price: The event_price of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: int
        """

        self._event_price = event_price

    @property
    def price_description(self):
        """Gets the price_description of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets or sets the description related with the price information.  # noqa: E501

        :return: The price_description of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: str
        """
        return self._price_description

    @price_description.setter
    def price_description(self, price_description):
        """Sets the price_description of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets or sets the description related with the price information.  # noqa: E501

        :param price_description: The price_description of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: str
        """

        self._price_description = price_description

    @property
    def is_major_event(self):
        """Gets the is_major_event of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets or sets a value indicating whether this timeline data is a major event.  # noqa: E501

        :return: The is_major_event of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: bool
        """
        return self._is_major_event

    @is_major_event.setter
    def is_major_event(self, is_major_event):
        """Sets the is_major_event of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets or sets a value indicating whether this timeline data is a major event.  # noqa: E501

        :param is_major_event: The is_major_event of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: bool
        """

        self._is_major_event = is_major_event

    @property
    def is_price_warning(self):
        """Gets the is_price_warning of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets or sets a value indicating if this timeline contains price warning information  # noqa: E501

        :return: The is_price_warning of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: bool
        """
        return self._is_price_warning

    @is_price_warning.setter
    def is_price_warning(self, is_price_warning):
        """Sets the is_price_warning of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets or sets a value indicating if this timeline contains price warning information  # noqa: E501

        :param is_price_warning: The is_price_warning of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: bool
        """

        self._is_price_warning = is_price_warning

    @property
    def advert_id(self):
        """Gets the advert_id of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501

        Gets or sets the advert identifier.  # noqa: E501

        :return: The advert_id of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :rtype: int
        """
        return self._advert_id

    @advert_id.setter
    def advert_id(self, advert_id):
        """Sets the advert_id of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.

        Gets or sets the advert identifier.  # noqa: E501

        :param advert_id: The advert_id of this DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase.  # noqa: E501
        :type: int
        """

        self._advert_id = advert_id

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
        if issubclass(DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1PropertiesTimelineBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
