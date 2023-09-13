from typing import List

from Vertex import Vertex
from Segment import Segment


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
    