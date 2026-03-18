from typing import TypedDict, Optional

class DataState(TypedDict):
    dataset: str
    profile: Optional[str]
    analysis: Optional[str]
    model: Optional[str]