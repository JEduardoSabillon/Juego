#MAIN

import pygame
import Constantes
from Personaje import Personaje
from weapons import Weapon


pygame.init()
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA,
                                   Constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi Primer Juego")

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

#Importar imagenes
#Personajes
animaciones = []
for i in range (7):
    img = pygame.image.load(f"assets//images//characters//player//Player_{i}.png").convert_alpha()
    img = escalar_img(img, Constantes.SCALA_PERSONAJE)
    animaciones.append(img)

#Arma
imagen_pistola = pygame.image.load(f"assets//images//weapons//gun.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola, Constantes.SCALA_ARMA)

#Balas
imagen_balas = pygame.image.load(f"assets//images//weapons//bala.png").convert_alpha()
imagen_balas = escalar_img(imagen_balas, Constantes.SCALA_ARMA)


#Crear un jugador de la clase personaje
Jugador = Personaje(50, 50, animaciones)


#Crear una arma de la clase weapon
pistola = Weapon(imagen_pistola, imagen_balas)

#Crear un grupo de Sprite
grupo_balas = pygame.sprite.Group()



#DEFINIR LAS VARIABLES DE MOVIMIENTO DEL JUGADOR
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#CONTROLAR EL FRENTE RATE
reloj = pygame.time.Clock()

run = True
while run == True:



    #QUE VAYA A 60 FPS
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

    # MVOVER ALL JUGADOR
    Jugador.movimeinto(delta_x, delta_y)

    # Actualiza estado del jugador
    Jugador.update()

    # Actualiza el estado del arma
    bala = pistola.update(Jugador)
    if bala:
        grupo_balas.add(bala)

        print(grupo_balas)


    # Dibijar al Jugador
    Jugador.dibujar(ventana)

    # Dibujar el Arma
    pistola.dibujar(ventana)

    #Dibujar Bala
    for bala in grupo_balas:
        bala.dibujar(ventana)

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


        #PARA CUANDO SE SUELTA LA TECLA
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