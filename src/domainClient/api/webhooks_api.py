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


class WebhooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def webhooks_create_subscription(self, id, subscription, **kwargs):  # noqa: E501
        """Creates a subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhooks_create_subscription(id, subscription, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Webhook identifier (required)
        :param DomainNotificationPortalV1ModelAddSubscriptionRequest subscription: Subscription data (required)
        :return: DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhooks_create_subscription_with_http_info(id, subscription, **kwargs)  # noqa: E501
        else:
            (data) = self.webhooks_create_subscription_with_http_info(id, subscription, **kwargs)  # noqa: E501
            return data

    def webhooks_create_subscription_with_http_info(self, id, subscription, **kwargs):  # noqa: E501
        """Creates a subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhooks_create_subscription_with_http_info(id, subscription, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Webhook identifier (required)
        :param DomainNotificationPortalV1ModelAddSubscriptionRequest subscription: Subscription data (required)
        :return: DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'subscription']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhooks_create_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `webhooks_create_subscription`")  # noqa: E501
        # verify the required parameter 'subscription' is set
        if ('subscription' not in params or
                params['subscription'] is None):
            raise ValueError("Missing the required parameter `subscription` when calling `webhooks_create_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscription' in params:
            body_params = params['subscription']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'text/html', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/webhooks/{id}/subscriptions', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhooks_delete_subscription(self, id, **kwargs):  # noqa: E501
        """Deletes a webhook subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhooks_delete_subscription(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Subscription identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhooks_delete_subscription_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.webhooks_delete_subscription_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def webhooks_delete_subscription_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes a webhook subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhooks_delete_subscription_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Subscription identifier (required)
        :return: None
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
                    " to method webhooks_delete_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `webhooks_delete_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/subscriptions/{id}', 'DELETE',
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

    def webhooks_get_subscription(self, id, **kwargs):  # noqa: E501
        """Retrieves a webhook subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhooks_get_subscription(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Subscription identifier (required)
        :return: DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhooks_get_subscription_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.webhooks_get_subscription_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def webhooks_get_subscription_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a webhook subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhooks_get_subscription_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Subscription identifier (required)
        :return: DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription
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
                    " to method webhooks_get_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `webhooks_get_subscription`")  # noqa: E501

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
            '/v1/subscriptions/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhooks_list_subscriptions(self, id, **kwargs):  # noqa: E501
        """Retreives all webhook subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhooks_list_subscriptions(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Subscriber (Webhook) ID (required)
        :param int page_number: 
        :param int page_size: 
        :return: list[DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhooks_list_subscriptions_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.webhooks_list_subscriptions_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def webhooks_list_subscriptions_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retreives all webhook subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhooks_list_subscriptions_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Subscriber (Webhook) ID (required)
        :param int page_number: 
        :param int page_size: 
        :return: list[DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhooks_list_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `webhooks_list_subscriptions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
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
            '/v1/webhooks/{id}/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainPublicAdapterWebApiModelsV1SubscriptionsSubscription]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
