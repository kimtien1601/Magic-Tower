"""
This module contains all item classes which defines the effects of the items
and the message received upon collection
"""


from map import *
from constants import *


class Item(GeneralSquare):
    def add_to_group(self):
        COLLISION_TYPE.add(self)
        ITEM_TYPE.add(self)


class RedGem(Item):
    ID = 0
    message = 'Gain a red gem. ATK + 3!'

    def effect(self, player):
        player.STATE['ATK'] += 3
        return True


class BlueGem(Item):
    ID = 1
    message = 'Gain a blue gem. DEF + 3!'

    def effect(self, player):
        player.STATE['DEF'] += 3
        return True


class RedPotion(Item):
    ID = 2
    message = 'Gain a red potion. HP + 200!'

    def effect(self, player):
        player.STATE['HP'] += 200
        return True


class BluePotion(Item):
    ID = 3
    message = 'Gain a blue potion. HP + 500!'

    def effect(self, player):
        player.STATE['HP'] += 500
        return True


class HolyWater(Item):
    ID = 4
    message = 'Gain a holy water!'

    def effect(self, player):
        player.STATE['HP'] += (player.STATE['ATK'] + player.STATE['DEF']) // 2
        return True


class YellowKey(Item):
    ID = 5
    message = 'Gain a yellow key!'

    def effect(self, player):
        player.KEY_COLLECTION['Yellow Key'] += 1
        return True


class BlueKey(Item):
    ID = 6
    message = 'Gain a blue key!'

    def effect(self, player):
        player.KEY_COLLECTION['Blue Key'] += 1
        return True


class RedKey(Item):
    ID = 7
    message = 'Gain a red key!'

    def effect(self, player):
        player.KEY_COLLECTION['Red Key'] += 1
        return True


class AllKeys(Item):
    ID = 8
    message = 'Gain all type keys!'

    def effect(self, player):
        player.KEY_COLLECTION['Yellow Key'] += 1
        player.KEY_COLLECTION['Blue Key'] += 1
        player.KEY_COLLECTION['Red Key'] += 1
        return True


class Coin(Item):
    ID = 9
    message = 'Gain a coin. GOLD + 300!'

    def effect(self, player):
        player.STATE['GOLD'] += 300
        return True


class Pickaxe(Item):
    ID = 10
    message = 'Gain a pickaxe. Unlock path and stair in floor 19!'

    def effect(self, world_overlays, world_floors):
        world_overlays[18]['block_121'] = StairUp('Map', SCREEN_X / 13, SCREEN_Y / 13)
        world_overlays[18]['block_121'].set_position(SCREEN_X / 13 + SCREEN_X / 13 * 10, SCREEN_Y / 13 + SCREEN_Y / 13 * 10)
        world_floors[18]['block_94'] = Ground('Map', SCREEN_X / 13, SCREEN_Y / 13)
        world_floors[18]['block_105'] = Ground('Map', SCREEN_X / 13, SCREEN_Y / 13)
        world_floors[18]['block_94'].set_position(SCREEN_X / 13 + SCREEN_X / 13 * 5, SCREEN_Y / 13 + SCREEN_Y / 13 * 8)
        world_floors[18]['block_105'].set_position(SCREEN_X / 13 + SCREEN_X / 13 * 5, SCREEN_Y / 13 + SCREEN_Y / 13 * 9)


class Compass(Item):
    ID = 11
    message = 'Gain a compass. Press J to teleport!'

    def effect(self, player):
        player.COMPASS = True
        return True


class Cross(Item):
    ID = 12
    message = 'Gain a cross!'

    def effect(self, player):
        player.STATE['HP'] += player.STATE['HP'] // 3
        player.STATE['ATK'] += player.STATE['ATK'] // 3
        player.STATE['DEF'] += player.STATE['DEF'] // 3
        return True


class Illustration(Item):
    ID = 13
    message = 'Gain an illustration. Press I to show monster details!'

    def effect(self, player):
        player.ILLUSTRATION = True
        return True


class SmallFeather(Item):
    ID = 14
    message = 'Gain a small feather. LEVEL + 1!'

    def effect(self, player):
        player.STATE['LEVEL'] += 1
        player.STATE['HP'] += 1000
        player.STATE['ATK'] += 10
        player.STATE['DEF'] += 10
        return True


class BigFeather(Item):
    ID = 15
    message = 'Gain a big feather. LEVEL + 3!'

    def effect(self, player):
        player.STATE['LEVEL'] += 3
        player.STATE['HP'] += 3000
        player.STATE['ATK'] += 30
        player.STATE['DEF'] += 30
        return True


class Sword(Item):
    ID = 16
    message = 'Gain a sword. ATK + 10!'

    def effect(self, player):
        player.STATE['ATK'] += 10
        return True


class Sword2(Item):
    ID = 17
    message = 'Gain a sword 2. ATK + 30!'

    def effect(self, player):
        player.STATE['ATK'] += 30
        return True


class Sword3(Item):
    ID = 18
    message = 'Gain a sword 3. ATK + 70!'

    def effect(self, player):
        player.STATE['ATK'] += 70
        return True


class Sword4(Item):
    ID = 19
    message = 'Require 500 EXP to gain!'

    def effect(self, player):
        if player.STATE['EXP'] >= 500:
            player.STATE['ATK'] += 120
            player.STATE['EXP'] -= 500
            self.message = 'Gain a sword 4. ATK + 120!'
            return True
        return False


class Sword5(Item):
    ID = 20
    message = 'Gain a sword 5. ATK + 150!'

    def effect(self, player):
        player.STATE['ATK'] += 150
        return True


class Shield(Item):
    ID = 21
    message = 'Gain a shield. DEF + 10!'

    def effect(self, player):
        player.STATE['DEF'] += 10
        return True


class Shield2(Item):
    ID = 22
    message = 'Gain a shield 2. DEF + 30!'

    def effect(self, player):
        player.STATE['DEF'] += 30
        return True


class Shield3(Item):
    ID = 23
    message = 'Gain a shield 3. DEF + 85!'

    def effect(self, player):
        player.STATE['DEF'] += 85
        return True


class Shield4(Item):
    ID = 24
    message = 'Require 500 GOLD to gain!'

    def effect(self, player):
        if player.STATE['GOLD'] >= 500:
            player.STATE['DEF'] += 120
            player.STATE['GOLD'] -= 500
            self.message = 'Gain a shield 4. DEF + 120!'
            return True
        return False


class Shield5(Item):
    ID = 25
    message = 'Gain a shield 5. DEF + 190!'

    def effect(self, player):
        player.STATE['DEF'] += 190
        return True


class Staff(Item):
    ID = 26
    message = 'Gain a staff. ATK + 700, DEF + 700!'

    def effect(self, player):
        player.STATE['ATK'] += 700
        player.STATE['DEF'] += 700
        return True


def get_item(obj):
    """function to return a class of the type passed in"""

    # set item list
    ITEM_LIST = [RedGem('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 BlueGem('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 RedPotion('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 BluePotion('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 HolyWater('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 YellowKey('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 BlueKey('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 RedKey('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 AllKeys('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Coin('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Pickaxe('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Compass('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Cross('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Illustration('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 SmallFeather('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 BigFeather('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword2('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword3('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword4('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword5('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield2('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield3('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield4('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield5('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Staff('Item', SCREEN_X / 13, SCREEN_Y / 13)]

    return ITEM_LIST[obj]
