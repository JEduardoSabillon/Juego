import pygame
import Constantes
import math

class Weapon():
    def __init__(self, image, imagen_bala):
        self.imagen_bala = imagen_bala
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()
        self.dispara = False

    def update(self, personaje):
        bala = None
        self.forma.center = personaje.forma.center
        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.forma.width / 2
            self.rotar_arma(False)
        if personaje.flip == True:
            self.forma.x = self.forma.x - personaje.forma.width / 2
            self.rotar_arma(True)

        # Mover la pistola con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))

        #print(self.angulo)

        #Detectar los clic con el mause
        if pygame.mouse.get_pressed()[0] and self.dispara == False:
            bala = Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.dispara = True
        #Resetear el Clic del Mouse
            if pygame.mouse.get_pressed() == False:
                self.dispara = False
            return bala

    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                                True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                                False, True)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)
       # pygame.draw.rect(interfaz, Constantes.COLOR_ARMA,  self.forma, 1)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.image_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def dibujar(self, interfaz):
        interfaz.blit(self.image, (self.rect.centerx,
                                   self.rect.centery - int(self.image.get_height())))