import pygame

from Sprite import *

#Making an Entity class with tile power up and psiibly player/npc
class Entity:
    TILESIZE = 64
    def __init__(self, name, SpriteSheet, size):
        self.name = name
        self.__sheet = SpriteSheet
        self.__SIZE = size

    def getName(self):
        return self.name

    def generateSprite(self, x, y):
        sprite = pygame.Surface((self.__SIZE, self.__SIZE))#creates surface object size of sprite
        xOffset = (x * self.__sheet.getSize())#gets x coordinate on sprite sheet by pixel
        yOffset = (y * self.__sheet.getSize())#gets y coordinate on sprite sheet by pixel
        sprite = pygame.Surface((self.__sheet.getSize(), self.__sheet.getSize()))
        sprite.blit(self.__sheet.getSheet(), (0,0), (xOffset, yOffset, xOffset + self.__sheet.getSize(), yOffset + self.__sheet.getSize()))
        sprite = pygame.transform.scale(sprite, (self.__SIZE, self.__SIZE))
        sprite.set_colorkey((208, 0, 255))#colourkey/alpha - D000FF
        return sprite

    def render(self, window, x, y):
        window.blit(self.image, (x, y))

class PowerUp(Entity):
    #Might have a class for each power up
    SUPER_SPEED = 1#Document
    LIFE_GAIN = 2

    END = 0
    def __init__(self, name, SpriteSheet, x, y, size):
        super().__init__(name, SpriteSheet, size)
        self.image = self.generateSprite(x, y)

class Tile(Entity):
    def __init__(self, name, collsion, SpriteSheet, x, y, size):
        super().__init__(name, SpriteSheet, size)
        self.image = self.generateSprite(x, y)
        self.collsion = collsion

    def getCollsion(self):
        #0 - no collsion, 1 - stop collsion, 2- die, 3 - special (for power ups and stuff)
        return self.collsion

#List of entities
SuperSpeed = PowerUp("Speed Power Up", PowerUpSheet, 0, 0, 64)
LifeRegain = PowerUp("1 Up Power Up", PowerUpSheet, 1, 0, 64)

#List of Tiles -Still testing - Define every Tile then remove
#Later might just have thing to flip some to use less vraibles
#also better variable names
Grass1Tile = Tile("Grass 1 Tile", 1, GrassSpriteSheet, 1, 0, Tile.TILESIZE)
Dirt1Tile = Tile("Dirt 1 Tile", 1, GrassSpriteSheet, 0, 0, Tile.TILESIZE)
#Cave
CellingB1Tile = Tile("Celling Blue 1 Tile", 1, CaveSpriteSheet, 0, 0, Tile.TILESIZE)#21B6FB, (33, 182, 251)
CellingB2Tile = Tile("Celling Blue 2 Tile", 1, CaveSpriteSheet, 1, 0, Tile.TILESIZE)#056592, (5, 101, 146)
CellingB3Tile = Tile("Celling Blue 3 Tile", 1, CaveSpriteSheet, 2, 0, Tile.TILESIZE)
CellingB4Tile = Tile("Celling Blue 4 Tile", 1, CaveSpriteSheet, 3, 0, Tile.TILESIZE)#002A3E, (0, 42, 62)

BackB1Tile = Tile("Background Blue 1 Tile", 0, CaveSpriteSheet, 0, 1, Tile.TILESIZE)
BackB2Tile = Tile("Background Blue 2 Tile", 0, CaveSpriteSheet, 1, 1, Tile.TILESIZE)#021721, (2, 23, 33)
BackB3Tile = Tile("Background Blue 3 Tile", 0, CaveSpriteSheet, 2, 1, Tile.TILESIZE)
BackB4Tile = Tile("Background Blue 4 Tile", 0, CaveSpriteSheet, 3, 1, Tile.TILESIZE)

BackB5Tile = Tile("Background Blue 5 Tile", 0, CaveSpriteSheet, 0, 2, Tile.TILESIZE)
BackB6Tile = Tile("Background Blue 6 Tile", 0, CaveSpriteSheet, 1, 2, Tile.TILESIZE)
BackB7Tile = Tile("Background Blue 7 Tile", 0, CaveSpriteSheet, 2, 2, Tile.TILESIZE)
BackB8Tile = Tile("Background Blue 8 Tile", 0, CaveSpriteSheet, 3, 2, Tile.TILESIZE)

