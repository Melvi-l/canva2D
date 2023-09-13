from typing import List

from Vertex import Vertex


class Triangle:
    def __init__(self, vertexList: List[Vertex], neighbor: List) -> None:
        self.vertexList = vertexList
        self.neighbors = neighbor