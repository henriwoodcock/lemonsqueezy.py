from typing import Literal, TypedDict, Optional, Dict


QueryApiOptions = TypedDict(
    'QueryApiOptions',
    {
        'path': str,
        'method': Literal['POST', 'GET', 'PATCH', 'DELETE'],
        'params': Optional[any],
        'payload': Optional[dict]
    }
)
