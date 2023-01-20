#importer le module pygame
from playsound import playsound 
import time
import pygame
from os import listdir
from constants import *

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

def load_img(path, size):
    """Charge une image et ajuste sa taille"""


    # Chargement de l'image
    img = pygame.image.load(path)
    

    # smoothscale() nécessite une image en 24-bits ou 32-bits
    if img.get_bitsize() in (24, 32):
        return pygame.transform.smoothscale(img, size)
    return pygame.transform.scale(img, size)


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

#classe qui représente le personnage
class Personnage(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #self.health = 100
        #self.max_health = 100
        #self.attack = 10
        self.velocity_x = 9
        self.velocity_y = 4 
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
            "marche_droite" : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeuneD", (23 *taille, 32*taille)), 
            "idle" : load_animation_images(DOSSIER_ANIM_JEUNE, "JeuneIdle", (23 *taille, 32 *taille)),
            'marche_gauche' : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeuneG", (23 *taille, 32 *taille)),
            "saut" : load_animation_images(DOSSIER_ANIM_JEUNE, "SautJeune", (32 *taille, 32 *taille)),
        } 
        self.actuel = "idle" 

    # Afficher les animations (frames)        
    def display(self):
        self.current_image = self.current_image %len(self.images[self.actuel])
        ecran.blit(self.images[self.actuel][int(self.current_image)], self.rect)
        self.current_image += delta_t / 200

    def idle(self):
        self.actuel = "idle"

    def move_right(self):
        self.actuel = "marche_droite"
        self.rect.x += self.velocity_x
        
    def move_left(self):
        self.actuel = "marche_gauche"
        self.rect.x -= self.velocity_x

    def jump(self):
  
        if self.on_ground:
            self.actuel = "saut"
            self.velocity_y = -10
            self.rect.y += self.velocity_y
            self.on_ground = False
       
        if self.on_ground == False :
            self.velocity_y += 0.5
            self.rect.y += self.velocity_y
        
            if self.rect.y > 666:        
                self.rect.y = 666
                self.velocity_y = 1
                self.on_ground = True

class Mechant(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(ENNEMI_CACTUS)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.current_image = 0
        self.animation = True
        self.actuel = "idle_ennemi1" 
        self.images = {
            "idle_ennemi1" : load_animation_images(DOSSIER_ENNEMI, "Cactus", (32 *taille, 32 *taille)), 
        } 

    def display(self):
        self.current_image = self.current_image %len(self.images[self.actuel])
        ecran.blit(self.images[self.actuel][int(self.current_image)], self.rect)
        self.current_image += delta_t / 200
    
    def update(self, shift):
        self.rect.x += shift

#Class du background 
class Background(pygame.sprite.Sprite):                         #Le fond qui est en mouvemet
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(IMAGE_FOND)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
    def display(self):
        ecran.blit(self.image, self.rect)

    def update(self, shift):
        self.rect.x += shift


def load_animation_images(path, name, size):

    # On cherche tous les images dans les dossiers avec le nom et on charge avec une certaine taille 
    return [load_img(path + "/" + file, size) for file in listdir(path) if file.startswith(name)]
    
#Dictionnaire
animation = {
    "marche" : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeune", (32, 32)),
    "mechant" : load_animation_images(DOSSIER_ENNEMI, "Cactus", (32, 32)),
} 

#classe qui représente le jeu
class Jeu: 
    def __init__(self):
        #générer le perso
        self.pressed = {}


#charger le personnage
player = Personnage()
#liste_mechant = [Mechant((200, 666))]
cactus = Mechant((750, 666))

back = Background((0, 0))
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
    
    print(player.rect.x, player.rect.y)
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
    print(back.rect.x)
    cactus.update(shift)
    back.update(shift)

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

    