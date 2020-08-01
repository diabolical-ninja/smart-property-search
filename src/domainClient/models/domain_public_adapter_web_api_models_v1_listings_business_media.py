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


class DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia(object):
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
        'date_created': 'datetime',
        'image_url': 'str',
        'media_type': 'str',
        'type': 'str',
        'video_url': 'str'
    }

    attribute_map = {
        'date_created': 'dateCreated',
        'image_url': 'imageUrl',
        'media_type': 'mediaType',
        'type': 'type',
        'video_url': 'videoUrl'
    }

    def __init__(self, date_created=None, image_url=None, media_type=None, type=None, video_url=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia - a model defined in Swagger"""  # noqa: E501

        self._date_created = None
        self._image_url = None
        self._media_type = None
        self._type = None
        self._video_url = None
        self.discriminator = None

        if date_created is not None:
            self.date_created = date_created
        if image_url is not None:
            self.image_url = image_url
        if media_type is not None:
            self.media_type = media_type
        if type is not None:
            self.type = type
        if video_url is not None:
            self.video_url = video_url

    @property
    def date_created(self):
        """Gets the date_created of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501

        Not used  # noqa: E501

        :return: The date_created of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.

        Not used  # noqa: E501

        :param date_created: The date_created of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def image_url(self):
        """Gets the image_url of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501

        Resource URL  # noqa: E501

        :return: The image_url of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.

        Resource URL  # noqa: E501

        :param image_url: The image_url of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def media_type(self):
        """Gets the media_type of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501

        Media type: \\\"image\\\", \\\"video\\\"  # noqa: E501

        :return: The media_type of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.

        Media type: \\\"image\\\", \\\"video\\\"  # noqa: E501

        :param media_type: The media_type of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def type(self):
        """Gets the type of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501

        Type: \\\"youtube\\\", \\\"vimeo\\\", \\\"mp4\\\"  # noqa: E501

        :return: The type of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.

        Type: \\\"youtube\\\", \\\"vimeo\\\", \\\"mp4\\\"  # noqa: E501

        :param type: The type of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def video_url(self):
        """Gets the video_url of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501

        Video URL  # noqa: E501

        :return: The video_url of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        """Sets the video_url of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.

        Video URL  # noqa: E501

        :param video_url: The video_url of this DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia.  # noqa: E501
        :type: str
        """

        self._video_url = video_url

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
        if issubclass(DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
