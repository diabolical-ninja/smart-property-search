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


class SalesResultsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sales_results_get(self, city, **kwargs):  # noqa: E501
        """Retrieves sales results for a given city  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sales_results_get(city, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str city: City. Supported cities are: `Sydney`, `Melbourne`, `Brisbane`, `Adelaide`, `Canberra` (required)
        :return: DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sales_results_get_with_http_info(city, **kwargs)  # noqa: E501
        else:
            (data) = self.sales_results_get_with_http_info(city, **kwargs)  # noqa: E501
            return data

    def sales_results_get_with_http_info(self, city, **kwargs):  # noqa: E501
        """Retrieves sales results for a given city  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sales_results_get_with_http_info(city, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str city: City. Supported cities are: `Sydney`, `Melbourne`, `Brisbane`, `Adelaide`, `Canberra` (required)
        :return: DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['city']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sales_results_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'city' is set
        if ('city' not in params or
                params['city'] is None):
            raise ValueError("Missing the required parameter `city` when calling `sales_results_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'city' in params:
            path_params['city'] = params['city']  # noqa: E501

        query_params = []

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
            '/v1/salesResults/{city}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sales_results_head(self, **kwargs):  # noqa: E501
        """Retrieves metadata regarding sales result data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sales_results_head(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsDate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sales_results_head_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sales_results_head_with_http_info(**kwargs)  # noqa: E501
            return data

    def sales_results_head_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves metadata regarding sales result data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sales_results_head_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsDate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sales_results_head" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/v1/salesResults/_head', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsDate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sales_results_listings(self, city, **kwargs):  # noqa: E501
        """Retrieves listing summaries corresponding to the sales results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sales_results_listings(city, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str city: City. Supported cities are: `Sydney`, `Melbourne`, `Brisbane`, `Adelaide`, `Canberra` (required)
        :return: list[DomainPublicAdapterWebApiModelsV1SalesResultsListingSummary]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sales_results_listings_with_http_info(city, **kwargs)  # noqa: E501
        else:
            (data) = self.sales_results_listings_with_http_info(city, **kwargs)  # noqa: E501
            return data

    def sales_results_listings_with_http_info(self, city, **kwargs):  # noqa: E501
        """Retrieves listing summaries corresponding to the sales results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sales_results_listings_with_http_info(city, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str city: City. Supported cities are: `Sydney`, `Melbourne`, `Brisbane`, `Adelaide`, `Canberra` (required)
        :return: list[DomainPublicAdapterWebApiModelsV1SalesResultsListingSummary]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['city']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sales_results_listings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'city' is set
        if ('city' not in params or
                params['city'] is None):
            raise ValueError("Missing the required parameter `city` when calling `sales_results_listings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'city' in params:
            path_params['city'] = params['city']  # noqa: E501

        query_params = []

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
            '/v1/salesResults/{city}/listings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainPublicAdapterWebApiModelsV1SalesResultsListingSummary]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
