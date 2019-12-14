"""
This module contains all monster classes and defines the stats of all monsters
and handles the display of battles with monsters
"""

import pygame
from constants import *


class Monster(GeneralSquare):
    """Main class for monster"""
    ATK2 = 0
    ATK3 = 0

    def add_to_group(self):
        COLLISION_TYPE.add(self)
        MONSTER_TYPE.add(self)

    def stats_data(self):
        return {'HP': self.HP, 'ATK': self.ATK, 'DEF': self.DEF, 'GOLD': self.GOLD, 'EXP': self.EXP}

    def draw_popup(self, player, screen):
        surf = pygame.Surface((POPUP_X, POPUP_Y))
        surf.fill(GREY)
        pygame.draw.rect(surf, [179, 89, 0], [0, 0, POPUP_X, POPUP_Y], 4)
        font = pygame.font.Font(None, DISPLAY_SIZE_X // 40)

        # Draw monster
        monster_img = pygame.transform.scale(self.image, (AVATAR, AVATAR))
        surf.blit(monster_img, ((POPUP_X - 2 * AVATAR) / 6, (POPUP_Y - AVATAR) / 3))
        pygame.draw.rect(surf, [179, 89, 0], [(POPUP_X - 2 * AVATAR) / 6 - 20, (POPUP_Y - AVATAR) / 3 - 20, AVATAR + 40, AVATAR + 40], 2)

        monster_name = font.render(self.NAME, True, WHITE)
        surf.blit(monster_name, ((POPUP_X - 2 * AVATAR) / 6 + AVATAR / 2 - monster_name.get_width() / 2, (POPUP_Y - AVATAR) / 3 + AVATAR + 40))

        # Draw player
        player_img = pygame.transform.scale(player.image, (AVATAR, AVATAR))
        surf.blit(player_img, ((POPUP_X - 2 * AVATAR) * 5 / 6 + AVATAR, (POPUP_Y - AVATAR) / 3))
        pygame.draw.rect(surf, [179, 89, 0], [(POPUP_X - 2 * AVATAR) * 5 / 6 + AVATAR - 20, (POPUP_Y - AVATAR) / 3 - 20, AVATAR + 40, AVATAR + 40], 2)

        player_name = font.render(player.NAME, True, WHITE)
        surf.blit(player_name, ((POPUP_X - 2 * AVATAR) * 5 / 6 + 3 * AVATAR / 2 - player_name.get_width() / 2, (POPUP_Y-AVATAR) / 3 + AVATAR + 40))

        # Play continuous batte sound
        effect = pygame.mixer.Sound(os.path.join('Sound', 'fight.wav'))
        effect.play(-1)

        while self.HP > 0:
            pygame.draw.rect(surf, GREY, pygame.Rect(POPUP_X * 3 / 10, 20, (POPUP_X - 2 * AVATAR) * 5 / 6 + AVATAR - POPUP_X * 3 / 10 - 20, POPUP_Y - 40))
            # Draw VS
            font2 = pygame.font.Font(None, DISPLAY_SIZE_X // 13)
            VS_text = font2.render('VS', True, WHITE)
            surf.blit(VS_text, (POPUP_X / 2 - 70, POPUP_Y / 2 - 50))

            # Monster state
            monster_dict = {'HP': self.HP, 'ATK': self.ATK, 'DEF': self.DEF}
            y = POPUP_Y / 5
            for key in monster_dict:
                state_text = font.render('{}:   {}'.format(key, monster_dict[key]), True, WHITE)
                surf.blit(state_text, (POPUP_X * 3 / 10, y))
                y += POPUP_Y / 5

            # Player state
            y = POPUP_Y / 5
            for key in ['HP', 'ATK', 'DEF']:
                state_text = font.render('{}:   {}'.format(key, player.STATE[key]), True, WHITE)
                surf.blit(state_text, (POPUP_X * 3 / 5 - 10, y))
                y += POPUP_Y / 5

            # Display on screen
            screen.blit(surf, ((SCREEN_X * 5 / 4 - POPUP_X) / 2, SCREEN_Y / 6))
            pygame.display.flip()
            pygame.time.wait(250)

            monster_minus = player.STATE['ATK'] - self.DEF
            self.HP -= monster_minus
            if self.HP <= 0:
                break

            if self.ATK > player.STATE['DEF']:
                player_minus = self.ATK - player.STATE['DEF']
            else:
                player_minus = 0
            player.STATE['HP'] -= player_minus

        # Stop batte sound
        effect.stop()

class GreenSlime(Monster):
    NAME = 'Green Slime'
    ID = 0
    HP = 50
    ATK = 20
    DEF = 1
    GOLD = 1
    EXP = 1


class RedSlime(Monster):
    NAME = 'Red Slime'
    ID = 1
    HP = 70
    ATK = 15
    DEF = 2
    GOLD = 2
    EXP = 2


class SmallBat(Monster):
    NAME = 'Small Bat'
    ID = 2
    HP = 100
    ATK = 20
    DEF = 5
    GOLD = 3
    EXP = 3


class Skeleton(Monster):
    NAME = 'Skeleton'
    ID = 3
    HP = 110
    ATK = 25
    DEF = 5
    GOLD = 5
    EXP = 4


class BlackSlime(Monster):
    NAME = 'Black Slime'
    ID = 4
    HP = 200
    ATK = 35
    DEF = 10
    GOLD = 5
    EXP = 5


class SkeletonSoldier(Monster):
    NAME = 'Skeleton Soldier'
    ID = 5
    HP = 150
    ATK = 40
    DEF = 20
    GOLD = 8
    EXP = 6


class JuniorWizard(Monster):
    NAME = 'Junior Wizard'
    ID = 6
    HP = 125
    ATK = 50
    DEF = 25
    GOLD = 10
    EXP = 7


class BigBat(Monster):
    NAME = 'Big Bat'
    ID = 7
    HP = 150
    ATK = 65
    DEF = 30
    GOLD = 10
    EXP = 8


class Ogre(Monster):
    NAME = 'Ogre'
    ID = 8
    HP = 300
    ATK = 75
    DEF = 45
    GOLD = 13
    EXP = 10


class SkeletonCaptain(Monster):
    NAME = 'Skeleton Captain'
    ID = 9
    HP = 400
    ATK = 90
    DEF = 50
    GOLD = 15
    EXP = 12


class RockMonster(Monster):
    NAME = 'Rock Monster'
    ID = 10
    HP = 500
    ATK = 115
    DEF = 65
    GOLD = 15
    EXP = 15


class Magician(Monster):
    NAME = 'Magician'
    ID = 11
    HP = 250
    ATK = 120
    ATK2 = 100
    DEF = 70
    GOLD = 20
    EXP = 17


class JuniorGuard(Monster):
    NAME = 'Junior Guard'
    ID = 12
    HP = 450
    ATK = 150
    DEF = 90
    GOLD = 22
    EXP = 19


class RedBat(Monster):
    NAME = 'Red Bat'
    ID = 13
    HP = 550
    ATK = 160
    DEF = 90
    GOLD = 25
    EXP = 20


class SeniorWizard(Monster):
    NAME = 'Senior Wizard'
    ID = 14
    HP = 100
    ATK = 200
    DEF = 110
    GOLD = 30
    EXP = 25


class SlimeKing(Monster):
    NAME = 'Slime King'
    ID = 15
    HP = 700
    ATK = 250
    DEF = 125
    GOLD = 32
    EXP = 30


class WhiteWarrior(Monster):
    NAME = 'White Warrior'
    ID = 16
    HP = 1300
    ATK = 150
    ATK3 = 4
    DEF = 150
    GOLD = 40
    EXP = 35


class GoldKnight(Monster):
    NAME = 'Gold Knight'
    ID = 17
    HP = 850
    ATK = 350
    DEF = 200
    GOLD = 45
    EXP = 40


class RedMagician(Monster):
    NAME = 'Red Magician'
    ID = 18
    HP = 500
    ATK = 400
    ATK2 = 300
    DEF = 260
    GOLD = 47
    EXP = 45


class OgreSoldier(Monster):
    NAME = 'Ogre Soldier'
    ID = 19
    HP = 900
    ATK = 450
    DEF = 330
    GOLD = 50
    EXP = 50


class GhostGuard(Monster):
    NAME = 'Ghost Guard'
    ID = 20
    HP = 1250
    ATK = 500
    DEF = 400
    GOLD = 55
    EXP = 55


class SeniorGuard(Monster):
    NAME = 'Senior Guard'
    ID = 21
    HP = 1500
    ATK = 560
    DEF = 460
    GOLD = 60
    EXP = 60


class Swordsman(Monster):
    NAME = 'Swordsman'
    ID = 22
    HP = 1200
    ATK = 620
    DEF = 520
    GOLD = 65
    EXP = 75


class GhostWarrior(Monster):
    NAME = 'Ghost Warrior'
    ID = 23
    HP = 2000
    ATK = 680
    DEF = 590
    GOLD = 70
    EXP = 65


class RedKnight(Monster):
    NAME = 'Red Knight'
    ID = 24
    HP = 900
    ATK = 750
    DEF = 650
    GOLD = 77
    EXP = 70


class GhostMagician(Monster):
    NAME = 'Ghost Magician'
    ID = 25
    HP = 1500
    ATK = 830
    ATK3 = 3
    DEF = 730
    GOLD = 80
    EXP = 70


class GhostMagician2(Monster):
    NAME = 'Ghost Magician 2'
    ID = 25
    HP = 2000
    ATK = 1106
    ATK3 = 3
    DEF = 973
    GOLD = 106
    EXP = 93


class GhostMagician3(Monster):
    NAME = 'Ghost Magician 3'
    ID = 25
    HP = 3000
    ATK = 2212
    ATK3 = 3
    DEF = 1946
    GOLD = 132
    EXP = 116


class GhostKnight(Monster):
    NAME = 'Ghost Knight'
    ID = 26
    HP = 2500
    ATK = 900
    DEF = 850
    GOLD = 84
    EXP = 75


class GhostKnight2(Monster):
    NAME = 'Ghost Knight 2'
    ID = 26
    HP = 3333
    ATK = 1200
    DEF = 1133
    GOLD = 112
    EXP = 100


class ShadowWarrior(Monster):
    NAME = 'Shadow Warrior'
    ID = 27
    HP = 3100
    ATK = 1150
    DEF = 1050
    GOLD = 92
    EXP = 80


class BlackWarrior(Monster):
    NAME = 'Black Warrior'
    ID = 28
    HP = 1200
    ATK = 980
    DEF = 900
    GOLD = 88
    EXP = 75


class BlackWarrior2(Monster):
    NAME = 'Black Warrior 2'
    ID = 28
    HP = 1600
    ATK = 1306
    DEF = 1200
    GOLD = 117
    EXP = 100


class BlackWarrior3(Monster):
    NAME = 'Black Warrior 3'
    ID = 28
    HP = 2400
    ATK = 2612
    DEF = 2400
    GOLD = 146
    EXP = 125


class RedDevil(Monster):
    NAME = 'Red Devil'
    ID = 29
    HP = 15000
    ATK = 1000
    DEF = 1000
    GOLD = 100
    EXP = 100


class RedDevil2(Monster):
    NAME = 'Red Devil 2'
    ID = 29
    HP = 20000
    ATK = 1333
    DEF = 1333
    GOLD = 133
    EXP = 133


class RedDevil3(Monster):
    NAME = 'Red Devil 3'
    ID = 29
    HP = 30000
    ATK = 2666
    DEF = 2666
    GOLD = 166
    EXP = 166


class Vampire(Monster):
    NAME = 'Vampire'
    ID = 30
    HP = 30000
    ATK = 1700
    DEF = 1500
    GOLD = 150
    EXP = 120


class Vampire2(Monster):
    NAME = 'Vampire 2'
    ID = 30
    HP = 45000
    ATK = 2550
    DEF = 2250
    GOLD = 312
    EXP = 275


class Vampire3(Monster):
    NAME = 'Vampire 3'
    ID = 30
    HP = 60000
    ATK = 3400
    DEF = 3000
    GOLD = 390
    EXP = 343


class Boss(Monster):
    NAME = 'Boss'
    ID = 31
    HP = 99999
    ATK = 5000
    DEF = 4000
    GOLD = 0
    EXP = 0


def get_monster(obj):
    """function to return a class of the type passed in"""

    # set monsters list
    MONSTER_LIST = [GreenSlime('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    RedSlime('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    SmallBat('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    Skeleton('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    BlackSlime('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    SkeletonSoldier('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    JuniorWizard('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    BigBat('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    Ogre('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    SkeletonCaptain('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    RockMonster('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    Magician('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    JuniorGuard('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    RedBat('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    SeniorWizard('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    SlimeKing('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    WhiteWarrior('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    GoldKnight('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    RedMagician('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    OgreSoldier('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    GhostGuard('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    SeniorGuard('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    Swordsman('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    GhostWarrior('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    RedKnight('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    GhostMagician('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    GhostMagician2('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    GhostMagician3('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    GhostKnight('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    GhostKnight2('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    ShadowWarrior('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    BlackWarrior('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    BlackWarrior2('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    BlackWarrior3('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    RedDevil('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    RedDevil2('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    RedDevil3('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    Vampire('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    Vampire2('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    Vampire3('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                    Boss('Monster', SCREEN_X / 13 * 3, SCREEN_Y / 13 * 3)]

    return MONSTER_LIST[obj]
