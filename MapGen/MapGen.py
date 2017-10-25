import pygame
import random
import os
print os.getcwd()

class MAP:
    FOREST_RADIUS_MAX = 10
    FOREST_AMOUNT = 3
    BLOCK_SIZE = 80
    SIZE_Y = 60
    SIZE_X = 60
    TILE_INFO = [  # INFORMATION ON TILES (SPAWN WEIGHT, FILE NAME)
        [20, "Images/Ground/temp_grass.jpg"],
        [3, "Images/Ground/temp_mountain.jpg"],
        [5, "Images/Ground/temp_grass2.jpg"],
        [2, "Images/Ground/temp_rock.jpg"],
        [1, "Images/Ground/temp_spooky.jpg"]
    ]

class MapClass:
    """Fully extendible mapclass, image size and spawn weights can be edited"""
    map = [[0 for x in range(0, MAP.SIZE_X)] for y in range(0, MAP.SIZE_X)]  # generates a 2d array for Map size
    rivers = [[False for x in range(0, MAP.SIZE_X)] for y in range(0, MAP.SIZE_X)]
    img = pygame.Surface((MAP.SIZE_X, MAP.SIZE_Y))

    def __init__(self, seed=0):  # Initilizes Map class with a seed
        if not (seed == 0):
            random.seed(seed)
        total_weight = 0
        for i in MAP.TILE_INFO:
            total_weight += i[0]
        for y in range(0, MAP.SIZE_Y):
            for x in range(0, MAP.SIZE_X):
                rand = random.randint(0, total_weight)
                ndone = True
                for i in range(0, len(MAP.TILE_INFO)):  # Turns random number into Map tile
                    rand -= MAP.TILE_INFO[i][0]
                    if rand <= 0 and ndone:
                        ndone = False
                        self.map[x][y] = i
        self.map_render()

    def map_render(self):
        ret = pygame.Surface((MAP.SIZE_X * MAP.BLOCK_SIZE, MAP.SIZE_Y * MAP.BLOCK_SIZE))
        for y in range(0, MAP.SIZE_Y):
            for x in range(0, MAP.SIZE_X):
                temp_img = pygame.image.load(MAP.TILE_INFO[self.map[x][y]][1]).convert()
                ret.blit(temp_img, (x * MAP.BLOCK_SIZE, y * MAP.BLOCK_SIZE))
        self.img = ret

    def draw_forest(self):
        print

screen = pygame.display.set_mode((800, 500))
Map = MapClass()
pygame.init()
temp_scroll = [0, 0]  # TEMP SCROLL MECHANIC


def display():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

            """TEMPORARY SCROLL MECHANIC"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if temp_scroll[0] > 0:
                        temp_scroll[0] -= 50

                if event.key == pygame.K_RIGHT:
                    if temp_scroll[0] < (MAP.SIZE_X * MAP.BLOCK_SIZE - 800):
                        temp_scroll[0] += 50

                if event.key == pygame.K_UP:
                    if temp_scroll[1] > 0:
                        temp_scroll[1] -= 50

                if event.key == pygame.K_DOWN:
                    if temp_scroll[1] < (MAP.SIZE_Y * MAP.BLOCK_SIZE - 500):
                        temp_scroll[1] += 50
            """END TEMP SCROLL MECHANIC"""

        screen.blit(Map.img, (-temp_scroll[0], -temp_scroll[1]))
        pygame.display.flip()


display()