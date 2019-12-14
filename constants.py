"""
This is a file to store all constant for the game.
"""
import os
import pygame

# import some keys from pygame.locals for easier access
from pygame.locals import (
    K_i,
    K_j,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)



class GeneralSquare(pygame.sprite.Sprite):
    """Main class that defines how most sprites should initialise and set position and draw themselves"""
    
    def __init__(self, DIR, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(DIR, '{}.png'.format(self.ID)))
        self.image = pygame.transform.scale(self.image, (int(width) + 1, int(height) + 1))
        self.rect = self.image.get_rect()
        self.rect[2:] = (self.rect[2] * 0.75, self.rect[3] * 0.75)

    def set_position(self, x, y):
        self.rect[0:2] = [x, y]

    def draw(self, surf):
        surf.blit(self.image, self.rect[0:2])

    def add_to_group(self):
        pass


# set some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (64, 64, 64)
YELLOW = (255, 255, 0)
ORANGE = (179, 89, 0)

# set the screen constants
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
DISPLAY_SIZE_X = pygame.display.Info().current_w
DISPLAY_SIZE_Y = pygame.display.Info().current_h
SCREEN_X = DISPLAY_SIZE_X // 5 * 4
SCREEN_Y = DISPLAY_SIZE_Y

# set the monster popup screen size
POPUP_X = SCREEN_X
POPUP_Y = SCREEN_Y // 2
AVATAR = SCREEN_Y // 6

# set the jump screen size
JUMP_X = SCREEN_X // 5 * 4 - 100
JUMP_Y = SCREEN_Y - 100

# set the shop size
SHOP_X = SCREEN_X // 5 * 4 - 100
SHOP_Y = SCREEN_Y // 2
MENU_OPTIONS = {49: 1, 50: 2, 51: 3}

# create sprite groups
COLLISION_TYPE = pygame.sprite.Group()
DOOR_TYPE = pygame.sprite.Group()
STAIR_TYPE = pygame.sprite.Group()
MONSTER_TYPE = pygame.sprite.Group()
ITEM_TYPE = pygame.sprite.Group()
NPC_TYPE = pygame.sprite.Group()
PLAYER = pygame.sprite.Group()

# key images
KEY_IMGS = {'Yellow Key': os.path.join('Item', '5.png'),
            'Blue Key': os.path.join('Item', '6.png'),
            'Red Key': os.path.join('Item', '7.png')}
