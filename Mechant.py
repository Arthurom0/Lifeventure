import pygame
from constants import *
from utils import load_animation_images

class Mechant(pygame.sprite.Sprite):
    def __init__(self, ecran, position):
        super().__init__()
        self.ecran = ecran
        self.tick = pygame.time.Clock().tick()
        self.image = pygame.image.load(ENNEMI_CACTUS)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.current_image = 0
        self.animation = True
        self.actuel = "idle_ennemi1" 
        self.images = {
            "idle_ennemi1" : load_animation_images(DOSSIER_ENNEMI, "Cactus", (32 * 2, 32 * 2)), 
        } 

    def display(self):
        self.current_image = self.current_image %len(self.images[self.actuel])
        self.ecran.blit(self.images[self.actuel][int(self.current_image)], self.rect)
        self.current_image += self.tick / 200
    
    def update(self, shift):
        self.rect.x += shift
