from Entity import *

class Mob(Entity):
    GHOST_NPC = 0
    
    MOB_SPEED = 2
    def __init__(self, name, SpriteSheet, size, x, y):
        super().__init__(name, SpriteSheet, size)
        
        self.image1 = self.generateSprite(x, y)
        self.image2 = self.generateSprite(x+1, y)
        
        self.MobSize = size
        self.xMovement, self.yMovement = 0, 0#distance mob moved from intial pos
        self.initialx, self.initialy = 0, 0
        self.Dir = -1

    def __Move(self, Dir):
        if Dir == -1:
            #left
            self.xMovement -= Mob.MOB_SPEED
        if Dir == 1:
            #right
            self.xMovement += Mob.MOB_SPEED

    def getXMov(self):
        return (self.initialx + self.xMovement)

    def getYMov(self):
        return (self.initialy + self.yMovement)

    def getSize(self):
        return self.MobSize

    def setPos(self, x, y):
        #start pos of mob
        self.initialx = x
        self.initialy = y

    def Collsion(self, BlockList, Dir):
        collsion = False
        newx = self.initialx + self.xMovement
        newy = self.initialy + self.yMovement
        if Dir > 0:
            #moving right
            newx += self.MobSize#right side of sprite
        #else moving left newX == newX
        blockx = int(newx/self.MobSize)
        blocky = int(newy/self.MobSize)

        try:
            block = BlockList[blockx][blocky]
            if block != None:
                if block.getCollsion() == 1: 
                    collsion = True
                if block.getCollsion() == 2:
                    #Die
                    pass
                            
        except IndexError:
            #Die
            pass
        return collsion

    def update(self, blockList, tick):
        #Document
        if (tick >= 0 and tick < 15) or (tick >= 30 and tick < 45):
            self.image = self.image1
        if (tick >=15  and tick < 30) or (tick >= 45 and tick < 60):
            self.image = self.image2
            
        if not self.Collsion(blockList, self.Dir):
            self.__Move(self.Dir)#self.Dir)
        else:
            self.Dir = -self.Dir
            self.image1 = pygame.transform.flip(self.image1, True, False)
            self.image2 = pygame.transform.flip(self.image2, True, False)
            
            #self.image = pygame.transform.flip(self.image, True, False)
            #Each time direction changes flip image 

class GhostNPC(Mob):
    #This is as the x & y postion are needed for collsion and my normal way of doing only has
    #one instance cant have mutiple of the same mob on the same level
    def __init__(self, size):
        super().__init__("Ghost NPC", GhostNPCSpriteSheet, size, 0, 0)
    
