from typing import List


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
class Segment:
    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b

class Polygon: 
    def __init__(self, segmentList: List[Segment]) -> None:
        self.segmentList = segmentList