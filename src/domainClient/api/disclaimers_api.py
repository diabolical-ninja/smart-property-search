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


class DisclaimersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def disclaimers_get(self, **kwargs):  # noqa: E501
        """Retrieves disclaimers for given ids  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disclaimers_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: Comma separated list of ids. Eg. \"1,2,3\"
        :return: list[DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.disclaimers_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.disclaimers_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def disclaimers_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves disclaimers for given ids  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disclaimers_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: Comma separated list of ids. Eg. \"1,2,3\"
        :return: list[DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disclaimers_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501

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
            '/v1/disclaimers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def disclaimers_get_by_product(self, product, **kwargs):  # noqa: E501
        """Retrieves disclaimers for given product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disclaimers_get_by_product(product, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product: Possible product values: `PropertyData`, `AURIN`, `HomePriceGuide` (required)
        :return: list[DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.disclaimers_get_by_product_with_http_info(product, **kwargs)  # noqa: E501
        else:
            (data) = self.disclaimers_get_by_product_with_http_info(product, **kwargs)  # noqa: E501
            return data

    def disclaimers_get_by_product_with_http_info(self, product, **kwargs):  # noqa: E501
        """Retrieves disclaimers for given product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disclaimers_get_by_product_with_http_info(product, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product: Possible product values: `PropertyData`, `AURIN`, `HomePriceGuide` (required)
        :return: list[DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disclaimers_get_by_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product' is set
        if ('product' not in params or
                params['product'] is None):
            raise ValueError("Missing the required parameter `product` when calling `disclaimers_get_by_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product' in params:
            path_params['product'] = params['product']  # noqa: E501

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
            '/v1/disclaimers/product/{product}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainAPMServiceV2ModelAPMAPIModelsDisclaimerV2DisclaimerModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
