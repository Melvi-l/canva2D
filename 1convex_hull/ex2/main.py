from typing import List
import pygame
import sys
import random
from Vertex import Vertex
from Segment import Segment
from Polygon import Polygon
from bull import extremEdge

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


def drawVertex(vertex: Vertex, color=YELLOW, size=2):
    pygame.draw.circle(canvas, color, (vertex.x, vertex.y), size)


def drawSegment(segment: Segment):
    pygame.draw.line(canvas, YELLOW, (segment.a.x,
                     segment.a.y), (segment.b.x, segment.b.y), 1)


def drawPolygon(polygon: Polygon):
    for segment in polygon.segmentList:
        pygame.draw.line(canvas, YELLOW, (segment.a.x,
                                          segment.a.y), (segment.b.x, segment.b.y), 1)


def mouseEventHandler(event):
    return


def createRandomVertex():
    VERTE_NB = 10
    for i in range(VERTE_NB):
        vertex = Vertex(random.randint(100, width-100),
                        random.randint(100, height-100))
        vertexList.append(vertex)
        drawVertex(vertex)


def keyboardEventHandler(event):
    if event.key == pygame.K_r:
        createRandomVertex()
    if event.key == pygame.K_e:
        print(extremEdge)
        hull = extremEdge(vertexList)
        print(hull)
        drawPolygon(hull)


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
