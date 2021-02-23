import pygame

from Load import *

class SpriteSheet:

    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.__SIZE = size#size of each sprite in pixels

        self.__image = load(path, name)
        self.__Width = self.__image.get_width()
        self.__Height = self.__image.get_height()

    def __str__(self):
        return "Sheet: %s, width: %s, height: %s, Sprite sizes: %s" % (self.name, self.__Width, self.__Height, self.__SIZE)

    def getSize(self):
        return self.__SIZE

    def getSheetSize(self):
        return (self.__Width, self.__Height)

    def getSheet(self):
        return self.__image

class Sprite:

    def __init__(self, name, size, x, y, SpriteSheet):
        self.__name = name
        self.x, self.y = x, y#this is the coordinates of the sprite by  on the spritesheet by sprite
        self.__SIZE = size #this is the size its intended to be rendered at (might get rid of cause probably always be tilesize)
        self.__sheet = SpriteSheet
        self.__sprite = self.generateSprite()

    def __str__(self):
        return "Sprite: %s, Co-ordinate: (%s, %s), Sheet:  (%s)" % (self.__name, self.x, self.y, self.__sheet)

    def generateSprite(self):
        sprite = pygame.Surface((self.__SIZE, self.__SIZE))#creates surface object size of sprite
        xOffset = (self.x * self.__sheet.getSize())#gets x coordinate on sprite sheet by pixel
        yOffset = (self.y * self.__sheet.getSize())#gets y coordinate on sprite sheet by pixel
        sprite = pygame.Surface((self.__sheet.getSize(), self.__sheet.getSize()))
        sprite.blit(self.__sheet.getSheet(), (0,0), (xOffset, yOffset, xOffset + self.__sheet.getSize(), yOffset + self.__sheet.getSize()))
        sprite = pygame.transform.scale(sprite, (self.__SIZE, self.__SIZE))
        return sprite
        #There should also be something to convert alpha

    def Sprite(self):
        return self.__sprite

class PlayerSprite:
    #Might be temporary
    #This is cause bannedstory (where i got my player sprites) returned the images indivually
    def __init__(self, name, path):
        self.name = name
        self.__path = path
        self.__sprite = load(path, name + "player sprite")
        self.__Width = self.__sprite.get_width()
        self.__Height = self.__sprite.get_height()

    def __str__(self):
        return self.name

    def getSize(self):
        return (self.__Height, self.__Width)

    def Sprite(self):
        return self.__sprite

#List of Spritesheets
GrassSpriteSheet = SpriteSheet("Grassland SpriteSheet", "res/SpriteSheets/Grassland.png", 16)
CaveSpriteSheet = SpriteSheet("Cave SpriteSheet", "res/SpriteSheets/Cave.png", 32)

GhostNPCSpriteSheet = SpriteSheet("Ghost NPC SpriteSheet", "res/NPCs/Ghost SpriteSheet.png", 32)

#PowerUp
PowerUpSheet = SpriteSheet("Speed Sprite", "res/PowerUp/PowerUpSheet.png", 32)

EndSprite = SpriteSheet("End Sprite", "res/Levels/End.png ", 16)
#Later make one Spritesheet

#PlayerSprites
#(Find better way than making flipped version of sprite)
Walk1 = PlayerSprite("Walk 1", "res/PlayerSprites/walk1.png")
Walk2 = PlayerSprite("Walk 2", "res/PlayerSprites/walk2.png")
Walk3 = PlayerSprite("Walk 3", "res/PlayerSprites/walk3.png")
Walk4 = PlayerSprite("Walk 4",  "res/PlayerSprites/walk4.png")
Walking = [Walk1, Walk2, Walk3, Walk4]

Stand1 = PlayerSprite("Stand 1", "res/PlayerSprites/stand1.png")
Stand2 = PlayerSprite("Stand 2", "res/PlayerSprites/stand2.png")
Stand3 = PlayerSprite("Stand 3", "res/PlayerSprites/stand3.png")
Stand4 = PlayerSprite("Stand 4", "res/PlayerSprites/stand4.png")
Standing = [Stand1, Stand2, Stand3, Stand4]

JumpSprite = PlayerSprite("Jumping", "res/PlayerSprites/jump.png")


