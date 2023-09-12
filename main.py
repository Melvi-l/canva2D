import pygame
import sys

pygame.init()

largeur = 800
hauteur = 600

fenetre = pygame.display.set_mode((largeur, hauteur))

fond = (0, 0, 0)
couleur_carre = (255, 0, 0)

x_carre = 100
y_carre = 100
largeur_carre = 50
hauteur_carre = 50
vitesse = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        x_carre -= 0.01
    if touches[pygame.K_RIGHT]:
        x_carre += 0.01
    if touches[pygame.K_UP]:
        y_carre -= 0.01
    if touches[pygame.K_DOWN]:
        y_carre += 0.01
        


    fenetre.fill(fond)

    

    pygame.draw.rect(fenetre, couleur_carre, (x_carre,y_carre,largeur_carre, hauteur_carre))

    pygame.display.flip()
