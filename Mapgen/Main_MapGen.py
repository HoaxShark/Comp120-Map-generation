import pygame
import random


class MAPCONST:
    BLOCK_SIZE = 80
    SIZE_Y_MAX = 30
    SIZE_X_MAX = 30
    RIVER_CHANCE = 200
    RIVER_LENGTH = 15
    RIVER_MIN = 5
    TILE_INFO = [ # INFORMATION ON TILES (SPAWN WEIGHT, FILE NAME)
        [20,"TEMP1.jpg"],
        [40,"TEMP2.jpg"]
    ]
    RIVER_TILE = [ # Information on river tiles (filename)
        ["START.jpg"],  # Start river tile
        ["END.jpg"],  # End river tile
        ["VERTICAL.jpg"],  #
        ["HORIZONTAL.jpg"],
        ["BEND_LEFT.jpg"],
        ["BEND_RIGHT.jpg"],
        ["LEFT_DOWN.jpg"],
        ["RIGHT_DOWN.jpg"],
        ["END_LEFT.jpg"],
        ["END_RIGHT.jpg"]
    ]

class MapClass:
    Map = [[0 for x in range (MAPCONST.SIZE_X_MAX)]for y in range (MAPCONST.SIZE_X_MAX)]  # Random Numbers Into Map
    Terrain = [[0 for x in range (Const.MAP.SIZE_X_MAX)]for y in range (MAPCONST.SIZE_X_MAX)] # Create array for terrain
    def __init__(self,Seed=0):
        if (not (Seed == 0)):
            random.seed(Seed)
        total_weight=0
        for i in MAPCONST.TILE_INFO:
            total_weight += i[0]
        for y in range(0,MAPCONST.SIZE_Y_MAX):
            for x in range(0,MAPCONST.SIZE_Y_MAX):  # Each Block
                temp = random.randint(0, total_weight)
                for i in range(0,len(MAPCONST.TILE_INFO)):
                    if temp-MAPCONST.TILE_INFO[i][0]<= 0:  # Weights The Random Number
                        self.Map[x][y] = i

    def create_river(self,surf):
        for y in range(0,MAPCONST.SIZE_Y_MAX):
            for x in range(0, MAPCONST.SIZE_X_MAX):
                number = random.randint(0,MAPCONST.RIVER_CHANCE)
                if number == 42: # If tile number is 42
                    self.Terrain[x][y] = 1
                    placeX = x
                    placeY = y
                    end = 0
                    river_length = random.randint(MAPCONST.RIVER_MIN,MAPCONST.RIVER_LENGTH)
                    temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[0][0]).convert() # Load river start image
                    surf.blit(temp_riv,(x*MAPCONST.BLOCK_SIZE,y*MAPCONST.BLOCK_SIZE))
                    placeY += 1
                    ran_tile = random.randint(4, 5)

                    for i in range(0, river_length):
                        end += 1
                        temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[ran_tile][0]).convert()
                        if ran_tile == 4:  # Blit tile left one block
                            surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                            placeX -= 1
                            ran_tile = random.randint(4, 7)
                            if end == river_length:
                                temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[8][0]).convert()
                                surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                            elif ran_tile is not 6:
                                ran_tile = 6
                                ran_length = random.randint(1, 2)
                                temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[3][0]).convert()
                                for i in range(0,ran_length):
                                    surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                                    placeX -= 1
                        elif ran_tile == 5:  # Blit tile right one block
                            surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                            placeX += 1
                            ran_tile = random.randint(4, 7)
                            if end == river_length:
                                temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[9][0]).convert()
                                surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                            elif ran_tile is not 7:
                                ran_tile = 7
                                ran_length = random.randint(1, 2)
                                temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[3][0]).convert()
                                for i in range(0,ran_length):
                                    surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                                    placeX += 1
                        elif ran_tile == 6:  # Blit tile right one block
                            surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                            placeY += 1
                            ran_tile = random.randint(4, 7)
                            if end == river_length:
                                temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[1][0]).convert()
                                surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                            elif ran_tile is not 4 or 5:
                                ran_tile = random.randint(4,5)
                                ran_length = random.randint(1, 2)
                                temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[2][0]).convert()
                                for i in range(0,ran_length):
                                    surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                                    placeY += 1
                        elif ran_tile == 7:  # Blit tile down one block
                            surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                            placeY += 1
                            ran_tile = random.randint(4, 7)
                            if end == river_length:
                                temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[1][0]).convert()
                                surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                            elif ran_tile is not 4 or 5:
                                ran_tile = random.randint(4, 5)
                                ran_length = random.randint(1, 2)
                                temp_riv = pygame.image.load(MAPCONST.RIVER_TILE[2][0]).convert()
                                for i in range(0,ran_length):
                                    surf.blit(temp_riv, (placeX * MAPCONST.BLOCK_SIZE, placeY * MAPCONST.BLOCK_SIZE))
                                    placeY += 1


        return surf

    def render(self):
        ret = pygame.Surface((MAPCONST.SIZE_X_MAX*MAPCONST.BLOCK_SIZE,MAPCONST.SIZE_Y_MAX*MAPCONST.BLOCK_SIZE))
        for y in range(0,MAPCONST.SIZE_Y_MAX):
            for x in range(0, MAPCONST.SIZE_X_MAX):
                temp_img = pygame.image.load(MAPCONST.TILE_INFO[self.Map[x][y]][1]).convert()
                ret.blit(temp_img,(x*MAPCONST.BLOCK_SIZE,y*MAPCONST.BLOCK_SIZE))
        ret = self.create_river(ret)
        return ret


screen = pygame.display.set_mode((1600,1000))
Map= MapClass()
pygame.init()

img=Map.render()


def SCREEN():
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done=True
        screen.blit(img,(0,0))
        pygame.display.flip()
SCREEN()