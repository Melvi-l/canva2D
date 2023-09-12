from typing import List
import pygame
import sys
from geom import Vertex, Segment, Polygon

# Color
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 226, 82)

# Global geom
polygon: Polygon = None
lastVertex: Vertex = None
vertexToTestList: List[Vertex] = []

pygame.init()
width = 1000
height = 1000
canvas = pygame.display.set_mode((width, height))
background = (0, 0, 0)
canvas.fill(background)
font = pygame.font.Font(None, 24)  # Utilisation de la police par défaut de Pygame


def addVertexToPolygon(vertex: Vertex) -> None:
    # prevent weird scope python shit
    global lastVertex
    global polygon

    drawVertex(vertex)

    if lastVertex is None:
        lastVertex = vertex
        return
    if polygon is None:
        segment = Segment(lastVertex, vertex)
        polygon = Polygon([segment])
        drawSegment(segment)
        return
    polygon.addVertex(vertex)
    drawSegment(polygon.segmentList[-1])

def addVertexToTestList(vertex: Vertex) -> None:
    drawVertex(vertex, WHITE)
    vertexToTestList.append(vertex)

let = lambda a, b: a.x * b.y - a.y * b.x
def sign(a: float): 
    if a<0:
        return -1
    return 1
def convexTest() -> None:
    lastSign = None
    for i in range(len(polygon.segmentList)-1):
        a, b, c = polygon.segmentList[i].a, polygon.segmentList[i].b, polygon.segmentList[i+1].b
        v = Vertex(b.x-a.x, b.y-a.y)
        w = Vertex(c.x-a.x, c.y-a.y)
        val = let(v,w)
        newSign = sign(val)
        if not(lastSign is None) and newSign != lastSign:
            drawText("Not convex", (width-100, height-50), RED)
            return 
        lastSign = newSign
    drawText("Convex", (width-50, height-50), GREEN)
        


def insideTest() -> None:
    for vertex in vertexToTestList:
        intersectionVertexList = []
        for segment in polygon.segmentList:
            intersectionVertex = getIntersectionVertex(vertex, segment)
            if not(intersectionVertex is None):
                intersectionVertexList.append(intersectionVertex)
        color = RED
        if len(intersectionVertexList) % 2 == 1:
            color = GREEN
        for intersectionVertex in intersectionVertexList:
            drawVertex(intersectionVertex, color, 3)
        drawVertex(vertex, color, 5)
        drawLineHelper(vertex, color)


def getIntersectionVertex(vertex, segment) -> Vertex | None:
    if segment.a.y == segment.b.y:  # horizontal
        return None
    
    t = (vertex.y - segment.a.y) / (segment.b.y - segment.a.y)
    if t > 1 or t < 0:
        return None

    x = (segment.b.x-segment.a.x) * t + segment.a.x
    if (x < vertex.x):
        return None
    y = (segment.b.y-segment.a.y) * t + segment.a.y

    return Vertex(x, y)

# Event handler
def mouseEventHandler(event):
    if event.button == 1:
        x, y = pygame.mouse.get_pos()
        newVertex = Vertex(x, y)

        if polygon is None or not (polygon.isClose):
            addVertexToPolygon(newVertex)
            return

        addVertexToTestList(newVertex)

    if event.button == 3:
        polygon.close()
        convexTest()
        drawSegment(polygon.segmentList[-1])


def keyboardEventHandler(event):
    if event.key == pygame.K_SPACE:
        insideTest()

# Draw function


def drawVertex(vertex: Vertex, color=YELLOW, size=2):
    pygame.draw.circle(canvas, color, (vertex.x, vertex.y), size)
 

def drawSegment(segment: Segment):
    pygame.draw.line(canvas, YELLOW, (segment.a.x,
                     segment.a.y), (segment.b.x, segment.b.y), 1)


def drawLineHelper(vertex: Vertex, color: (int, int, int)):
    pygame.draw.line(canvas, color, (vertex.x, vertex.y),
                     (width-20, vertex.y), 1)

def drawText(content, position,color):
    text = font.render(content, True, color)
    rect = text.get_rect()
    rect.center = position
    canvas.blit(text, rect) 

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
