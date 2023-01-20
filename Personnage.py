from constants import *
import pygame
from utils import load_animation_images

#classe qui représente le personnage
class Personnage(pygame.sprite.Sprite):

    def __init__(self, ecran):
        super().__init__()
        self.ecran = ecran
        self.tick = pygame.time.Clock().tick()
        #self.health = 100
        #self.max_health = 100
        #self.attack = 10
        
        self.velocity_x = 9
        self.velocity_y = 4 
        self.vitesse_x = 0
        self.vitesse_y = 0

        self.gravity = 1
        #self.velocity_z = 4
        self.image = pygame.image.load(ANIM_JEUNE)
        self.rect = self.image.get_rect()
        self.on_ground = True
        self.rect.x = 999
        self.rect.y = 666
        #self.rect.z = 1
        self.current_image = 0
        self.animation = True
        self.images = {
            "marche_droite" : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeuneD", (23 *2, 32*2)), 
            "idle" : load_animation_images(DOSSIER_ANIM_JEUNE, "JeuneIdle", (23 *2, 32 *2)),
            'marche_gauche' : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeuneG", (23 *2, 32 *2)),
            "saut" : load_animation_images(DOSSIER_ANIM_JEUNE, "SautJeune", (32 *2, 32 *2)),
        } 
        self.actuel = "idle" 

    # Afficher les animations (frames)        
    def display(self):
        self.current_image = self.current_image %len(self.images[self.actuel])
        self.ecran.blit(self.images[self.actuel][int(self.current_image)], self.rect)
        self.current_image += self.tick / 200

    def idle(self):
        self.actuel = "idle"

    def move_right(self):
        self.actuel = "marche_droite"
        self.rect.x += self.velocity_x
        
    def move_left(self):
        self.actuel = "marche_gauche"
        self.rect.x -= self.velocity_x

    def update(self):
        
        self.rect.y += self.vitesse_y
        self.vitesse_y += 0.5

        if self.rect.y >= 666:
            self.vitesse_y = 0

        print(self.rect.x, self.rect.y)

    def jump(self):
        if self.vitesse_y == 0:
            self.vitesse_y = -10
