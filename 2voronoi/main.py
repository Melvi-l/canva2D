import math
import random
from typing import List, Tuple
from Triangle import Triangle
import pygame
import sys
from Vertex import Vertex

# Color
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 226, 82)

# Global
vertexList: List[Vertex] = []

pygame.init()
width = 1000
height = 1000
canvas = pygame.display.set_mode((width, height))
background = (0, 0, 0)
canvas.fill(background)
font = pygame.font.Font(None, 24)


def drawVertex(vertex, color=YELLOW, size=2):
    pygame.draw.circle(canvas, color, (vertex.x, vertex.y), size)


def drawEdge(start, stop, color=YELLOW, size=1):
    pygame.draw.line(canvas, color, (start.x,
                     start.y), (stop.x, stop.y), size)


def drawTriangle(triangle, color=YELLOW, size=1):
    drawEdge(triangle.vertexList[0], triangle.vertexList[1], color, size)
    drawEdge(triangle.vertexList[1], triangle.vertexList[2], color, size)
    drawEdge(triangle.vertexList[2], triangle.vertexList[0], color, size)

def drawTriangulation(triangulation):
    for triangle in triangulation: 
        drawTriangle(triangle)

def drawPolygon(polygon):
    for segment in polygon.segmentList:
        pygame.draw.line(canvas, YELLOW, (segment.a.x,
                                          segment.a.y), (segment.b.x, segment.b.y), 1)


def drawCircle(center, radius, color=WHITE, size=2):
    pygame.draw.circle(canvas, color, (center.x, center.y), radius, size)


def distance(vertexA, vertexB):
    return math.sqrt((vertexB.x - vertexA.x)**2 + (vertexB.y - vertexA.y)**2)
def createRandomVertex():
    VERTE_NB = 3
    for i in range(VERTE_NB):
        vertex = Vertex(random.randint(100, width-100),
                        random.randint(100, height-100))
        vertexList.append(vertex)
        drawVertex(vertex)


# emptyCircle
def findEmptyCircle(triangle: Triangle):
    edgeA = triangle.vertexList[0], triangle.vertexList[1]
    edgeB = triangle.vertexList[1], triangle.vertexList[2]
    centerVectorTupleA = findBisector(edgeA)
    centerVectorTupleB = findBisector(edgeB)
    circleCenter = findLineIntersection(centerVectorTupleA, centerVectorTupleB)
    circleRadius = distance(circleCenter, triangle.vertexList[0])
    drawEmptyCircle(circleCenter, circleRadius,
                    centerVectorTupleA[0], centerVectorTupleB[0])
    return circleCenter, circleRadius
def findBisector(edge: Tuple[Vertex, Vertex]):
    center = Vertex(
        (edge[0].x + edge[1].x)/2,
        (edge[0].y + edge[1].y)/2
    )
    orthoVector = Vertex(edge[1].y - edge[0].y, -edge[1].x + edge[0].x)
    # return lambda t: Vertex(orthoVector.x*t + center.x, orthoVector.y*t + center.y)
    return center, orthoVector
def findLineIntersection(centerVectorTupleA, centerVectorTupleB):
    centerA, vectorA = centerVectorTupleA
    centerB, vectorB = centerVectorTupleB
    tB = ((centerB.x - centerA.x) / vectorA.x - (centerB.y - centerA.y) /
          vectorA.y) / (vectorB.y / vectorA.y - vectorB.x / vectorA.x)
    return Vertex(vectorB.x*tB + centerB.x, vectorB.y*tB + centerB.y)
def drawEmptyCircle(center, radius, centerEdgeA, centerEdgeB):
    drawEdge(centerEdgeA, center, RED, 3)
    drawEdge(centerEdgeB, center, RED, 3)
    drawVertex(center, RED, 4)
    drawCircle(center, radius)

# testVertexInTriangle
let = lambda a, b: a.x * b.y - a.y * b.x
convertVector = lambda a, b: Vertex(b.x-a.x, b.y-a.y) 
def sign(a: float): 
    if a<0:
        return -1
    return 1
def classicInside(vertex, triangle):
    [A, B, C] = triangle.vertexList
    return sign(let(convertVector(A,B), convertVector(A, vertex))) == sign(let(convertVector(B,C), convertVector(B, vertex))) == sign(let(convertVector(C,A), convertVector(C, vertex)))
def barycentre(vertex, triangle):
    [A, B, C] = triangle.vertexList
    totalSurface = abs((B.x - A.x) * (C.y - A.y) - (C.x - A.x) * (B.y - A.y))
    surfaceA = abs((vertex.x - B.x) * (C.y - B.y) -
                   (C.x - B.x) * (vertex.y - B.y))
    surfaceB = abs((vertex.x - A.x) * (C.y - A.y) -
                   (C.x - A.x) * (vertex.y - A.y))
    surfaceC = abs((vertex.x - A.x) * (B.y - A.y) -
                   (B.x - A.x) * (vertex.y - A.y))
    return surfaceA + surfaceB + surfaceC <= totalSurface
isVertexInTriangle = classicInside

# insertVertexInTriangulation
def insertVertexInTrianglulation(triangulation, vertex):
    for index in range(len(triangulation)):
        triangle = triangulation[index]
        if isVertexInTriangle(vertex, triangle):
            print("in")
            subTriangulation = splitTriangle(triangle, vertex)
            triangulation = triangulation[:index] + subTriangulation + triangulation[index+1:]
            break
    return triangulation
def splitTriangle(triangle, vertex):
    triangleAB = Triangle([triangle.vertexList[0], triangle.vertexList[1], vertex], [])
    triangleBC = Triangle([triangle.vertexList[1], triangle.vertexList[2], vertex], [])
    triangleCA = Triangle([triangle.vertexList[2], triangle.vertexList[0], vertex], [])
    triangleAB.neighbors = [triangleAB.neighbors[0], triangleBC, triangleCA]
    triangleBC.neighbors = [triangleAB.neighbors[1], triangleCA, triangleAB]
    triangleBC.neighbors = [triangleAB.neighbors[2], triangleAB, triangleBC]
    return [triangleAB, triangleBC, triangleCA]


# delaunayTest
def delaunayTest(triangle, neighborsIndex):
    center, radius = findEmptyCircle(triangle)


createRandomVertex()
triangle = Triangle(vertexList, [None, None, None])
# drawTriangle(triangle)
# findEmptyCircle(triangle)
triangulation = [triangle]

vertexToTest = Vertex(0,0)
def mouseEventHandler(event):
    global triangulation
    global vertexToTest
    if event.button == 1:
        drawVertex(vertexToTest, (0,0,0), 3)
        x, y = pygame.mouse.get_pos()
        vertexToTest = Vertex(x, y)
        triangulation = insertVertexInTrianglulation(triangulation, vertexToTest)
        drawTriangulation(triangulation)



def keyboardEventHandler(event):
    if event.key == pygame.K_r:
        # createRandomVertex()
        return
    if event.key == pygame.K_e:
        return


def game():
    global triangulation
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseEventHandler(event)
            if event.type == pygame.KEYDOWN:
                keyboardEventHandler(event)

        canvas.fill(background)
        drawVertex(vertexToTest)
        drawTriangulation(triangulation)
        pygame.display.flip()


game()
