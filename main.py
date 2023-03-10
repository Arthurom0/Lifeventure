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
jumping = False
Y_gravity = 1
JUMP_HEIGHT = 20
Y_velocity = JUMP_HEIGHT 


#fenêtre du jeu
pygame.display.set_caption("Lifenture")
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
ecran = pygame.display.set_mode((width, height))
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

#importer l'arrière plan
arriereplan = pygame.image.load(IMAGE_FOND)

#mouvement du fond
screen_scrolling = 0

#valeur y du background
y_background = 0

#  # On récupère ses dimensions
# dimension_fondx = arriereplan.get_width()
# dimension_fondy = arriereplan.get_height()

# print(dimension_fondx)
# print(dimension_fondy)

# pygame.Rect(0, 0, 1920, 1080)


    
#Dictionnaire
animation = {
    "marche" : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeune", (32, 32)),
    "mechant" : load_animation_images(DOSSIER_ENNEMI, "Cactus", (32, 32)),
} 



#charger le personnage
player = Personnage(ecran)
#liste_mechant = [Mechant((200, 666))]
cactus = Mechant(ecran, (750, 666))

back = Background(ecran, (0, 0))
#charger le jeu
game = Jeu()

# liste qui va conteir les truc a afficher (fond, mobs, joueur, items...)
entities = [back, player, cactus]

# placement de la caméra qu'on peut déplacer indépendamenr du joueur
camera_offset = [0, 0]

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

    if game.pressed.get(pygame.K_ESCAPE):
        pygame.quit
    
        
   

    