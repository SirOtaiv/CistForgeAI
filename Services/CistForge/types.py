from typing import TypedDict, Tuple

class ImageConfig(TypedDict):
    color: Tuple[int, int, int]
    thickness: int