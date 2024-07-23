#CLASE PERSONAJE

import pygame
import Constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        #imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0
        #Aqui se almacena la hora actual (en milisegundos desde que se inicia)
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = pygame.Rect(0, 0, Constantes.ANCHO_PERSONAJE,
                                        Constantes.ALTO_PERSONAJE)
        self.forma.center = (x,y)

    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]



    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(self.image, self.forma)
      #  pygame.draw.rect(interfaz, (255, 250, 0),  self.forma, 1)


def movimineto(self, delta_x, delta_y):
    if delta_x < 0:
        self.flip = True
    if delta_x > 0:
        self.flip = False

    self.forma.x = self.forma.x + delta_x
    self.forma.y = self.forma.y + delta_y