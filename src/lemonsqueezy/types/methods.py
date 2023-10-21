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


StoreInclude = Optional[
    List[
        Literal[
            'products', 'discounts', 'license-keys', 'subscriptions',
            'webhooks'
        ]
    ]
]


class GetStoresOptions(PaginatedOptions):
    include: StoreInclude


GetStoreOptions = TypedDict(
    'GetStoreOptions',
    {
        'id': str,
        'include': StoreInclude
    }
)


ProductInclude = Optional[List[Literal['store', 'variants']]]


class GetProductsOptions(PaginatedOptions):
    include: ProductInclude
    storeId: int


GetProductOptions = TypedDict(
    'GetProductOptions',
    {
        'id': str,
        'include': ProductInclude
    }
)


VariantInclude = Optional[List[Literal['product', 'files']]]


class GetVariantsOptions(PaginatedOptions):
    include: VariantInclude
    productId: Optional[int]


GetVariantOptions = TypedDict(
    'GetVariantOptions',
    {
        'id': str,
        'include': VariantInclude
    }
)


PriceInclude = Optional[List[Literal['variant']]]


class GetPricesOptions(PaginatedOptions):
    include: PriceInclude
    variantId: Optional[int]


GetPriceOptions = TypedDict(
    'GetPriceOptions',
    {
        'id': int,
        'include': PriceInclude
    }
)
