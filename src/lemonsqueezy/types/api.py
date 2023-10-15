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
