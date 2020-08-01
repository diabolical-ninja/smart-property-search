# coding: utf-8

"""
    Domain Group API V1

    Provides public access to Domain's microservices  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from domainClient.api_client import ApiClient


class PropertiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def properties_get(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific property.  # noqa: E501

        Applicable [policies](/docs/support/policies) apply here include APM attribution and appropriate state government attribution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.properties_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Property identifier.  Use the `_suggest` resource to determine the propertyId. (required)
        :return: DomainPublicAdapterWebApiModelsV1PropertiesProperty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.properties_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.properties_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def properties_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific property.  # noqa: E501

        Applicable [policies](/docs/support/policies) apply here include APM attribution and appropriate state government attribution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.properties_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Property identifier.  Use the `_suggest` resource to determine the propertyId. (required)
        :return: DomainPublicAdapterWebApiModelsV1PropertiesProperty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method properties_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `properties_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/properties/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainPublicAdapterWebApiModelsV1PropertiesProperty',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def properties_get_price_estimate(self, id, **kwargs):  # noqa: E501
        """Retrieves the current price estimate for the given property.  # noqa: E501

        The price estimate data is refreshed monthly, typically towards the end of each month.    The price estimate provides a guide of the approximate market value for a property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.properties_get_price_estimate(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Property identifier.  Use the `_suggest` resource to determine the propertyId. (required)
        :return: DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.properties_get_price_estimate_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.properties_get_price_estimate_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def properties_get_price_estimate_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves the current price estimate for the given property.  # noqa: E501

        The price estimate data is refreshed monthly, typically towards the end of each month.    The price estimate provides a guide of the approximate market value for a property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.properties_get_price_estimate_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Property identifier.  Use the `_suggest` resource to determine the propertyId. (required)
        :return: DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method properties_get_price_estimate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `properties_get_price_estimate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/properties/{id}/priceEstimate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def properties_suggest(self, terms, **kwargs):  # noqa: E501
        """Provides property suggestions.  # noqa: E501

        Applicable [policies](/docs/support/policies) apply here include APM attribution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.properties_suggest(terms, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str terms: Terms on which to base suggestions (required)
        :param int page_size: Number of suggestions (maximum 20)
        :param str channel: Restrict the suggestions to this type of property: `All` (default), `Residential`, `Commercial`
        :return: list[DomainPublicAdapterWebApiModelsV1PropertiesPropertySuggestion]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.properties_suggest_with_http_info(terms, **kwargs)  # noqa: E501
        else:
            (data) = self.properties_suggest_with_http_info(terms, **kwargs)  # noqa: E501
            return data

    def properties_suggest_with_http_info(self, terms, **kwargs):  # noqa: E501
        """Provides property suggestions.  # noqa: E501

        Applicable [policies](/docs/support/policies) apply here include APM attribution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.properties_suggest_with_http_info(terms, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str terms: Terms on which to base suggestions (required)
        :param int page_size: Number of suggestions (maximum 20)
        :param str channel: Restrict the suggestions to this type of property: `All` (default), `Residential`, `Commercial`
        :return: list[DomainPublicAdapterWebApiModelsV1PropertiesPropertySuggestion]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['terms', 'page_size', 'channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method properties_suggest" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'terms' is set
        if ('terms' not in params or
                params['terms'] is None):
            raise ValueError("Missing the required parameter `terms` when calling `properties_suggest`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'terms' in params:
            query_params.append(('terms', params['terms']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'channel' in params:
            query_params.append(('channel', params['channel']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/properties/_suggest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainPublicAdapterWebApiModelsV1PropertiesPropertySuggestion]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
