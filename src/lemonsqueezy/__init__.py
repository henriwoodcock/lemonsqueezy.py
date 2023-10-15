from http import HTTPStatus
import requests
from lemonsqueezy.types.api import UserResponse

from lemonsqueezy.types.methods import QueryApiOptions


class LemonSqueezyError(Exception):
    def __init__(self, status, message, errors):
        self.status = status
        self.message = message
        self.errors = errors

    def __repr__(self) -> str:
        return f'LemonSqueezyError({self.message})'


class LemonSqueezy:
    apiUrl = "https://api.lemonsqueezy.com/"

    def __init__(self, api_key: str):
        """ LemonSqueezy API client

        Args:
            api_key (str): Your LemonSqueezy API key
        """
        self.api_key = api_key

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
