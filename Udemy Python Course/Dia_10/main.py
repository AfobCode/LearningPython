"""
Crear el juego de convertir canastas
"""

## desde pypi.org descargar la libreria pygame
import pygame
import math
from pygame import mixer


pygame.init() #Inicializar el modulo

#Crear la ventana/Pantalla
pantalla = pygame.display.set_mode((800, 600)) #Dimensionamiento de la ventada de tipo pygame

# Definir titulo e icono de la ventada
icono = pygame.image.load("Imagenes/icon.png")
pygame.display.set_caption('Basquet Shooting')
pygame.display.set_icon(icono)
fondo = pygame.image.load("Imagenes/court.png")

# Agregar sonido juego
musica_fondo = mixer.music.load("Sonidos/basketball-game.mp3")
mixer.music.set_volume(0.15)
mixer.music.play(-1)

canasta = mixer.Sound("Sonidos/basketball-net.mp3")
canasta.set_volume(0.20)

fin = mixer.Sound("Sonidos/buzer.mp3")



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

# Puntaje
puntaje = 0
fuente_puntaje = pygame.font.Font('freesansbold.ttf', 24)
fuente_tipo_canasta = pygame.font.Font('freesansbold.ttf', 20)
tpo_canasta = ""

# Funcion canasta:
def anotar(pos_x1,pos_y1 , pos_x2 , pos_y2):
    x2_x1 = pos_x2 - pos_x1
    y2_y1 = pos_y2 - pos_y1
    distancia = math.sqrt((x2_x1**2) + (y2_y1**2))
    return  distancia

def puntuar(altura):

    if altura < 150:
        valor = "Triplazoo !!"
        punto= 3
    else:
        valor = "Doble +2"
        punto = 2

    return punto , valor

# informacion juego
pos_x_mostarPuntos = 580
pos_x_tipoCanasta = 300
pos_y_tipoCanasta = pos_y_mostarPuntos = 15

def mostrar_puntuacion(posX, posY,puntos):
    puntuacion = fuente_puntaje.render(f"Marcador: {puntos}", True, (0,0,0))
    pantalla.blit(puntuacion,(posX, posY))

def tipo_canasta(posX,posY, tipo):
    tpo_canasta = fuente_tipo_canasta.render(tipo,True,(0,0,0))
    pantalla.blit(tpo_canasta, (posX, posY))

# Final del juego
texto_fin = pygame.font.Font('freesansbold.ttf', 20)

def fin_juego():
    mixer.music.stop()
    fin.play()
    mesaje_fin = texto_fin.render("FIN del JUEGO", True, (0,0,0))
    pantalla.blit(mesaje_fin, (60,200))


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
                movimiento_lanzador = 1
            elif (evento.key == pygame.K_LEFT) or (evento.key == pygame.K_s):
                movimiento_lanzador = -1
            elif (evento.key == pygame.K_SPACE) or (evento.key == pygame.K_d):
                pos_balon_x = pos_shooter_x
                pos_balon_y = pos_shooter_y
                lanzar = True

        elif evento.type == pygame.KEYUP:
            movimiento_lanzador = 0

        if evento.type == pygame.QUIT:
            """ Cerrar la ventana
            """
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
    if pos_ring_y >= 40:
        if pos_ring_x >= (800-65):
            mueve_derecha = False
            mueve_izquierda = True
            pos_ring_y -= 15
            
        elif pos_ring_x <= 0:
            mueve_derecha = True
            mueve_izquierda = False
            pos_ring_y -= 15

    else:
        fin_juego()
        movimiento_ring_x = 0
        mueve_derecha = mueve_izquierda = False
        pos_y_mostarPuntos = 320
        pos_x_mostarPuntos = 332
        pos_y_tipoCanasta = -50
        pos_shooter_x, pos_ring_x = 410, 300
        pos_ring_y = pos_shooter_y = 228





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
    if punto > 15 and punto < 22.1:
        canasta.play()
        lanzar = False
        movimiento_ring_x = 0
        pos_balon_y = 800
        pos_balon_x = 600
        anotacion = puntuar(pos_ring_y)

        puntaje += anotacion[0]
        tpo_canasta = anotacion[1]


    # Mofidicar la pocision del jugador en pantalla
    pos_shooter_x += movimiento_lanzador

    # Mofidicar la pocision del aro en pantalla
    pos_ring_y += movimiento_ring_y
    pos_ring_x += movimiento_ring_x

    # Mofidicar la pocision del balon en pantalla
    pos_balon_y += movimiento_balon_y
    pos_balon_x += movimiento_balon_x

    mostrar_puntuacion(pos_x_mostarPuntos,pos_y_mostarPuntos,puntaje)
    tipo_canasta(pos_x_tipoCanasta,pos_y_tipoCanasta,tpo_canasta)
    aro(pos_ring_x,pos_ring_y)
    shooter(pos_shooter_x,pos_shooter_y)
    lanzamiento(pos_balon_x,pos_balon_y)
    pygame.display.update() # mostrar los cambios en pantalla