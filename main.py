#MAIN.PY

import pygame
import Constantes
from Personaje import Personaje


Jugador = Personaje(20, 20)

pygame.init()

ancho = 800
alto = 600

ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA,
                                   Constantes.ALTO_VENTANA))

pygame.display.set_caption("Mi Primer Juego")

#DEFINIR LAS VARIABLES DE MOVIMIENTO DEL JUGADOR
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

run = True
while run == True:

    ventana.fill(Constantes.COLOR_BG)

    #CALCULAR EL MOVIMIENTO DEL JUGADOR
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = 5
    if mover_izquierda == True:
        delta_x = -5
    if mover_arriba == True:
        delta_x = -5
    if mover_derecha == True:
        delta_x = 5

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


    pygame.display.update()

pygame.quit()