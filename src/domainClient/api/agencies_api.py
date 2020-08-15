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


class AgenciesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def agencies_create_test_agency(self, **kwargs):  # noqa: E501
        """Creates a test agency  # noqa: E501

        Enables automatic creation of a test agency in our sandbox environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_create_test_agency(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DomainAgencyServiceV2ModelAgency
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agencies_create_test_agency_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.agencies_create_test_agency_with_http_info(**kwargs)  # noqa: E501
            return data

    def agencies_create_test_agency_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a test agency  # noqa: E501

        Enables automatic creation of a test agency in our sandbox environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_create_test_agency_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DomainAgencyServiceV2ModelAgency
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
                    " to method agencies_create_test_agency" % key
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
            '/v1/agencies/_testAgency', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainAgencyServiceV2ModelAgency',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agencies_get(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific agency details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :return: DomainAgencyServiceV2ModelAgency
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agencies_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.agencies_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def agencies_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific agency details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :return: DomainAgencyServiceV2ModelAgency
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
                    " to method agencies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `agencies_get`")  # noqa: E501

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
            '/v1/agencies/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainAgencyServiceV2ModelAgency',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agencies_get_bundle_contracts(self, id, **kwargs):  # noqa: E501
        """Retrieves the product bundle contracts applicable to the specific agency.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_bundle_contracts(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :return: list[DomainBookingServiceV1ModelProductBundleContractDetailsResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agencies_get_bundle_contracts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.agencies_get_bundle_contracts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def agencies_get_bundle_contracts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves the product bundle contracts applicable to the specific agency.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_bundle_contracts_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :return: list[DomainBookingServiceV1ModelProductBundleContractDetailsResponse]
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
                    " to method agencies_get_bundle_contracts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `agencies_get_bundle_contracts`")  # noqa: E501

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
            '/v1/agencies/{id}/bundlecontracts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainBookingServiceV1ModelProductBundleContractDetailsResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agencies_get_listings(self, id, **kwargs):  # noqa: E501
        """Retrieves listings across all channels for a specific agency matching specified criteria.  # noqa: E501

        Note that the result page size is clamped at 200.  Requesting a page size greater than this will be treated as if only a page size of 200 were requested.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_listings(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :param str listing_status_filter: Filter for listing status
        :param datetime date_updated_since: Filter to remove listings not updated since before the given date time
        :param int page_number: Page number for paginated results
        :param int page_size: Page size for paginated results
        :return: list[DomainPublicAdapterWebApiModelsV1ListingsListing]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agencies_get_listings_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.agencies_get_listings_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def agencies_get_listings_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves listings across all channels for a specific agency matching specified criteria.  # noqa: E501

        Note that the result page size is clamped at 200.  Requesting a page size greater than this will be treated as if only a page size of 200 were requested.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_listings_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :param str listing_status_filter: Filter for listing status
        :param datetime date_updated_since: Filter to remove listings not updated since before the given date time
        :param int page_number: Page number for paginated results
        :param int page_size: Page size for paginated results
        :return: list[DomainPublicAdapterWebApiModelsV1ListingsListing]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'listing_status_filter', 'date_updated_since', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agencies_get_listings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `agencies_get_listings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'listing_status_filter' in params:
            query_params.append(('listingStatusFilter', params['listing_status_filter']))  # noqa: E501
        if 'date_updated_since' in params:
            query_params.append(('dateUpdatedSince', params['date_updated_since']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/v1/agencies/{id}/listings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainPublicAdapterWebApiModelsV1ListingsListing]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agencies_get_statistics(self, id, **kwargs):  # noqa: E501
        """Retrieves statistics across all channels for a specific agency.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_statistics(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :param str time_period: Period to report on, Valid values are: `last7Days`, `last90Days`, `wholeCampaign`. Default is `last7Days`.
        :param str status_filter: Status to filter, Valid values are: `Live`, `LiveAndArchived`. Default is `LiveAndArchived`
        :param int page_number: Page number
        :param int page_size: Page size
        :return: list[DomainPublicAdapterWebApiModelsV1ListingsStatistics]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agencies_get_statistics_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.agencies_get_statistics_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def agencies_get_statistics_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves statistics across all channels for a specific agency.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_statistics_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :param str time_period: Period to report on, Valid values are: `last7Days`, `last90Days`, `wholeCampaign`. Default is `last7Days`.
        :param str status_filter: Status to filter, Valid values are: `Live`, `LiveAndArchived`. Default is `LiveAndArchived`
        :param int page_number: Page number
        :param int page_size: Page size
        :return: list[DomainPublicAdapterWebApiModelsV1ListingsStatistics]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'time_period', 'status_filter', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agencies_get_statistics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `agencies_get_statistics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'time_period' in params:
            query_params.append(('timePeriod', params['time_period']))  # noqa: E501
        if 'status_filter' in params:
            query_params.append(('statusFilter', params['status_filter']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/v1/agencies/{id}/statistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainPublicAdapterWebApiModelsV1ListingsStatistics]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agencies_get_subscriptions(self, id, **kwargs):  # noqa: E501
        """Retrieves the active subscriptions for the specific agency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_subscriptions(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :param str channel: Channel. Either `residential` or `commercial` (case insensitive). Defaults to `residential` if not provided
        :return: list[DomainAgencyServiceV1ModelAgencySubscriptionDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agencies_get_subscriptions_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.agencies_get_subscriptions_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def agencies_get_subscriptions_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves the active subscriptions for the specific agency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_get_subscriptions_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Agency identifier (required)
        :param str channel: Channel. Either `residential` or `commercial` (case insensitive). Defaults to `residential` if not provided
        :return: list[DomainAgencyServiceV1ModelAgencySubscriptionDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agencies_get_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `agencies_get_subscriptions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
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
            '/v1/agencies/{id}/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainAgencyServiceV1ModelAgencySubscriptionDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agencies_head(self, q, **kwargs):  # noqa: E501
        """Retrieves summary of agency search  # noqa: E501

        Given a specified agency search criteria, this endpoint can be used to ascertain the result count that can be expected.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_head(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: Search phrase.  e.g. name:\"Agency XYZ\" (required)
        :param int page_number: Page number for paginated results
        :param int page_size: Page size for paginated results
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agencies_head_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.agencies_head_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def agencies_head_with_http_info(self, q, **kwargs):  # noqa: E501
        """Retrieves summary of agency search  # noqa: E501

        Given a specified agency search criteria, this endpoint can be used to ascertain the result count that can be expected.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_head_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: Search phrase.  e.g. name:\"Agency XYZ\" (required)
        :param int page_number: Page number for paginated results
        :param int page_size: Page size for paginated results
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agencies_head" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `agencies_head`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/v1/agencies', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agencies_search(self, q, **kwargs):  # noqa: E501
        """Retrieves summary of agencies matching the specified criteria.  # noqa: E501

        <para>The <code>q</code> parameter supports:</para>  <ul>    <li>name: search by name eg. <code>name:\"Agency XYZ\"</code></li>    <li>providerId: search by providerId. eg. <code>providerId:\"ABC Software\"</code></li>    <li>domainUrl: search by domainUrl. eg. <code>domainUrl:\"agency-xyz\"</code></li>    <li>dateUpdated: search by dateUpdated. eg. <code>dateUpdated:\"2016-12-25\"</code></li>    <li>suburbId: search by suburbId. Lists supported.  eg. <code>suburbId:1</code> eg. <code>suburbId:(1 OR 2 OR 3)</code>.  Can include related suburbs by adding <code>in:related</code></li>    <li>accountType: search by account type. Lists supported.  eg. <code>accountType:residential</code> eg. <code>accountType:(residential OR commercial)</code> Valid values are: none, residential, commerciallight, commercialfull, developer, holiday, business</li>    <li>      <code>in:all</code> includes archived agencies (archived agencies excluded by default)</li>    <li>      <code>-is:selfservice</code> excludes selfservice</li>  </ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_search(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: Search phrase.  e.g. name:\"Agency XYZ\" (required)
        :param int page_number: Page number for paginated results
        :param int page_size: Page size for paginated results
        :return: list[DomainAgencyServiceV2ModelAgencySummary]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agencies_search_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.agencies_search_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def agencies_search_with_http_info(self, q, **kwargs):  # noqa: E501
        """Retrieves summary of agencies matching the specified criteria.  # noqa: E501

        <para>The <code>q</code> parameter supports:</para>  <ul>    <li>name: search by name eg. <code>name:\"Agency XYZ\"</code></li>    <li>providerId: search by providerId. eg. <code>providerId:\"ABC Software\"</code></li>    <li>domainUrl: search by domainUrl. eg. <code>domainUrl:\"agency-xyz\"</code></li>    <li>dateUpdated: search by dateUpdated. eg. <code>dateUpdated:\"2016-12-25\"</code></li>    <li>suburbId: search by suburbId. Lists supported.  eg. <code>suburbId:1</code> eg. <code>suburbId:(1 OR 2 OR 3)</code>.  Can include related suburbs by adding <code>in:related</code></li>    <li>accountType: search by account type. Lists supported.  eg. <code>accountType:residential</code> eg. <code>accountType:(residential OR commercial)</code> Valid values are: none, residential, commerciallight, commercialfull, developer, holiday, business</li>    <li>      <code>in:all</code> includes archived agencies (archived agencies excluded by default)</li>    <li>      <code>-is:selfservice</code> excludes selfservice</li>  </ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agencies_search_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: Search phrase.  e.g. name:\"Agency XYZ\" (required)
        :param int page_number: Page number for paginated results
        :param int page_size: Page size for paginated results
        :return: list[DomainAgencyServiceV2ModelAgencySummary]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agencies_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `agencies_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/v1/agencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainAgencyServiceV2ModelAgencySummary]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)