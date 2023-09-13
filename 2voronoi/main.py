import random
from typing import List, Tuple
from Triangle import Triangle
import pygame
import sys
from Vertex import Vertex
from Segment import Segment
from Polygon import Polygon

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
# Utilisation de la police par défaut de Pygame
font = pygame.font.Font(None, 24)


def drawVertex(vertex, color=YELLOW, size=2):
    pygame.draw.circle(canvas, color, (vertex.x, vertex.y), size)


def drawEdge(start, stop, color=YELLOW, size=1):
    pygame.draw.line(canvas, color, (start.x,
                     start.y), (stop.x, stop.y), size)

def drawTriangle(triangle, color=YELLOW, size = 1):
    drawEdge(vertexList[0], vertexList[1], color, size)
    drawEdge(vertexList[1], vertexList[2], color, size)
    drawEdge(vertexList[2], vertexList[0], color, size)



def drawPolygon(polygon):
    for segment in polygon.segmentList:
        pygame.draw.line(canvas, YELLOW, (segment.a.x,
                                          segment.a.y), (segment.b.x, segment.b.y), 1)


def mouseEventHandler(event):
    return


def createRandomVertex():
    VERTE_NB = 3
    for i in range(VERTE_NB):
        vertex = Vertex(random.randint(100, width-100),
                        random.randint(100, height-100))
        vertexList.append(vertex)
        drawVertex(vertex)


def keyboardEventHandler(event):
    if event.key == pygame.K_r:
        # createRandomVertex()
        return
    if event.key == pygame.K_e:
        return


def findEmptyCircleCenter(triangle: Triangle):
    
    edgeA = triangle.vertexList[0], triangle.vertexList[1] 
    edgeB = triangle.vertexList[1], triangle.vertexList[2] 

    centerVectorTupleA = findBisector(edgeA)
    centerVectorTupleB = findBisector(edgeB)

    intersection = findLineIntersection(centerVectorTupleA, centerVectorTupleB)

    drawEdge(centerVectorTupleA[0], intersection, RED, 3)
    drawEdge(centerVectorTupleB[0], intersection, RED, 3)
    drawVertex(intersection, RED, 4)




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
    tB = ((centerB.x - centerA.x) / vectorA.x - (centerB.y - centerA.y) / vectorA.y) / (vectorB.y / vectorA.y - vectorB.x / vectorA.x)  
    return Vertex(vectorB.x*tB + centerB.x, vectorB.y*tB + centerB.y)

createRandomVertex()
triangle = Triangle(vertexList, [None, None, None])
drawTriangle(triangle)
findEmptyCircleCenter(triangle)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseEventHandler(event)
            if event.type == pygame.KEYDOWN:
                keyboardEventHandler(event)

        pygame.display.flip()


game()
