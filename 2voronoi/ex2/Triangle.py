from typing import List

from Vertex import Vertex


class Triangle:
    def __init__(self, vertexList: List[Vertex], neighborList: List) -> None:
        self.vertexList = vertexList
        self.neighborList = neighborList
        while len(neighborList) < 3:
            neighborList.append(None)
    def __str__(self) -> str:
        return f"({self.vertexList[0]}, {self.vertexList[1]}, {self.vertexList[2]})"