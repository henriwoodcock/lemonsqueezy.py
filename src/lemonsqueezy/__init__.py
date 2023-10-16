import re
from typing import Dict, List, Optional
import requests
from lemonsqueezy.types.api import (
    ProductResponse, ProductsResponse, StoreResponse, StoresResponse,
    UserResponse
)

from lemonsqueezy.types.methods import (
    GetProductOptions, GetProductsOptions, GetStoreOptions, GetStoresOptions,
    QueryApiOptions
)


class LemonSqueezyError(Exception):
    def __init__(self, status, message, errors):
        self.status = status
        self.message = message
        self.errors = errors

    def __repr__(self) -> str:
        return f'LemonSqueezyError({self.message})'


class LemonSqueezy:
    apiUrl = "https://api.lemonsqueezy.com"

    def __init__(self, api_key: str):
        """ LemonSqueezy API client

        Args:
            api_key (str): Your LemonSqueezy API key
        """
        self.api_key = api_key

    def _build_params(
        self, args: Dict[str, any], allowed_filters: Optional[List[str]]=[]
    ) -> Dict[str, any]:
        """ Builds a params object for the API query based on provided and
        allowed filters.

        Also converts pagination parameters `page` to `page[number]` and
        `perPage` to `page[size]`

        Args:
            args (Dict[str, any]): Arguments to the API method
            allowedFilters (List[str]): List of filters the API query permits
                                        (camelCase)

        Returns:
            Dict[str, any]: Built params for query
        """
        params = {}
        for filter_name in args:
            if filter_name in allowed_filters:
                query_filter = re.sub(
                    r'(?<!^)(?=[A-Z])', '_', filter_name
                ).lower()
                params["filter[" + query_filter + "]"] = args[filter_name];
            else:
                if filter_name == 'include':
                    params['include'] = args[filter_name]
                elif filter_name == 'page':
                    params['page[number]'] = args[filter_name]
                elif filter_name == 'perPage':
                    params['page[size]'] = args[filter_name]
        return params;

    def _query(self, ops: QueryApiOptions) -> dict:
        """ Send an API query to the LemonSqueezy API

        Args:
            ops (QueryApiOptions): API options to pass to the server

        Raises:
            LemonSqueezyError: When a non 200 response is returned

        Returns:
            dict: JSON response
        """
        path = ops['path']
        method = ops.get('method', 'GET')
        params = ops.get('params', None)
        payload = ops.get('payload', None)

        url = f'{self.apiUrl}/{path}'

        headers = {
            'Accept': 'application/vnd.api+json',
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/vnd.api+json'
        }

        kwargs = {}
        if params is not None:
            kwargs['params'] = params
        if payload is not None:
            kwargs['json'] = payload

        resp = requests.request(method, url, headers=headers, **kwargs)
        if not (200 <= resp.status_code <= 299):
            errors = resp.json()
            raise LemonSqueezyError(
                status=resp.status_code,
                message=resp.reason,
                errors=errors['errors']
            )
        if method != 'DELETE':
            return resp.json()

    def get_user(self) -> UserResponse:
        """ Get current user

        Returns:
            UserResponse: JSON
        """
        return self._query({'path': 'v1/users/me'})

    def get_stores(self, params: GetStoresOptions={}) -> StoresResponse:
        """ Get stores

        Args:
            params (GetStoresOptions, optional). Defaults to {}.

        Returns:
            StoresResponse: JSON
        """
        return self._query(
            {
                'path': 'v1/stores',
                'params': self._build_params(params)
            }
        )

    def get_store(self, params: GetStoreOptions) -> StoreResponse:
        """ Get store

        Args:
            params: GetStoreOptions.

        Raises:
            ValueError: If id is missing

        Returns:
            StoreResponse: JSON
        """
        id_ = params.pop('id', None)
        if id_ is None:
            raise ValueError('id is required')
        return self._query(
            {
                'path': f'v1/stores/{id_}',
                'params': self._build_params(params),
            }
        )

    def get_products(self, params: GetProductsOptions={}) -> ProductsResponse:
        """ Get products

        Args:
            params (GetProductsOptions, optional). Defaults to {}.

        Returns:
            ProductsResponse: JSON
        """
        return self._query({
            'path': 'v1/products',
            'params': self._build_params(params, ['storeId']),
        });


    def get_product(self, params: GetProductOptions) -> ProductResponse:
        """ Get a product

        Args:
            params GetProductOptions.

        Returns:
            ProductResponse: JSON
        """
        id_ = params.pop('id', None)
        if id_ is None:
            raise ValueError('id is required')
        return self._query({
            'path': f'v1/products/{id_}',
            'params': self._build_params(params),
        });
