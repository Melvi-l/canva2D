from typing import List


class Vertex:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
class Segment:
    def __init__(self, a: Vertex, b: Vertex) -> None:
        self.a = a
        self.b = b

class Polygon: 
    def __init__(self, segmentList: List[Segment]) -> None:
        self.segmentList = segmentList
        self.isClose = False

    def addVertex(self, b: Vertex) -> None:
        a = self.segmentList[-1].b
        self.segmentList.append(Segment(a,b))

    def close(self) -> None:
        self.addVertex(self.segmentList[0].a)
        self.isClose = True
    