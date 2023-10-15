from typing import Literal, TypedDict, Optional, Dict


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
