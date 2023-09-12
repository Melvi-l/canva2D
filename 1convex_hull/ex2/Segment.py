from Vertex import Vertex


class Segment:
    def __init__(self, a: Vertex, b: Vertex) -> None:
        self.a = a
        self.b = b
    def reverse(self) -> None:
        tmp = self.a
        self.a = self.b
        self.b = tmp
    def __str__(self) -> str:
        return f"(a: {self.a}, b: {self.b}])"