import pygame
from constants import *

#Class du background 
class Background(pygame.sprite.Sprite):                         #Le fond qui est en mouvemet
    def __init__(self, ecran, position):
        super().__init__()
        self.ecran = ecran
        self.image = pygame.image.load(IMAGE_FOND)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
    def display(self):
        self.ecran.blit(self.image, self.rect)

    def update(self, shift):
        self.rect.x += shift
