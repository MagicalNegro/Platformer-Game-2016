import pygame

from Entity import *
from Mob import *
from Load import *
from Files import *

class Level:
    #add sprite stuff (group.draw)
    def __init__(self, name, path, background):
        self.name = name
        self.path = path
        self.background = background
        self.__image = load(path, name)
        self.Width = self.__image.get_width()
        self.Height = self.__image.get_height()
        self.blockList = self.__generateLevel()
        self.gravity = 0.5#figure out later
        self.PowerUpCollection = []
        self.AllPowerUps = []
        self.EndInLevel = False

        #Document
        self.MobCollection = []
        self.AllMobs = []

    def __generateLevel(self):
        level = []
        for x in range(self.Width):
            temp = []
            for y in range(self.Height):
                temp.append(self.getTile(x, y))
            level.append(temp)
        return level

    def getBlockList(self):
        return self.blockList

    def addPowerUp(self, PowerUpType, x, y):
        self.PowerUpCollection.append((PowerUpType, x, y))
        self.AllPowerUps.append((PowerUpType, x, y))

    def getPowerUp(self, PowerUpType):
        AddedPowerUp = None
        if PowerUpType == PowerUp.SUPER_SPEED:
            AddedPowerUp = SuperSpeed
        elif PowerUpType == PowerUp.LIFE_GAIN:
            AddedPowerUp = LifeRegain

        elif PowerUpType == PowerUp.END:
            AddedPowerUp = PowerUp("End of Level", EndSprite, 0, 0, 64)
        return AddedPowerUp

    def addMob(self, MobType, x, y):
        x = (x*64)
        y = (y*64)
        if MobType == Mob.GHOST_NPC:
            AddedMob = GhostNPC(Tile.TILESIZE)
        AddedMob.setPos(x, y)
        self.MobCollection.append(AddedMob)
        self.AllMobs.append(AddedMob)

    def End(self, x, y):
        if not self.EndInLevel:
            self.PowerUpCollection.append((PowerUp.END, x, y))#Cause its similar to power up
            self.AllPowerUps.append((PowerUp.END, x, y))
        self.EndInLevel = True#makes sure only one end to level

    def Reset(self):
        #cause when level finished then started again power ups and end missing
        self.PowerUpCollection = list(self.AllPowerUps)
        #self.MobCollection = self.AllMobs

        #Needs to decide whether to put mobs back in orginal place

        #After 2 atttempts on same level stops woking

    def getTile(self, x, y):
        #Treats the image like an 2d array
        #gets the colour of the pixel at the certian point in the array and returns the corisponding Tile
        colour = self.__image.get_at((x, y))
        if colour == (0, 255, 0):
            return Grass1Tile
        if colour == (int(0x7F), int(0x33), 0):
            return Dirt1Tile
        if colour == (33, 182, 251):
            return CellingB1Tile
        if colour == (5, 101, 146):
            return CellingB2Tile
        if colour == (0, 42, 62):
            return CellingB4Tile
        if colour == (255, 141, 7):
            return LavaFullTile
        if colour == (2, 23, 33):
            return BackB2Tile
        if colour == (33, 182, 151):
            return FloorB1Tile
        if colour == (5, 101, 201):
            return FloorB3Tile
        if colour == (0, 42, 143):
            return FloorB4Tile
        if colour == (5, 101, 89):
            return WallB3Tile
        if colour == (5, 101, 255):
            return Block1MTile
        if colour == (33, 182, 255):
            return Block1EndRTile
        if colour == (33, 182, 70):
            return Block1EndLTile
        if colour == (5, 101, 124):
            return WallB4Tile
        return None

    def update(self, tick):
        #handles all the update things to do with things in levels e.g. mobs
        for mob in self.MobCollection:
            mob.update(self.blockList, tick)

    def renderTiles(self, window, xOffset, yOffset):
        for x in range(self.Width):
            for y in range(self.Height):
                #TILESIZE from Tile module
                xPos = (x * Tile.TILESIZE) - xOffset
                yPos = (y * Tile.TILESIZE) - yOffset
                Block = self.blockList[x][y]
                if Block:
                    #None = False
                    if xPos > -Tile.TILESIZE or yPos > -Tile.TILESIZE or xPos < (window.get_width()+Tile.TILESIZE) or yPos < (window.get_height()+Tile.TILESIZE):
                        #Should make it more efficent so blocks on screen arent attempted to be rendered
                        Block.render(window, xPos, yPos)

    def renderMobs(self, window, xOffset, yOffset):
        #document
        for mob in self.MobCollection:
            xPos = mob.getXMov() - xOffset#Document
            yPos = mob.getYMov() - yOffset#Documet
            if xPos > -Tile.TILESIZE or yPos > -Tile.TILESIZE or xPos < (window.get_width()+Tile.TILESIZE) or yPos < (window.get_height()+Tile.TILESIZE):
                mob.render(window, xPos, yPos)

    def renderPowerUps(self, window, xOffset, yOffset):
        for item in self.PowerUpCollection:
            xPos = (item[1]*64) - xOffset
            yPos = (item[2]*64) - yOffset
            if xPos > -Tile.TILESIZE or yPos > -Tile.TILESIZE or xPos < (window.get_width()+Tile.TILESIZE) or yPos < (window.get_height()+Tile.TILESIZE):
                image = self.getPowerUp(item[0])
                image.render(window, xPos, yPos)

    def render(self, window, xOffset, yOffset):
        window.fill(self.background)
        self.renderTiles(window, xOffset, yOffset)
        self.renderPowerUps(window, xOffset, yOffset)
        self.renderMobs(window, xOffset, yOffset)

