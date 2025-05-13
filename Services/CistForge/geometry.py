from typing import List, NamedTuple, Tuple


class GeometryConfig(NamedTuple):
    points: List[Tuple[int, int]]
    size: int
    thickness: int
    color: Tuple[int, int, int]

def geometry_points_generate(x: int = 400, zPoint: int = 60 ) -> GeometryConfig:
    thicknes, color = 3, (0, 0, 0)

    aPoint, bPoint = (x // 2), (x - zPoint)
    tPoint = bPoint // 4

    pointBlocks = [
        (aPoint - tPoint, zPoint),             # 1
        (aPoint, zPoint),                      # 2
        (aPoint + tPoint, zPoint),             # 3

        (aPoint - tPoint, zPoint + tPoint),    # 4
        (aPoint, zPoint + tPoint),             # 5
        (aPoint + tPoint, zPoint + tPoint),    # 6

        (aPoint - tPoint, bPoint - tPoint),    # 7
        (aPoint, bPoint - tPoint),             # 8
        (aPoint + tPoint, bPoint - tPoint),    # 9

        (aPoint - tPoint, bPoint),             # 10
        (aPoint, bPoint),                      # 11
        (aPoint + tPoint, bPoint),             # 12
        ]
    
    return GeometryConfig(points=pointBlocks, size=x, thickness=thicknes, color=color)