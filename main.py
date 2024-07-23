#MAIN.PY

import pygame
import Constantes
import player
from Personaje import Personaje

pygame.init()

ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA,
                                   Constantes.ALTO_VENTANA))

pygame.display.set_caption("Mi Primer Juego")

def escala_img(image, scala):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scala, h*scala))
    return nueva_imagen


animaciones= []
for i in range (6):
    img = pygame.image.load(f"assets//images//characters//player//Player_{i}.png")
    img =escala_img(img, Constantes.SCALA_PERSONAJE)
    animaciones.append(img)


Jugador = Personaje(50, 50, animaciones)


#DEFINIR LAS VARIABLES DE MOVIMIENTO DEL JUGADOR
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#Controlar el freme red
reloj = pygame.time.Clock()

run = True
while run == True:

    #Que vaya a 60 fps
    reloj.tick(Constantes.FPS)


    ventana.fill(Constantes.COLOR_BG)

    #CALCULAR EL MOVIMIENTO DEL JUGADOR
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = Constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -Constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -Constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = Constantes.VELOCIDAD

    #Mover al Jugador
    Jugador.movimineto(delta_x, delta_y)


    Jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        # PAra cuando se suelte la tecla
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            mover_izquierda = False
        if event.key == pygame.K_d:
            mover_derecha = False
        if event.key == pygame.K_w:
            mover_arriba = False
        if event.key == pygame.K_s:
            mover_abajo = False

    pygame.display.update()

pygame.quit()