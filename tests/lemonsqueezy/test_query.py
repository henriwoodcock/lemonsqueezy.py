from http import HTTPStatus

import pytest

from lemonsqueezy import LemonSqueezy, LemonSqueezyError
from tests.utils import MockResponse


@pytest.mark.parametrize(
    'ops, resp, is_delete',
    (
        (
            {
                'method': 'GET',
                'path': 'my-path'
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'GET',
                'path': 'my-path',
                'params': {'my-param': 'value'}
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'GET',
                'path': 'my-path',
                'params': {'my-param': 'value'}
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'PATCH',
                'path': 'my-path',
                'params': {'my-param': 'value'},
                'payload': {'my-payload': 'value'}
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'PATCH',
                'path': 'my-path',
                'payload': {'my-payload': 'value'}
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'PATCH',
                'path': 'my-path',
                'params': {'my-param': 'value'},
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'POST',
                'path': 'my-path',
                'params': {'my-param': 'value'},
                'payload': {'my-payload': 'value'}
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'POST',
                'path': 'my-path',
                'payload': {'my-payload': 'value'}
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'POST',
                'path': 'my-path',
                'params': {'my-param': 'value'},
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            False
        ),
        (
            {
                'method': 'DELETE',
                'path': 'my-path',
                'params': {'my-param': 'value'},
                'payload': {'my-payload': 'value'}
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            True
        ),
        (
            {
                'method': 'DELETE',
                'path': 'my-path',
                'payload': {'my-payload': 'value'}
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            True
        ),
        (
            {
                'method': 'DELETE',
                'path': 'my-path',
                'params': {'my-param': 'value'},
            },
            {
                'json_data': {'my-key': 'value'},
                'reason': 'ok'
            },
            True
        ),
    )
)
@pytest.mark.parametrize(
    'status_code',
    (
        HTTPStatus.OK,
        HTTPStatus.CREATED,
        HTTPStatus.ACCEPTED,
    )
)
def test_query_ok(
    ls: LemonSqueezy, api_key, ops, resp, is_delete, mocker,
    status_code
):
    resp['status_code'] = status_code
    mocked = mocker.patch(
        'lemonsqueezy.requests.request', return_value=MockResponse(**resp)
    )
    returned = ls._query(ops)
    assert returned is None if is_delete else resp['json_data']
    kwargs = {
        'headers': {
            'Accept': 'application/vnd.api+json',
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/vnd.api+json'
        }
    }
    params = ops.get('params', None)
    payload = ops.get('payload', None)
    if params:
        kwargs['params'] = params
    if payload:
        kwargs['json'] = payload
    mocked.assert_called_once_with(
        ops['method'], f'{ls.apiUrl}/my-path', **kwargs
    )


@pytest.mark.parametrize(
    'ops, resp',
    (
        (
            {
                'method': 'POST',
                'path': 'my-path',
                'payload': {'my-payload': 'value'}
            },
            {
                'json_data': {
                    'my-key': 'value',
                    'errors': ['error-1']
                },
                'reason': 'error-reason',
            },
        ),
        (
            {
                'method': 'DELETE',
                'path': 'my-path',
            },
            {
                'json_data': {
                    'my-key': 'value',
                    'errors': ['error-2']
                },
                'reason': 'error-reason-2',
            },
        ),
    )
)
@pytest.mark.parametrize(
    'status_code',
    (
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.CONTINUE,
    )
)
def test_query_error(
    ls: LemonSqueezy, api_key, ops, resp, mocker,
    status_code
):
    resp['status_code'] = status_code
    mocked = mocker.patch(
        'lemonsqueezy.requests.request', return_value=MockResponse(**resp)
    )
    with pytest.raises(LemonSqueezyError) as exc:
        ls._query(ops)
    assert exc.value.message == resp['reason']
    assert exc.value.errors == resp['json_data']['errors']
    assert exc.value.status == status_code
    kwargs = {
        'headers': {
            'Accept': 'application/vnd.api+json',
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/vnd.api+json'
        }
    }
    params = ops.get('params', None)
    payload = ops.get('payload', None)
    if params:
        kwargs['params'] = params
    if payload:
        kwargs['json'] = payload
    mocked.assert_called_once_with(
        ops['method'], f'{ls.apiUrl}/my-path', **kwargs
    )