#List of Levels
#For mobs could define their postion on map here - and have one big mob class and sub classes of mobs
#PowerUps aswell
TestLevelGrass = Level("Test Level 1", "res/Levels/platTestLevel.png", (135, 206, 234))#87CEEA, (135, 206, 234)
TestLevelGrass.End(16, 15)

Level_1 = Level("Test Level 1", "res/Levels/platTestLevel.png", (135, 206, 234))#87CEEA, (135, 206, 234)
Level_1.End(16, 15)
Level_1.addMob(Mob.GHOST_NPC, 15, 11)
Level_2 = Level("Level 2", "res/Levels/Level 2.png", (135, 206, 234))
Level_2.End(20, 21)
Level_2.addMob(Mob.GHOST_NPC, 23, 5)
Level_2.addMob(Mob.GHOST_NPC, 23, 11)
Level_2.addMob(Mob.GHOST_NPC, 23, 17)
Level_2.addPowerUp(PowerUp.SUPER_SPEED, 10, 11)
Level_2.addPowerUp(PowerUp.SUPER_SPEED, 9, 17)
Level_3 = Level("Level 3", "res/Levels/Level 3.png", (135, 206, 234))
Level_3.End(20, 21)
Level_3.addPowerUp(PowerUp.LIFE_GAIN, 2, 20)
Level_3.addPowerUp(PowerUp.SUPER_SPEED, 11, 12)
Level_3.addMob(Mob.GHOST_NPC, 2, 20)
Level_4 = Level("Level 4", "res/Levels/Level 4.png", (135, 206, 234))
Level_4.End(20, 21)
Level_4.addMob(Mob.GHOST_NPC, 13, 15)
Level_4.addPowerUp(PowerUp.LIFE_GAIN, 14, 15)
Level_5 = Level("Level 5", "res/Levels/Level 5.png", (2, 23, 33))
Level_5.End(20, 23)
Level_5.addMob(Mob.GHOST_NPC, 4, 7)
Level_5.addPowerUp(PowerUp.LIFE_GAIN, 13, 7)
Level_5.addPowerUp(PowerUp.SUPER_SPEED, 10, 14)

Level_6 = Level("Test Level 1", "res/Levels/caveTestLevel.png", (2, 23, 33))
Level_6.End(21, 20)
Level_6.addPowerUp(PowerUp.SUPER_SPEED, 13, 13)
Level_6.addPowerUp(PowerUp.LIFE_GAIN, 9, 6)
Level_6.addMob(Mob.GHOST_NPC, 4, 5)
Level_6.addMob(Mob.GHOST_NPC, 3, 3)
Level_7 = Level("Level 7", "res/Levels/Level 7.png", (2, 23, 33))
Level_7.End(20, 21)
Level_7.addMob(Mob.GHOST_NPC, 16, 3)
Level_7.addMob(Mob.GHOST_NPC, 23, 8)
Level_7.addMob(Mob.GHOST_NPC, 23, 14)
Level_7.addMob(Mob.GHOST_NPC, 23, 20)
Level_7.addPowerUp(PowerUp.SUPER_SPEED, 10, 8)
Level_7.addPowerUp(PowerUp.SUPER_SPEED, 9, 17)
Level_8 = Level("Level 8", "res/Levels/Level 8.png", (2, 23, 33))
Level_8.End(20, 21)
Level_8.addPowerUp(PowerUp.SUPER_SPEED, 23, 12)
Level_8.addPowerUp(PowerUp.LIFE_GAIN, 2, 20)
Level_8.addMob(Mob.GHOST_NPC, 2, 20)
Level_9 = Level("Level 9", "res/Levels/Level 9.png", (2, 23, 33))
Level_9.End(20, 21)
Level_9.addPowerUp(PowerUp.SUPER_SPEED, 14, 10)
Level_9.addPowerUp(PowerUp.LIFE_GAIN, 16, 8)
Level_9.addMob(Mob.GHOST_NPC, 17, 14)
Level_9.addMob(Mob.GHOST_NPC, 17, 20)
Level_10 = Level("Level 10", "res/Levels/Level 10.png", (2, 23, 33))
Level_10.End(20, 21)
Level_10.addMob(Mob.GHOST_NPC, 14, 13)
Level_10.addMob(Mob.GHOST_NPC, 23, 17)
AllLevels = [Level_1, Level_2, Level_3, Level_4, Level_5, Level_6, Level_7, Level_8, Level_9, Level_10]#List of levels

#--------------------------------------------------------------------
TestLevelCave = Level("Test Level 1", "res/Levels/caveTestLevel.png", (2, 23, 33))#021721, (2, 23, 33)

TestLevelCave.addPowerUp(PowerUp.SUPER_SPEED, 7, 6)
TestLevelCave.addPowerUp(PowerUp.SUPER_SPEED, 13, 13)
TestLevelCave.addPowerUp(PowerUp.LIFE_GAIN, 9, 6)#1 Up Test

TestLevelCave.addMob(Mob.GHOST_NPC, 4, 5)
TestLevelCave.addMob(Mob.GHOST_NPC, 3, 3)#Mob Test

TestLevelCave.End(21, 20)
#--------------------------------------------------------------------

CurrentLevel = [AllLevels[0], 1]#Level and lwvwl number
#level selector will set this to a value depending on level picked
#As its 0 will always be same level currently, but should work
