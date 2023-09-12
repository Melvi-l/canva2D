import pygame
import sys
from geom import Point

pygame.init()

width = 800
height = 600

canvas = pygame.display.set_mode((width, height))

background = (0, 0, 0)

pointList = []

def mouseEventHandler(event):
    if event.button == 1:
        x, y = pygame.mouse.get_pos()
        pointList.append(Point(x, y))

# Game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseEventHandler(event)
    
    canvas.fill(background)

    for point in pointList: 
        pygame.draw.circle(canvas, (255,0,0), (point.x, point.y), 2)
        


    pygame.display.flip()


