import pygame
import sys
from geom import Vertex, Segment, Polygon

pygame.init()

width = 1000
height = 1000

canvas = pygame.display.set_mode((width, height))

background = (0, 0, 0)


polygon: Polygon = None
lastVertex: Vertex = None

def addVertexToPolygon(vertex: Vertex) -> None:
    # prevent weird scope python shit
    global lastVertex
    global polygon

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

# Event handler
def mouseEventHandler(event):
    if event.button == 1:
        x, y = pygame.mouse.get_pos()
        newVertex = Vertex(x, y)
        
        if polygon is None or not(polygon.isClose):
            drawVertex(newVertex)
            addVertexToPolygon(newVertex)
            return
        
        drawVertex(newVertex, (255,255,255))
            
    if event.button == 3:
        polygon.close()
        drawSegment(polygon.segmentList[-1])
def keyboardEventHandler(event):
    if event.key == pygame.K_SPACE:
        print("space")

# Draw function
def drawVertex(vertex: Vertex, color = (255,0,0)):
    pygame.draw.circle(canvas, color, (vertex.x, vertex.y), 2)
def drawSegment(segment: Segment):
    pygame.draw.line(canvas, (255,0,0), (segment.a.x, segment.a.y), (segment.b.x, segment.b.y), 1)


def init():
    canvas.fill(background)

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

init()
game()
     
        

        



