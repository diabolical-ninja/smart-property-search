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


class SchoolsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def schools_get(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schools_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: School identifier (required)
        :return: DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schools_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.schools_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def schools_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schools_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: School identifier (required)
        :return: DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool
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
                    " to method schools_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `schools_get`")  # noqa: E501

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
            ['application/json', 'text/json', 'text/html', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/locations/schools/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schools_search(self, **kwargs):  # noqa: E501
        """Searches schools based on specified criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schools_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str coordinate: Filter schools to include the specified coordinate in their catchment area (lat,long)
        :return: list[DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schools_search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.schools_search_with_http_info(**kwargs)  # noqa: E501
            return data

    def schools_search_with_http_info(self, **kwargs):  # noqa: E501
        """Searches schools based on specified criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schools_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str coordinate: Filter schools to include the specified coordinate in their catchment area (lat,long)
        :return: list[DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coordinate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schools_search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'coordinate' in params:
            query_params.append(('coordinate', params['coordinate']))  # noqa: E501

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
            '/v1/locations/schools', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
