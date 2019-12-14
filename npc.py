"""
Main module for NPC classes

This module contains all classes for NPC characters in the game. The classes contain the interaction function and
details of the available options that the player will have when interacting.

All NPCs inherit their base properties from the class GeneralSquare, which in turn inherits its properties
from pygame.sprite.Sprite class. Therefore, these NPC classes can be use the normal pygame.sprite.Sprite functions.
"""

import pygame
from map import *
from constants import *


class NPC(GeneralSquare):
    """Base NPC class that defines the main interaction ability that a player has with a sprite"""
    
    def add_to_group(self):
        COLLISION_TYPE.add(self)
        NPC_TYPE.add(self)

    def action(self, player, screen):
        surf = pygame.Surface((SHOP_X, SHOP_Y))
        pygame.draw.rect(surf, ORANGE, [0, 0, SHOP_X, SHOP_Y], 5)
        font = pygame.font.Font(None, DISPLAY_SIZE_X // 40)
        x = surf.get_width() / 6
        y = surf.get_height() / 6
        count = 0
        for key in self.options:
            count += 1
            text = font.render('Press {}. Spend {} {} for adding {} {}'.format(count, self.options[key]['cost'], self.options[key]['cost_type'], self.options[key]['amount'], self.options[key]['state_type']), True, WHITE)
            surf.blit(text, (x, y))
            y += surf.get_height() / 5
        x = surf.get_width() / 3
        text = font.render('Press SPACE to return', True, WHITE)
        surf.blit(text, (x, y))
        choosing = True
        while choosing:
            screen.blit(draw_stats(player, SCREEN_X / 4, SCREEN_Y), (0, 0))
            screen.blit(surf, (DISPLAY_SIZE_X / 5 + SCREEN_X / 2 - surf.get_width() / 2, DISPLAY_SIZE_Y / 2 - surf.get_height() / 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                        if self.options[MENU_OPTIONS[event.key]]['cost_type'] in player.KEY_COLLECTION and player.KEY_COLLECTION[self.options[MENU_OPTIONS[event.key]]['cost_type']] >= self.options[MENU_OPTIONS[event.key]]['cost']:
                            player.KEY_COLLECTION[self.options[MENU_OPTIONS[event.key]]['cost_type']] -= self.options[MENU_OPTIONS[event.key]]['cost']
                            player.STATE[self.options[MENU_OPTIONS[event.key]]['state_type']] += self.options[MENU_OPTIONS[event.key]]['amount']
                        elif self.options[MENU_OPTIONS[event.key]]['state_type'] in player.KEY_COLLECTION and player.STATE[self.options[MENU_OPTIONS[event.key]]['cost_type']] >= self.options[MENU_OPTIONS[event.key]]['cost']:
                            player.STATE[self.options[MENU_OPTIONS[event.key]]['cost_type']] -= self.options[MENU_OPTIONS[event.key]]['cost']
                            player.KEY_COLLECTION[self.options[MENU_OPTIONS[event.key]]['state_type']] += self.options[MENU_OPTIONS[event.key]]['amount']
                        elif player.STATE[self.options[MENU_OPTIONS[event.key]]['cost_type']] >= self.options[MENU_OPTIONS[event.key]]['cost']:
                            player.STATE[self.options[MENU_OPTIONS[event.key]]['cost_type']] -= self.options[MENU_OPTIONS[event.key]]['cost']
                            player.STATE[self.options[MENU_OPTIONS[event.key]]['state_type']] += self.options[MENU_OPTIONS[event.key]]['amount']
                            if self.options[MENU_OPTIONS[event.key]]['state_type'] == 'LEVEL':
                                player.STATE['HP'] += 1000 * self.options[MENU_OPTIONS[event.key]]['amount']
                                player.STATE['ATK'] += 7 * self.options[MENU_OPTIONS[event.key]]['amount']
                                player.STATE['DEF'] += 7 * self.options[MENU_OPTIONS[event.key]]['amount']
                    elif event.key == pygame.K_SPACE:
                        choosing = False


class Fairy(NPC):
    ID = 'Fairy'

    def action(self, world_overlays):
        world_overlays[0]['block_92'] = Fairy('NPC', SCREEN_X / 13, SCREEN_Y / 13)
        world_overlays[0]['block_92'].set_position(SCREEN_X / 13 + SCREEN_X / 13 * 4, SCREEN_Y / 13 + SCREEN_Y / 13 * 8)
        world_overlays[0]['block_92'].add_to_group()


class GodLeft(NPC):
    ID = 'God0'

    def action(self, player):
        pass
    
    
class GodMid(NPC):
    ID = 'God1'


class GodRight(NPC):
    ID = 'God2'

    def action(self, player):
        pass


class God1(GodMid):
    options = {1: {'amount': 800, 'state_type': 'HP', 'cost': 25, 'cost_type': 'GOLD'},
               2: {'amount': 4, 'state_type': 'ATK', 'cost': 25, 'cost_type': 'GOLD'},
               3: {'amount': 4, 'state_type': 'DEF', 'cost': 25, 'cost_type': 'GOLD'}}


class God2(GodMid):
    options = {1: {'amount': 4000, 'state_type': 'HP', 'cost': 100, 'cost_type': 'GOLD'},
               2: {'amount': 20, 'state_type': 'ATK', 'cost': 100, 'cost_type': 'GOLD'},
               3: {'amount': 20, 'state_type': 'DEF', 'cost': 100, 'cost_type': 'GOLD'}}

    
class WiseMan(NPC):
    ID = 'Wise man'


class WM1(WiseMan):
    options = {1: {'amount': 1, 'state_type': 'LEVEL', 'cost': 100, 'cost_type': 'EXP'},
               2: {'amount': 5, 'state_type': 'ATK', 'cost': 30, 'cost_type': 'EXP'},
               3: {'amount': 5, 'state_type': 'DEF', 'cost': 30, 'cost_type': 'EXP'}}
    
    
class WM2(WiseMan):
    options = {1: {'amount': 3, 'state_type': 'LEVEL', 'cost': 270, 'cost_type': 'EXP'},
               2: {'amount': 17, 'state_type': 'ATK', 'cost': 95, 'cost_type': 'EXP'},
               3: {'amount': 17, 'state_type': 'DEF', 'cost': 95, 'cost_type': 'EXP'}}


class SellMan(NPC):
    ID = 'Sell man'


class SM1(SellMan):
    options = {1: {'amount': 1, 'state_type': 'Yellow Key', 'cost': 10, 'cost_type': 'GOLD'},
               2: {'amount': 1, 'state_type': 'Blue Key', 'cost': 50, 'cost_type': 'GOLD'},
               3: {'amount': 1, 'state_type': 'Red Key', 'cost': 100, 'cost_type': 'GOLD'}}


class SM2(SellMan):
    options = {1: {'amount': 7, 'state_type': 'GOLD', 'cost': 1, 'cost_type': 'Yellow Key'},
               2: {'amount': 35, 'state_type': 'GOLD', 'cost': 1, 'cost_type': 'Blue Key'},
               3: {'amount': 70, 'state_type': 'GOLD', 'cost': 1, 'cost_type': 'Red Key'}}


class Thief(NPC):
    ID = 'Thief'

    def action(self, world_overlays):
        for key in world_overlays[2]:
            if type(world_overlays[2][key]) == MagicDoor:
                world_overlays[2][key].kill()
                world_overlays[2][key] = 0


class Princess(NPC):
    ID = 'Princess'

    def action(self, player):
        pass


def draw_stats(player, width, height):
    surf = pygame.Surface((width, height))
    font = pygame.font.Font(None, DISPLAY_SIZE_X // 50)
    new_x = width / 2
    new_y = height / 7
    state_text = font.render('FLOOR: {}'.format(player.FLOOR), True, WHITE)
    surf.blit(state_text, (new_x, new_y - state_text.get_height()))
    new_y += height / 14
    for key in player.STATE:
        state_text = font.render('{}: {}'.format(key, player.STATE[key]), True, WHITE)
        surf.blit(state_text, (new_x, new_y - state_text.get_height()))
        new_y += height / 14
    for key in player.KEY_COLLECTION:
        state_text = font.render(': {}'.format(player.KEY_COLLECTION[key]), True, WHITE)
        surf.blit(state_text, (new_x + width / 4, new_y - state_text.get_height() / 2))
        img = pygame.image.load(KEY_IMGS[key])
        img = pygame.transform.scale(img, (int(SCREEN_X / 13 + 1), int(SCREEN_Y / 13 + 1)))
        surf.blit(img, (new_x - width / 8, new_y - img.get_height() / 2))
        new_y += height / 14

    wall2 = pygame.image.load(os.path.join('Map', 'Wall2.png'))
    wall2 = pygame.transform.scale(wall2, (int(SCREEN_X / 13) + 1, int(SCREEN_Y / 13) + 1))
    y1 = 0
    y2 = int(SCREEN_Y / 13 * 12)
    for x in range(4):
        surf.blit(wall2, (SCREEN_X / 13 * x, y1))
        surf.blit(wall2, (SCREEN_X / 13 * x, y2))
    x = 0
    for y in range(1, 12):
        surf.blit(wall2, (x, SCREEN_Y / 13 * y))
    return surf
