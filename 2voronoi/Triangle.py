from typing import List

from Vertex import Vertex


class Triangle:
    def __init__(self, vertexList: List[Vertex], neighbor: List) -> None:
        self.vertexList = vertexList
        self.neighbors = neighbor
        while len(neighbor) < 3:
            neighbor.append(None)
    def __str__(self) -> str:
        return f"({self.vertexList[0]}, {self.vertexList[1]}, {self.vertexList[2]})"