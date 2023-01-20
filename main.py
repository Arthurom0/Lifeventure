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
    pygame.mixer.music.set_volume(0.7)
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

shift = 0

# tant que le jeu est en marche...
running = True
while running:

    #delta temps
    delta_t = clock.tick()

    # mettre à jour l'écran
    pygame.display.flip()
    
    #ecran.blit(arriereplan, (x_fond - (player.rect.x +shift)//3 , y_fond ))



    #Limite de la fenetre 
    if player.rect.x < width/3 and back.rect.x != 0:
        player.rect.x = width/3
        shift = 9
    elif player.rect.x > (width/3) *2 and back.rect.x > -1950:
        player.rect.x = (width/3) *2
        shift = -9 
    else:
        shift = 0

    cactus.update(shift)
    back.update(shift)
    player.update()

    ecran.blit(arriereplan, (x_fond, y_fond ))    
                        
    #Montrer le personnage et mechant
    back.display()
    player.display()    
    cactus.display()

    # déplacement du personnage et mechant
    if game.pressed.get(pygame.K_RIGHT):
        player.move_right()
    
    elif game.pressed.get(pygame.K_LEFT):
        player.move_left()
    elif game.pressed.get(pygame.K_UP): 
        player.jump()
    else: 
        player.idle()   

         
    if game.pressed.get(pygame.K_TAB):
        pygame.quit
    
        
    #fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            
        # deplacement du personnage
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] =False

    