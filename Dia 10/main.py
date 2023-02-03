"""
Crear el juego de convertir canastas
"""

## desde pypi.org descargar la libreria pygame
import pygame

pygame.init() #Inicializar el modulo
pantalla = pygame.display.set_mode((800, 600)) #Dimensionamiento de la ventada de tipo pygame

corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False