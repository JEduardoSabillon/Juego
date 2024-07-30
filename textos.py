#CLASE TEXTOS

import pygame.sprite

class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, font, color):
        pygame.sprite.Sprite._init_(self)
        self.image = font.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.contador = 0

    def update(self):
        self.rect.y -= 2
        self.contador += 1
        if self.contador > 50:
            self.kill()