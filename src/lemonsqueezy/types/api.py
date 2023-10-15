from typing import List, Literal, TypedDict, Optional, Dict


BaseListResponse = TypedDict(
    'BaseListResponse',
    {
        'meta': dict,
        'jsonapi': {'version': Literal['1.0']},
        'links': dict,
        'included': Optional[Dict[str, any]]
    }
)


BaseIndividualResponse = TypedDict(
    'BaseIndividualResponse',
    {
        'jsonapi': {'version': Literal['1.0']},
        'links': dict,
        'included': Optional[Dict[str, any]]
    }
)


BaseApiObject = TypedDict(
    'BaseApiObject',
    {
        'type': str,
        'id': str,
        'relationships': dict,
        'links': dict,
    }
)


UserAttributes = TypedDict(
    'UserAttributes',
    {
        'name': str,
        'email': str,
        'color': str,
        'avatar_url': str,
        'has_custom_avatar': str,
        'createdAt': str,
        'updatedAt': str
    }
)


class UserObject(BaseApiObject):
    attributes: UserAttributes


class UserResponse(BaseIndividualResponse):
    data: UserObject


StoreAttributes = TypedDict(
    'StoreAttributes',
    {
        'name': str,
        'slug': str,
        'domain': str,
        'url': str,
        'avatar_url': str,
        'plan': str,
        'country': str,
        'country_nicename': str,
        'currency': str,
        'total_sales': int,
        'total_revenue': int,
        'thirty_day_sales': int,
        'thirty_day_revenue': int,
        'created_at': str,
        'updated_at': str,
    }
)


class StoreObject(BaseApiObject):
    attributes: StoreAttributes


class StoresResponse(BaseListResponse):
  data: List[StoreObject]


class StoreResponse(BaseIndividualResponse):
  data: StoreObject


ProductAttributes = TypedDict(
    'ProductionAttributes',
    {
       'stored_id': int,
       'name': str,
       'slug': str,
       'description': str,
       'status': Literal['draft', 'publish'],
       'status_formatted': Literal['Draft', 'Published'],
       'thumb_url': Optional[str],
       'large_thumb_url': Optional[str],
       'price': int,
       'price_formatted': str,
       'from_price': Optional[int],
       'to_price': Optional[int],
       'pay_what_you_want': bool,
       'buy_now_url': str,
       'created_at': str,
       'updated_at': str,
       'test_mode': bool
    }
)


class ProductObject(BaseApiObject):
   attributes: ProductAttributes


class ProductsResponse(BaseListResponse):
    data: List[ProductObject]

class ProductResponse(BaseIndividualResponse):
    data: ProductObject
