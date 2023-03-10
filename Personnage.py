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
        
        self.velocity_x = 13
        self.velocity_y = 5
        self.vitesse_x = 0
        self.vitesse_y = 0

        self.gravity = 1
        #self.velocity_z = 4
        self.image = pygame.image.load(ANIM_JEUNE)
        self.rect = self.image.get_rect()
        self.on_ground = True
        self.rect.x = 999
        self.rect.y = 666
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
    def display(self, camera_offset):
        self.current_image = self.current_image % len(self.images[self.actuel])

        pixel_x = self.rect.x + camera_offset[0]
        pixel_y = self.rect.y + camera_offset[1]

        self.ecran.blit(self.images[self.actuel][int(self.current_image)], (pixel_x, pixel_y))
        self.current_image += 1
 
    def idle(self):
        self.actuel = "idle"

    def move_right(self, container):
        """
        container est une liste [x, y] qui contient la largeuyr et la hauteur de la map dans laquelle est le joueur (pour pas qu'il sorte)
        """
        self.actuel = "marche_droite"
        self.rect.x += self.velocity_x
        # marge de 64 sur lequel le joueur ne peut pas aller a droite
        if self.rect.x > container[0] - 64 :
            self.rect.x = container[0] - 64 
        
    def move_left(self, container):
        """
        container est une liste [x, y] qui contient la largeuyr et la hauteur de la map dans laquelle est le joueur (pour pas qu'il sorte)
        """
        self.actuel = "marche_gauche"
        self.rect.x -= self.velocity_x
        if self.rect.x < 64:
            self.rect.x = 64

    def jump(self):
            if self.vitesse_y == 0:
                self.vitesse_y = -10

    def update(self):
        self.rect.y += self.vitesse_y
        self.vitesse_y += 0.7

        if self.rect.y >= 666:
            self.vitesse_y = 0

        #print(self.rect.x, self.rect.y)

    
#helloo 