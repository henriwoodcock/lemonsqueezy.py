from lemonsqueezy import LemonSqueezy


def test_build_params(ls: LemonSqueezy):
    args = {
        'myFilter': 'some-filter',
        'notAllowedFilter': 'another-filter',
        'include': [1,2,3],
        'page': 1,
        'perPage': 10,
    }
    returned = ls._build_params(args, ['myFilter'])
    assert returned == {
        'filter[my_filter]': 'some-filter',
        'include': [1, 2, 3],
        'page[number]': 1,
        'page[size]': 10
    }
