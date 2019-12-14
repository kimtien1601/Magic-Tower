"""
This module contains the player class which defines the players abilities and
interactions with the world and handles player movement
"""


import os
import pygame
from map import *
from constants import *

class Player(GeneralSquare):
    """Main class for player"""
    
    ID = 'default'
    NAME = ''
    STATE = {'LEVEL': 1, 'HP': 1000, 'ATK': 10, 'DEF': 10, 'GOLD': 0, 'EXP': 0}
    KEY_COLLECTION = {'Yellow Key': 1, 'Blue Key': 1, 'Red Key': 1}
    FLOOR = 1
    FLOOR_SET = {FLOOR} #storing floors have been through
    COMPASS = False
    ILLUSTRATION = False
    WIN = False

    def playSound(self, file):
        """function to play sound effect"""

        effect = pygame.mixer.Sound(os.path.join('Sound', file))
        effect.play()

    def showMessage(self, text, screen):
        """ function to show message box on screen"""
        
        width = SCREEN_X - 100
        height = SCREEN_Y // 7
        surf = pygame.Surface((width, height))
        pygame.draw.rect(surf, ORANGE, [0, 0, width, height], 5)
        font = pygame.font.Font(None, width // 25)
        text_print = font.render('{}'.format(text), True, WHITE)
        surf.blit(text_print, (width / 2 - text_print.get_width() / 2, height / 2 - 20))
        screen.blit(surf, (SCREEN_X / 4 + (SCREEN_X - width) / 2, (SCREEN_Y - height) / 2))
        pygame.display.flip()
        pygame.time.wait(750)

    def update(self, pressed_keys, overlay, world_overlays, world_floors, screen):
        """function to update player interactions"""

        old_position = self.rect[0:2]
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, int(-SCREEN_Y / 13))
        elif pressed_keys[K_DOWN]:
            self.rect.move_ip(0, int(SCREEN_Y / 13))
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(int(SCREEN_X / 13), 0)
        elif pressed_keys[K_LEFT]:
            self.rect.move_ip(int(-SCREEN_X / 13), 0)

        if pygame.sprite.spritecollideany(self, COLLISION_TYPE):

            # If the player collide a door
            if pygame.sprite.spritecollideany(self, DOOR_TYPE):
                for key in overlay:
                    if type(overlay[key]) == YellowDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['Yellow Key'] > 0:
                                self.KEY_COLLECTION['Yellow Key'] -= 1
                                overlay[key].kill()
                                overlay[key] = 0
                    elif type(overlay[key]) == BlueDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['Blue Key'] > 0:
                                self.KEY_COLLECTION['Blue Key'] -= 1
                                overlay[key].kill()
                                overlay[key] = 0
                    elif type(overlay[key]) == RedDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['Red Key'] > 0:
                                self.KEY_COLLECTION['Red Key'] -= 1
                                overlay[key].kill()
                                overlay[key] = 0

            # If the player collide a stair
            if pygame.sprite.spritecollideany(self, STAIR_TYPE):
                for key in overlay:
                    if type(overlay[key]) == StairUp:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.FLOOR += 1
                            self.FLOOR_SET = self.FLOOR_SET | {self.FLOOR}
                    elif type(overlay[key]) == StairDown:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.FLOOR -= 1
                            self.FLOOR_SET = self.FLOOR_SET | {self.FLOOR}

            # If the player collide a monster
            if pygame.sprite.spritecollideany(self, MONSTER_TYPE):
                for key in overlay:
                    try:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            # Check condition for ability to fight
                            monster_ability = {'HP': overlay[key].HP, 'ATK': overlay[key].ATK, 'ATK2': overlay[key].ATK2, 'ATK3': overlay[key].ATK3, 'DEF': overlay[key].DEF}
                            player_ability = {'HP': self.STATE['HP'], 'ATK': self.STATE['ATK'], 'DEF': self.STATE['DEF']}

                            if monster_ability['ATK'] > player_ability['DEF']:
                                player_minus = monster_ability['ATK'] - player_ability['DEF']
                            else:
                                player_minus = 0

                            if player_ability['ATK'] > monster_ability['DEF']:
                                monster_minus = player_ability['ATK'] - monster_ability['DEF']
                            else:
                                break

                            if monster_ability['ATK2'] != 0:
                                player_ability['HP'] -= monster_ability['ATK2']

                            if monster_ability['ATK3'] != 0:
                                player_ability['HP'] -= player_ability['HP'] // monster_ability['ATK3']

                            while monster_ability['HP'] > 0 and player_ability['HP'] > 0:
                                monster_ability['HP'] -= monster_minus
                                player_ability['HP'] -= player_minus

                            # If player wins
                            if monster_ability['HP'] <= 0:
                                if monster_ability['ATK2'] != 0:
                                    self.STATE['HP'] -= monster_ability['ATK2']
                                if monster_ability['ATK3'] != 0:
                                    self.STATE['HP'] -= self.STATE['HP'] // monster_ability['ATK3']
                                overlay[key].draw_popup(self, screen) # draw battle box
                                self.STATE['GOLD'] += overlay[key].GOLD
                                self.STATE['EXP'] += overlay[key].EXP
                                if overlay[key].NAME == 'Boss':
                                    self.showMessage('You have conquered the magic tower!', screen)
                                    self.WIN = True
                                overlay[key].kill()
                                overlay[key] = 0
                    except AttributeError:
                        pass

            # If the player collide an NPC
            if pygame.sprite.spritecollideany(self, NPC_TYPE):
                i = 0
                for key in overlay:
                    try:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if overlay[key].ID == 'Fairy':
                                print('Fairy')
                                overlay[key].action(world_overlays)
                                print('Fairy2')
                                self.showMessage('Hi {}! Welcome to Magic Tower! Enjoy your game!'.format(self.NAME), screen)
                                if i == 93:
                                    overlay[key].kill()
                                    overlay[key] = 0
                            elif overlay[key].ID == 'Thief':
                                overlay[key].action(world_overlays)
                                self.showMessage('Thanks for saving me, {}! I will open the magic door in floor 3 for you!'.format(self.NAME), screen)
                                overlay[key].kill()
                                overlay[key] = 0
                            elif overlay[key].ID == 'Princess':
                                self.showMessage('You are my hero, {}! I will wait for you here until you defeat final boss!'.format(self.NAME), screen)
                            else:
                                overlay[key].action(self, screen)
                    except AttributeError:
                        pass
                    i += 1

            # If the player collide an item
            if pygame.sprite.spritecollideany(self, ITEM_TYPE):
                for key in overlay:
                    try:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.playSound('pickup.wav')
                            if overlay[key].ID == 10:
                                overlay[key].effect(world_overlays, world_floors)
                                self.showMessage(overlay[key].message, screen)
                                overlay[key].kill()
                                overlay[key] = 0
                            elif overlay[key].effect(self):
                                self.showMessage(overlay[key].message, screen)
                                overlay[key].kill()
                                overlay[key] = 0
                            else:
                                self.showMessage(overlay[key].message, screen)
                    except AttributeError:
                        pass

            self.rect[0:2] = old_position
        elif self.rect[0] < int(SCREEN_X / 13) or self.rect.right > int(SCREEN_X / 13 * 12) or self.rect[1] < int(SCREEN_Y / 13) or self.rect.bottom > int(SCREEN_Y / 13 * 12):
            self.rect[0:2] = old_position
