from http import HTTPStatus
from lemonsqueezy import LemonSqueezy
from tests.utils import MockResponse


def test_get_user(ls: LemonSqueezy, api_key, mocker):
    user = {
        'atttributes': {
            'name': 'my-name',
            'email': 'my-email',
            'color': 'red',
            'avatar_url': 'https://url.com',
            'has_custom_avatar': True,
            'createdAt': '2023-01-01',
            'updatedAt': '2023-01-01'
        }
    }
    mocked = mocker.patch(
        'lemonsqueezy.requests.request',
        return_value=MockResponse(
            json_data={'data': user},
            status_code=HTTPStatus.OK,
            reason='OK'
        )
    )
    with mocked:
        returned = ls.get_user()

    assert returned == {'data': user}

    kwargs = {
        'headers': {
            'Accept': 'application/vnd.api+json',
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/vnd.api+json'
        }
    }
    mocked.assert_called_once_with(
        'GET', f'{ls.apiUrl}/v1/users/me', **kwargs
    )
