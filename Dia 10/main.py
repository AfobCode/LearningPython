"""
Crear el juego de convertir canastas
"""

## desde pypi.org descargar la libreria pygame
import pygame
import math
pygame.init() #Inicializar el modulo

#Crear la ventana/Pantalla
pantalla = pygame.display.set_mode((800, 600)) #Dimensionamiento de la ventada de tipo pygame

# Definir titulo e icono de la ventada
icono = pygame.image.load("Imagenes/icon.png")
pygame.display.set_caption('Basquet Shooting')
pygame.display.set_icon(icono)
fondo = pygame.image.load("Imagenes/court.png")

# Jugador
img_lanzador = pygame.image.load("Imagenes/shooter.png")
pos_shooter_x = 368
pos_shooter_y = 520
movimiento_lanzador = 0
def shooter(pos_x, pos_y):
    pantalla.blit(img_lanzador,(pos_x,pos_y))


# Aro
img_ring = pygame.image.load("Imagenes/ring.png")
pos_ring_x = 368
pos_ring_y = 350
movimiento_ring_x = 0
movimiento_ring_y = 0
mueve_derecha = True
mueve_izquierda = False
def aro(pos_x , pos_y):
    pantalla.blit(img_ring,(pos_x,pos_y))


# Balon
img_balon = pygame.image.load("Imagenes/ball.png")
pos_balon_x = 800
pos_balon_y = 600
lanzar = False
movimiento_balon_x = 0
movimiento_balon_y = 0


def lanzamiento(pos_x,pos_y):
    pantalla.blit(img_balon, (pos_x , pos_y))

# Funcion canasta:
def anotar(pos_x1,pos_y1 , pos_x2 , pos_y2):
    x2_x1 = pos_x2 - pos_x1
    y2_y1 = pos_y2 - pos_y1
    distancia = math.sqrt((x2_x1**2) + (y2_y1**2))
    return  distancia


# Puntaje
puntaje = 0

# Loop del juego
corriendo = True

while corriendo:

    pantalla.fill((255, 148, 91))  # Cambio de color del fondo de la pantalla en escala RGB
    #pantalla.blit(fondo,(142,300))


    for evento in pygame.event.get():
        """ Capturar los eventos que ocurran sobre la ventana de pygame
        """

        if evento.type == pygame.KEYDOWN:
            """ Desplazamiento del jugador
            """
            if (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_f):
                movimiento_lanzador = 0.5
            elif (evento.key == pygame.K_LEFT) or (evento.key == pygame.K_s):
                movimiento_lanzador = -0.5
            elif (evento.key == pygame.K_SPACE) or (evento.key == pygame.K_d):
                pos_balon_x = pos_shooter_x
                pos_balon_y = pos_shooter_y
                lanzar = True

        elif evento.type == pygame.KEYUP:
            movimiento_lanzador = 0

        if evento.type == pygame.QUIT:
            """ Cerrar la ventana
            """
            print(evento.type)
            corriendo = False

    # tod0 lo que se va a mostrar/actualizar dentro de la ventada tiene que
    # codificarse dentro del loop de la ejecucion

    # Mofidicar la posicion del aro en pantalla
    if mueve_derecha:
        movimiento_ring_x = 0.5
    elif mueve_izquierda:
        movimiento_ring_x = -0.5


    # Mantener jugador en cancha
    if pos_shooter_x < 1:
        pos_shooter_x = 4
    elif pos_shooter_x > (800-65):
        pos_shooter_x = 800-69

    # Mantener Aro en cancha
    if pos_ring_y >= 30:
        if pos_ring_x >= (800-65):
            mueve_derecha = False
            mueve_izquierda = True
            pos_ring_y -= 15
            
        elif pos_ring_x <= 0:
            mueve_derecha = True
            mueve_izquierda = False
            pos_ring_y -= 15

    else:
        pos_ring_y = 350

    # Lanzar el balon
    if not lanzar:
        movimiento_balon_y = 0
    elif lanzar and pos_balon_y > 0:
        movimiento_balon_y = -1.5
    elif pos_balon_y <= 0:
        pos_balon_y = 800
        lanzar = False

    #Chequear si anoto
    punto = anotar(pos_balon_x, pos_balon_y, pos_ring_x, pos_ring_y)
    if punto > 22 and punto < 22.1:
        lanzar = False
        movimiento_ring_x = 0
        pos_balon_y = 800
        pos_balon_x = 600

        print("Canastaaa")
        if pos_ring_y < 190:
            print("Triplazo!!")
            puntaje += 3
        else:
            print("Doble")
            puntaje += 2

        print(puntaje)

    # Mofidicar la pocision del jugador en pantalla
    pos_shooter_x += movimiento_lanzador

    # Mofidicar la pocision del aro en pantalla
    pos_ring_y += movimiento_ring_y
    pos_ring_x += movimiento_ring_x

    # Mofidicar la pocision del balon en pantalla
    pos_balon_y += movimiento_balon_y
    pos_balon_x += movimiento_balon_x

    aro(pos_ring_x,pos_ring_y)
    shooter(pos_shooter_x,pos_shooter_y)
    lanzamiento(pos_balon_x,pos_balon_y)
    pygame.display.update() # mostrar los cambios en pantalla