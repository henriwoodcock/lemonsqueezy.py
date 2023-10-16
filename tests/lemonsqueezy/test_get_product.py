from http import HTTPStatus

from lemonsqueezy import LemonSqueezy
from tests.utils import MockResponse


def test_get_product(ls: LemonSqueezy, api_key, mocker):
    product = {
        'attributes': {
            'stored_id': 1,
            'name': 'prod',
            'slug': 'slug-1',
            'description': 'my prod',
            'status': 'draft',
            'status_formatted': 'Draft',
            'thumb_url': 'https://url.com',
            'large_thumb_url': 'https://url.com',
            'price': 10,
            'price_formatted': '$0.10',
            'from_price': '1000',
            'to_price': None,
            'pay_what_you_want': False,
            'buy_now_url': 'https://url.com',
            'created_at': '2023-01-01T00:00:00.000z',
            'updated_at': '2023-01-01T00:00:00.000z',
            'test_mode': True
        }
    }
    mocked = mocker.patch(
        'lemonsqueezy.requests.request',
        return_value=MockResponse(
            json_data={'data': product},
            status_code=HTTPStatus.OK,
            reason='OK'
        )
    )
    returned = ls.get_product({'id': 1})

    assert returned == {'data': product}

    kwargs = {
        'headers': {
            'Accept': 'application/vnd.api+json',
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/vnd.api+json'
        },
        'params': {}
    }
    mocked.assert_called_once_with(
        'GET', f'{ls.apiUrl}/v1/products/1', **kwargs
    )