FloorB1Tile = Tile("Floor Blue 1 Tile", 1, CaveSpriteSheet, 0, 3, Tile.TILESIZE)#21B697, (33, 182, 151)
FloorB2Tile = Tile("Floor Blue 2 Tile", 1, CaveSpriteSheet, 1, 3, Tile.TILESIZE)
FloorB3Tile = Tile("Floor Blue 3 Tile", 1, CaveSpriteSheet, 2, 3, Tile.TILESIZE)#0565C9, (5, 101, 201)
FloorB4Tile = Tile("Floor Blue 4 Tile", 1, CaveSpriteSheet, 3, 3, Tile.TILESIZE)#002A8F, (0, 42, 143)

WallB1Tile = Tile("Wall Blue 1 Tile", 1, CaveSpriteSheet, 0, 4, Tile.TILESIZE)
WallB2Tile = Tile("Wall Blue 2 Tile", 1, CaveSpriteSheet, 1, 4, Tile.TILESIZE)
WallB3Tile = Tile("Wall Blue 3 Tile", 1, CaveSpriteSheet, 2, 4, Tile.TILESIZE)#056559, (5, 101, 89)
WallB4Tile = Tile("Wall Blue 4 Tile", 1, CaveSpriteSheet, 3, 4, Tile.TILESIZE)#05657C, (5, 101, 124)

CrackGTile = Tile("Cracked block Grey Tile", 1, CaveSpriteSheet, 5, 1, Tile.TILESIZE)
ArrowGTile = Tile("Arrow block Grey Tile", 1, CaveSpriteSheet, 4, 2, Tile.TILESIZE)
Block1GTile = Tile("Block 1 Grey Tile", 1, CaveSpriteSheet, 5, 2, Tile.TILESIZE)

BlockTRGTile = Tile("Block Top Right Grey Tile", 1, CaveSpriteSheet, 7, 1, Tile.TILESIZE)
BlockTLGTile = Tile("Block Top Left Grey Tile", 1, CaveSpriteSheet, 6, 1, Tile.TILESIZE)
BlockBRGTile = Tile("Block Bottom Right Grey Tile", 1, CaveSpriteSheet, 7, 2, Tile.TILESIZE)
BlockBLGTile = Tile("Block Bottom Left Grey Tile", 1, CaveSpriteSheet, 6, 2, Tile.TILESIZE)

Block2TGTile = Tile("Block 2 Top Grey Tile", 1, CaveSpriteSheet, 6, 1, Tile.TILESIZE)
Block2BGTile = Tile("Block 2 Bottom Grey Tile", 1, CaveSpriteSheet, 6, 1, Tile.TILESIZE)

Block2RGTile = Tile("Block 2 Right Grey Tile", 1, CaveSpriteSheet, 6, 1, Tile.TILESIZE)
Block2LGTile = Tile("Block 2 Left Grey Tile", 1, CaveSpriteSheet, 6, 1, Tile.TILESIZE)

LavaFullTile = Tile("Lava Full Tile", 2, CaveSpriteSheet, 4, 1, Tile.TILESIZE)#FF8D07, (255, 141, 7)
LavaHalf1Tile = Tile("Lava Half 1 Tile", 2, CaveSpriteSheet, 4, 0, Tile.TILESIZE)
LavaHalf2Tile = Tile("Lava Half 2 Tile", 2, CaveSpriteSheet, 5, 0, Tile.TILESIZE)

Block1MTile = Tile("1 Block Middle Tile", 1, CaveSpriteSheet, 8, 0, Tile.TILESIZE)#0565FF, (5, 101, 255)
Block1EndLTile = Tile("1 Block End Right Tile", 1, CaveSpriteSheet, 8, 1, Tile.TILESIZE)#21B6FF, (33, 182, 255)
Block1EndRTile = Tile("1 Block End Left Tile", 1, CaveSpriteSheet, 8, 2, Tile.TILESIZE)#21B646, (33, 182, 70)
BackGTile = Tile("Grey Background", 0, CaveSpriteSheet, 8, 3, Tile.TILESIZE)

