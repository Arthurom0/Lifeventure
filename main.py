#importer le module pygame
from playsound import playsound 
import time
import pygame
from os import listdir
from constants import *
from utils import load_animation_images
from Personnage import Personnage
from Background import Background
from Mechant import Mechant
from Jeu import Jeu

pygame.init()
pygame.font.init() 

jumping = False
Y_gravity = 1
JUMP_HEIGHT = 20
Y_velocity = JUMP_HEIGHT 


#fenêtre du jeu
pygame.display.set_caption("Lifenture")
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
ecran = pygame.display.set_mode((width, height))
my_font = pygame.font.SysFont('Comic Sans MS', 30)

x_fond = 0
y_fond = 0
width_max = 1920
height_max = 1080
#taille
taille = 2
#Musique

DO_PLAY_SOUND = False
if DO_PLAY_SOUND:
    pygame.mixer.music.load(MUSIQUE_FOND)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    
#Temps
clock = pygame.time.Clock()

#Dictionnaire
animation = {
    "marche" : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeune", (32, 32)),
    "mechant" : load_animation_images(DOSSIER_ENNEMI, "Cactus", (32, 32)),
} 

#charger le personnage
player = Personnage(ecran)
cactus = Mechant(ecran, (750, 666))
back = Background(ecran)

#charger le jeu
game = Jeu()

# qui permet de savoir sur quelle map on est
current_map_id = 0

# liste qui va conteir les truc a afficher (fond, mobs, joueur, items...)
entities = [back, player, cactus]

# placement de la caméra qu'on peut déplacer indépendamenr du joueur
camera_offset = [0, 0]

def set_nd_map():
    global current_map_id
    camera_offset[0] = 0
    camera_offset[1] = 0
    current_map_id = 1
    player.rect.x = 0
    player.rect.y = 900
    back.setImage(1)
    

# tant que le jeu est en marche...
running = True
while running:

    #delta temps
    delta_t = clock.tick(60)

    # mettre à jour l'écran
    pygame.display.flip()

    #fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # defini si la touche est appuyée ou non (a faire avant de detecter les touches)
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
 

    for entity in entities:
        entity.update()

    # déplacement du personnage et mechant
    player.idle()  
    
    if game.pressed.get(pygame.K_RIGHT):
        player.move_right([back.image.get_width(), back.image.get_height()])
    elif game.pressed.get(pygame.K_LEFT):
        player.move_left([back.image.get_width(), back.image.get_height()])

    if game.pressed.get(pygame.K_UP): 
        player.jump()


    # on déplace la caméra sur le joueur
    camera_offset[0] = -(player.rect.x - width_max//2)
  

    #Montrer le personnage et mechant
    for entity in entities:
        entity.display(camera_offset)  
  
    # afficher les coordonnées (x;y du joueur)
    text_surface = my_font.render(f"x={player.rect.x}, y={player.rect.y}", False, (0, 0, 0))
    ecran.blit(text_surface, (0, 0))

    # si la map est 1 et que le joueur est a droite
    if current_map_id == 0 and player.rect.x >= 2710 and player.rect.x <= 2770 :
        text_surface = my_font.render(f"Press down to enter", False, (0, 0, 0))
        ecran.blit(text_surface, (player.rect.x + camera_offset[0] - 100, 600))
        if game.pressed.get(pygame.K_RETURN):
            set_nd_map()

    if game.pressed.get(pygame.K_ESCAPE):
        pygame.quit()
    
        
   

    