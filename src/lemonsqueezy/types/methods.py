from typing import Literal, TypedDict, Optional, List


QueryApiOptions = TypedDict(
    'QueryApiOptions',
    {
        'path': str,
        'method': Literal['POST', 'GET', 'PATCH', 'DELETE'],
        'params': Optional[any],
        'payload': Optional[dict]
    }
)


PaginatedOptions = TypedDict(
    'PaginatedOptions',
    {
        'perPage': int,
        'page': int
    }
)


class GetStoresOptions(PaginatedOptions):
    include: List[
        Literal[
            'products',
            'discounts',
            'license-keys',
            'subscriptions',
            'webhooks'
        ]
    ]
