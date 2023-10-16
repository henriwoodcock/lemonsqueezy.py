from http import HTTPStatus

from lemonsqueezy import LemonSqueezy
from tests.utils import MockResponse


def test_get_store(ls: LemonSqueezy, api_key, mocker):
    store = {
        'attributes': {
            'name': 'store-1',
            'slug': 'slug-1',
            'domain': 'https://url.com',
            'url': 'https://url.com',
            'avatar_url': 'https://url.com',
            'plan': 'basic',
            'country': 'USA',
            'country_nicename': 'USA',
            'currency': 'USD',
            'total_sales': 1000,
            'total_revenue': 1000,
            'thirty_day_sales': 500,
            'thirty_day_revenue': 500,
            'createdAt': '2023-01-01',
            'updatedAt': '2023-01-01'
        }
    }
    mocked = mocker.patch(
        'lemonsqueezy.requests.request',
        return_value=MockResponse(
            json_data={'data': store},
            status_code=HTTPStatus.OK,
            reason='OK'
        )
    )
    returned = ls.get_store({'id': 1})

    assert returned == {'data': store}

    kwargs = {
        'headers': {
            'Accept': 'application/vnd.api+json',
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/vnd.api+json'
        },
        'params': {}
    }
    mocked.assert_called_once_with(
        'GET', f'{ls.apiUrl}/v1/stores/1', **kwargs
    )
