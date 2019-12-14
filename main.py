"""
This is the main file to run the game
"""

import os
import pygame
from item import *
from map import *
from monster import *
from npc import *
from player import *
from constants import *


def init_floor(level, struct):
    """function to initialise all floor sprites and positions
       Needs to be passed a floor map and initialised dictionary to fill"""
       
    row = 0
    column = 0

    for key in struct:
        if column == 11:
            column = 0
            row += 1
        #check what map datapoint represents and construct relevant class
        if level[row][column] == 0:
            struct[key] = Wall('Map', SCREEN_X / 13, SCREEN_Y / 13)
        elif level[row][column] == 1:
            struct[key] = Ground('Map', SCREEN_X / 13, SCREEN_Y / 13)
        elif level[row][column] == 2:
            struct[key] = Star('Map', SCREEN_X / 13, SCREEN_Y / 13)
        elif level[row][column] == 3:
            struct[key] = Lava('Map', SCREEN_X / 13, SCREEN_Y / 13)

        struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        column += 1

    return struct


def init_overlay(level, struct, floorNum):
    """function to initialise all overlay sprites and positions
       Needs to be passed a overlay map and initialised dictionary to fill"""
       
    row = 0
    column = 0

    for key in struct:
        if column == 11:
            column = 0
            row += 1

        #check what map datapoint represents and construct relevant class
        obj = str(level[row][column])
        if obj[0] == 'm':
            struct[key] = get_monster(int(obj[1:]))
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj[0] == 'i':
            struct[key] = get_item(int(obj[1:]))
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj[0] == 's':
            if int(obj[1:]) > floorNum:
                struct[key] = StairUp('Map', SCREEN_X / 13, SCREEN_Y / 13)
            else:
                struct[key] = StairDown('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'YD':
            struct[key] = YellowDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'BD':
            struct[key] = BlueDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'RD':
            struct[key] = RedDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'MD':
            struct[key] = MagicDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'Fairy':
            struct[key] = Fairy('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'Thief':
            struct[key] = Thief('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'Princess':
            struct[key] = Princess('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'GodL':
            struct[key] = GodLeft('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'GodM_1':
            struct[key] = God1('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'GodM_2':
            struct[key] = God2('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'GodR':
            struct[key] = GodRight('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'WM1':
            struct[key] = WM1('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'WM2':
            struct[key] = WM2('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'SM1':
            struct[key] = SM1('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'SM2':
            struct[key] = SM2('NPC', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)

        column += 1

    return struct


def init_player(player, level, init):
    """function to initalise player to starting location"""
    
    for row in range(0, 11):
        for column in range(0, 11):
            if level[row][column] == init:
                player.set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
                break


def draw_floor(struct, surf):
    for key in struct:
        struct[key].draw(surf)


def draw_overlay(struct, surf):
    for key in struct:
        try:
            struct[key].draw(surf)
        except:
            pass


def draw_outside(struct, surf):
    """function to draw the border around play area"""
    
    row = 0
    column = 0
    wall2 = pygame.image.load(os.path.join('Map', 'Wall2.png'))
    wall2 = pygame.transform.scale(wall2, (int(SCREEN_X / 13) + 1, int(SCREEN_Y / 13) + 1))

    for i in range(169):
        if column == 13:
            column = 0
            row += 1
        if struct[row][column] == 1:
            surf.blit(wall2, (SCREEN_X / 13 * column, SCREEN_Y / 13 * row))
        column += 1


def add_all_to_group(objects):
    """add all sprites in object to their relevant group"""
    
    for key in objects:
        try:
            objects[key].add_to_group()
        except:
            pass


def remove_all_from_group(objects):
    """remove all sprites in object to their relevant group"""
    
    for key in objects:
        try:
            objects[key].kill()
        except:
            pass


def fetch_floors():
    """function to gather all sprites for all floors and return them"""
    
    floors = {}
    for key in FLOORS:
        floors[key] = init_floor(FLOORS[key], block_objects.copy())
    return floors


def fetch_overlays():
    """function to gather all sprites for all overlays and return them"""
    
    overlays = {}
    i = 1
    for key in floor_overlays:
        overlays[key] = init_overlay(floor_overlays[key], overlay_objects.copy(), i)
        i += 1
    return overlays


def draw_stats(player, width, height):
    """draws the player stats to a surface and returns the surface"""
    
    surf = pygame.Surface((width, height))

    # Add text
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

    # Add key images
    for key in player.KEY_COLLECTION:
        state_text = font.render(': {}'.format(player.KEY_COLLECTION[key]), True, WHITE)
        surf.blit(state_text, (new_x + width / 4, new_y - state_text.get_height() / 2))
        img = pygame.image.load(KEY_IMGS[key])
        img = pygame.transform.scale(img, (int(SCREEN_X / 13 + 1), int(SCREEN_Y / 13 + 1)))
        surf.blit(img, (new_x - width / 8, new_y - img.get_height() / 2))
        new_y += height / 14

    # Add background
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


def draw_info(player):
    """Draws stats for the monsters on the current world floor
       Returns new surface"""
       
    surf = pygame.Surface((SCREEN_X, SCREEN_Y))
    surf.fill(GREY)
    pygame.draw.rect(surf, ORANGE, [0, 0, SCREEN_X, SCREEN_Y], 6)
    font = pygame.font.Font(None, SCREEN_Y // 25)
    x = SCREEN_X / 6
    y = SCREEN_Y / 24
    added = []
    count = 0
    for monster in MONSTER_TYPE:
        if monster.NAME in added:
            pass
        else:
            if monster.ATK <= player.STATE['DEF']:
                loss = 0
            elif player.STATE['ATK'] <= monster.DEF:
                loss = '???'
            else:
                times = monster.HP // (player.STATE['ATK'] - monster.DEF)
                loss = times * (monster.ATK - player.STATE['DEF'])
                if loss > player.STATE['HP']:
                    loss = '???'
            position = (x - SCREEN_X // 13, y)
            img = pygame.transform.scale(monster.image, (SCREEN_X // 13, SCREEN_Y // 13))
            surf.blit(img, position)
            stats = monster.stats_data()
            text = font.render('{}:  {}    {}:  {}    {}:  {}    {}:  {}    {}:  {}    {}:  {}'.format('HP', stats['HP'], 'ATK', stats['ATK'], 'DEF', stats['DEF'], 'GOLD', stats['GOLD'], 'EXP', stats['EXP'], 'LOSS', loss), True, WHITE)
            x2 = SCREEN_X / 2 - text.get_width() // 2
            surf.blit(text, (x2 + 25, y + text.get_height() // 2 + 5))
            y += SCREEN_Y / 10
            count += 1
        added.append(monster.NAME)
    return surf


def draw_jump(player, width, height, selected):
    """draws the floor jump menu
       Returns new surface"""
       
    surf = pygame.Surface((width, height))
    pygame.draw.rect(surf, ORANGE, [0, 0, width, height], 5)
    font = pygame.font.Font(None, width // 20)
    title = font.render('Floor Jump', True, WHITE)
    surf.blit(title, (width / 2 - title.get_width() / 2, height / 10))
    x = width / 9
    y = height / 4
    for i in FLOORS:
        if i > 21:
            break
        elif i == selected:
            floor_text = font.render('Floor {}'.format(i + 1), True, YELLOW)
        elif i + 1 > len(player.FLOOR_SET):
            floor_text = font.render('Floor {}'.format(i + 1), True, GREY)
        else:
            floor_text = font.render('Floor {}'.format(i + 1), True, WHITE)
        surf.blit(floor_text, (x, y))
        y += height / 11
        if i % 7 == 6:
            x += width / 3
            y = height / 4
    return surf


def draw_start():
    """Draws the start menu to a surface
       Returns new surface"""
       
    surf = pygame.Surface((DISPLAY_SIZE_X, DISPLAY_SIZE_Y))

    # Add background
    wall = pygame.image.load(os.path.join('Map', 'Wall.png'))
    wall = pygame.transform.scale(wall, (int(SCREEN_X / 13) + 1, int(SCREEN_Y / 13) + 1))
    y1 = 0
    y2 = int(SCREEN_Y / 13 * 12)
    for x in range(17):
        surf.blit(wall, (SCREEN_X / 13 * x, y1))
        surf.blit(wall, (SCREEN_X / 13 * x, y2))
    for x in [0, DISPLAY_SIZE_X - SCREEN_X / 13]:
        for y in range(1, 12):
            surf.blit(wall, (x, SCREEN_Y / 13 * y))

    # Add text
    font = pygame.font.Font(None, DISPLAY_SIZE_X // 14)
    title = font.render('MAGIC TOWER', True, WHITE)
    surf.blit(title, (DISPLAY_SIZE_X / 2 - title.get_width() / 2, DISPLAY_SIZE_Y / 5))
    font = pygame.font.Font(None, DISPLAY_SIZE_X // 20)
    start_text = font.render('START', True, YELLOW)
    surf.blit(start_text, (DISPLAY_SIZE_X / 2 - start_text.get_width() / 2, DISPLAY_SIZE_Y * 5 / 7))
    font = pygame.font.Font(None, DISPLAY_SIZE_X // 35)
    input_text = font.render('Please input your name:', True, ORANGE)
    surf.blit(input_text, (DISPLAY_SIZE_X / 2 - input_text.get_width() / 2, DISPLAY_SIZE_Y * 3 / 7))
    return surf


def draw_input(surf, text):
    """Draws the input text to the passed in surface"""
    
    w = DISPLAY_SIZE_X/3
    h = DISPLAY_SIZE_Y/14
    x = DISPLAY_SIZE_X/2 - w/2
    y = DISPLAY_SIZE_Y * 4/7 - 50
    input_box = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surf, BLACK, input_box)
    font = pygame.font.Font(None, DISPLAY_SIZE_X // 30)
    # Render the current text.
    text_print = font.render(text, True, WHITE)
    # Blit the text.
    surf.blit(text_print, (x + 15, y + 15))
    # Blit the input_box rect.
    pygame.draw.rect(surf, WHITE, input_box, 2)


# Initalize pygame and its modules to use
pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Initalize player and its position on the floor
player = Player('Player', SCREEN_X / 13, SCREEN_Y / 13)
init_player(player, floor_overlays[player.FLOOR - 1], 1)

# Initalize everything on floors
world_floors = fetch_floors()
world_overlays = fetch_overlays()

# Create a surface to add on the right of the screen
surf1 = pygame.Surface((SCREEN_X, SCREEN_Y))

# Add contents on floors to their groups
add_all_to_group(world_floors[player.FLOOR - 1])
add_all_to_group(world_overlays[player.FLOOR - 1])


# Add background music
pygame.mixer.music.load(os.path.join('Sound', 'background.mp3'))
pygame.mixer.music.play(-1)

# Show start screen
input_text = ''
screen.blit(draw_start(), (0, 0))
draw_input(screen, input_text)
pygame.display.flip()

starting = True
running = True
while starting:
    for event in pygame.event.get():
        if event.type == QUIT: # Press Quit to exit game
            starting = False
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE: # Press Esc to exit game
                starting = False
                running = False
            else:
                if event.key == pygame.K_RETURN: # Press Enter to start game
                    if input_text != '':
                        player.NAME = input_text
                        starting = False
                elif event.key == pygame.K_BACKSPACE: # Backspace handling
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode  # Input name handling
        draw_input(screen, input_text) # Update input name
        pygame.display.flip()

# Main loop
while running:
    # Draw floors, player on the surface and blit it on the right of the screen
    draw_floor(world_floors[player.FLOOR - 1], surf1)
    draw_overlay(world_overlays[player.FLOOR - 1], surf1)
    draw_outside(OUTSIDE, surf1)
    player.draw(surf1)
    screen.blit(surf1, (SCREEN_X / 4, 0))

    # Draw stats box on the left of the screen
    screen.blit(draw_stats(player, SCREEN_X / 4, SCREEN_Y), (0, 0))
    pygame.display.flip()

    temp = player.FLOOR - 1 # Get current floor
    for event in pygame.event.get():
        if event.type == QUIT: # Click Quit to exit game
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE: # Press Esc to exit game
                running = False
            elif event.key == K_i and player.ILLUSTRATION: # Press i to show information box
                screen.blit(draw_info(player), (DISPLAY_SIZE_X / 5, 0))
                pygame.display.flip()
                checking = True
                while checking:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == pygame.K_SPACE: # Press Space to show exit information
                                checking = False
                            else:
                                screen.blit(draw_info(player), (DISPLAY_SIZE_X / 5, 0))
                                pygame.display.flip()
            elif event.key == K_j and player.FLOOR < 22 and player.COMPASS: # Press j to show floor jump box
                screen.blit(draw_jump(player, JUMP_X, JUMP_Y, player.FLOOR - 1), (SCREEN_X / 4 + (SCREEN_X - JUMP_X) / 2, (SCREEN_Y - JUMP_Y) / 2))
                pygame.display.flip()
                choosing = True
                while choosing:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                if event.key == pygame.K_UP: # Move up to choose floor
                                    if player.FLOOR > 1:
                                        player.FLOOR -= 1
                                elif event.key == pygame.K_DOWN: # Move down to choose floor
                                    if player.FLOOR < 21 and player.FLOOR < len(player.FLOOR_SET):
                                        player.FLOOR += 1
                                screen.blit(draw_jump(player, JUMP_X, JUMP_Y, player.FLOOR - 1), (SCREEN_X / 4 + (SCREEN_X - JUMP_X) / 2, (SCREEN_Y - JUMP_Y) / 2))
                                pygame.display.flip()
                            elif event.key == pygame.K_RETURN: # Press Enter to select the floor
                                choosing = False
    keys = pygame.key.get_pressed()
    player.update(keys, world_overlays[player.FLOOR - 1], world_overlays, world_floors, screen) # Update player interactions

    if player.FLOOR - 1 != temp: # If player's current floor is changed
        # Remove the old floor contents from groups
        remove_all_from_group(world_floors[temp])
        remove_all_from_group(world_overlays[temp])
        COLLISION_TYPE.empty()

        if player.FLOOR - 1 > temp:  # If player has moved to upper floors
            init_player(player, floor_overlays[player.FLOOR - 1], 1)
        else: # If player has moved to lower floors
            init_player(player, floor_overlays[player.FLOOR - 1], 2)

        # Add the new floor contents to groups
        add_all_to_group(world_floors[player.FLOOR - 1])
        add_all_to_group(world_overlays[player.FLOOR - 1])

    if player.WIN: # If player defeated final boss, exit game
        running = False
    clock.tick(15 )

# Remove all floor contents from groups
remove_all_from_group(world_floors[player.FLOOR - 1])
remove_all_from_group(world_overlays[player.FLOOR - 1])

# Stop background music
pygame.mixer.music.stop()

# Exit pygame
pygame.quit()
os._exit(0) # for Mac OS
