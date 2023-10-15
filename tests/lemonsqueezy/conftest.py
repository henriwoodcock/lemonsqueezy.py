import pytest

from lemonsqueezy import LemonSqueezy


@pytest.fixture
def api_key():
    return 'test'


@pytest.fixture
def ls(api_key):
    return LemonSqueezy(api_key)
