import pygame

from Sprite import *
from Audio import *
from Files import *
from Entity import * #for power up types

class Player:
    MAX_V = 13
    MAX_movX = 5
    SSMAX_movX = 10

    MAX_LIVES = 5
    def __init__(self, initalx, initaly, screenx, screeny, tilesize):
        self.x = initalx * tilesize
        self.y = initaly * tilesize
        self.intial = (self.x, self.y)
        self.screenx = screenx
        self.screeny = screeny
        self.TileSize = tilesize

        self.xOffset, self.yOffset = self.x - screenx, self.y-screeny

        self.lives = savefile.Load("Lives")

        #Sprite
        self.SpriteSet = Standing#Default
        self.Sprite = self.SpriteSet[0]
        self.Dir = -1#Possibly temp: -1 left, 1 right
        size = Walk1.getSize()
        self.PlayerWalkingHeight = size[0]
        self.PlayerWalkingWidth = size[1]

        #keep track of time
        self.counter = 0
        self.Xspeed = Player.MAX_movX

        #For End of Level
        self.End = 0
        #0 - Nothing
        #1 - completed
        #2 - lost all lives

        #keys/movement
        self.keyPressed = []#all keys pressed at once (because mutiple keys can be pressed at once and previosu sprite promblems i was having)
        self.movX = 0#X
        #Y collsion + Jump*****************
        self.velocity = 0#Y
        self.falling = False#Y
        self.onground = False#Y

        #HUD
        self.HeartImg = pygame.transform.scale(load("res/HUD/Hearts.png", "Life Heart"), (32, 32))


    def keyDown(self, event):
        if (event.type == pygame.KEYDOWN):
            #Right - A, Left - D, Down - S or Up - W
            #Change later so key set can be changed
            if(event.key==pygame.K_a or event.key==pygame.K_LEFT or event.key==pygame.K_d or event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN or event.key==pygame.K_w or event.key==pygame.K_SPACE):
                self.keyPressed.append(pygame.key.name(event.key))
                #print(self.keyPressed)
                #print(pygame.key.name(event.key))
                self.Move()

    def keyUp(self, event):
        if (event.type == pygame.KEYUP):
           if(event.key==pygame.K_a or event.key==pygame.K_LEFT or event.key==pygame.K_d or event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN or event.key==pygame.K_w or event.key==pygame.K_SPACE):
                try:
                    self.keyPressed.remove(pygame.key.name(event.key))
                except ValueError:
                    pass
                self.Move()

    def Move(self):
        #This change means this codes only run when its needed making it more efficent
        if  self.keyPressed:
            #for loop cause of keys pressed that arent the right left or up keys
            for key in reversed(self.keyPressed):
                #Change later so key set can be changed
                #W/Up - Jump, D/Right - Right, A.Left - left
                #Can tell direction by using self.movX
                if key == "right" or key == "d":
                    #going right
                    self.movX = self.Xspeed
                    self.Dir = 1#PossiblyTemp
                    self.SpriteSet = Walking
                    break
                if key == "left" or key == "a":
                    #going left
                    self.movX = -self.Xspeed
                    self.Dir = -1
                    self.SpriteSet = Walking
                    break
                if key == "up" or key == "w" or key == "space":
                    #Jump (cant implement without y collsion)
                    self.__Jump()

                if key == "down":
                    #Allows me to see stuff developr tool
                    pass
        else:
            #Not moving
            self.movX = 0
            self.SpriteSet = Standing

    def __Jump(self):
        #Y collsion + Jump*****************
        if not self.onground:
            return
        #JumpingSFX.play()
        self.velocity = Player.MAX_V
        self.onground = False

    def PowerUp(self, item, level):
        #To make it easier cant have 2 powerups at the same time
        #might have to change for checkpoints and lives etc
        self.BacktoNormal()
        #find better way to define and get effect
        #Speed
        PUtype = item[0]
        if PUtype == PowerUp.SUPER_SPEED:
            #increased speed for 5 secs
            level.PowerUpCollection.remove(item)
            PowerUpSFX.play()
            self.Xspeed = Player.SSMAX_movX
        elif PUtype == PowerUp.LIFE_GAIN:
            #1 Up
            level.PowerUpCollection.remove(item)
            PowerUpSFX.play()
            self.__Lives(False)

        elif PUtype == PowerUp.END:
            self.End = 1

    def __Lives(self, lost):
        #lost = True - live lost, False -gained
        if lost:

            if self.lives > 0:
                self.lives-=1
                Deaths = savefile.Load("Deaths")
                Deaths += 1
                savefile.Save("Deaths", Deaths)
            else:
                #all lives lost
                self.End = 2
                #set lives back to defualt and level back to 1
                #Return Player to Level Selector
                #Or if cant think of anything just leave it or work out something simpler
        else:
            if self.lives < Player.MAX_LIVES:
                self.lives += 1
        savefile.Save("Lives", self.lives)



    def EndReached(self):
        return self.End

    def BacktoNormal(self):
        #gets rid of power Ups
        self.Xspeed = Player.MAX_movX
        self.counter = 0

    def __Die(self):
        DeathSFX.play()
        #pygame.event.wait() - bascially pause
        self.__Lives(True)
        self.BacktoNormal()
        self.velocity = 0
        self.falling = False
        self.onground = False
        self.x, self.y = self.intial

    def Xcollsion(self, level):
        collsion = False
        #if self.x += self.movX = collsion collsion = True
        xPosL = self.x + self.movX
        xPosR = xPosL + (self.PlayerWalkingWidth-5)
        #newy = self.y
        if self.movX > 0:
            #moving right
            newx = xPosR#moving right
            xPosR -= 15
        else:
            newx = xPosL#moving left
            xPosL += 20
        blockx = int(newx/self.TileSize)
        blocky = int(self.y/self.TileSize)

        blocklist = level.getBlockList()
        try:
            block = blocklist[blockx][blocky]
            if block != None:
                if block.getCollsion() == 1: #or blocklist[blockX][blockY+1].getCollsion() == 1:
                    #changed when considering different types of collsions
                    collsion = True
                if block.getCollsion() == 2:
                    self.__Die()

            if level.PowerUpCollection:
                #check if list empty
                #redo in 'neater' way so ot using Levels variable directly
                for item in level.PowerUpCollection:
                    if blockx == item[1] and blocky == item[2]:
                        self.PowerUp(item, level)

            if level.MobCollection:
                #check if list empty
                for mob in level.MobCollection:
                    if (xPosL >= mob.getXMov() and xPosL < mob.getXMov() + mob.getSize()) or  (xPosR >= mob.getXMov() and xPosR < mob.getXMov() + mob.getSize()) :
                        if self.y >= mob.getYMov() and self.y < mob.getYMov() + mob.getSize():
                            self.__Die()

        except IndexError:
            self.__Die()
        return collsion

    def Ycollsion(self, level):
        #Might change collsion so when collsion sets postio next to tile due to promblems

        #Might change again to make more efficent so power up on blocklist
        #and collsion detection just uses blocklist
        #also possibly get rid of passable blocks and just set the background colour
        #also possibly if movement happens only so often instaed of every loop might be more efficent

        #Y collsion + Jump*******************
        collsion = False
        yPosT = self.y - self.velocity
        yPosB = yPosT + self.PlayerWalkingHeight
        #newx = self.x
        if self.velocity <= 0:
            #falling
            newy = yPosB
        else:
            #rising
            newy = yPosT
        blockx = int((self.x+20)/self.TileSize)
        blockx2 = int((self.x+self.PlayerWalkingWidth-20)/self.TileSize)#part of solution
        blocky = int(newy/self.TileSize)

        blocklist = level.getBlockList()
        try:
            block = blocklist[blockx][blocky]
            block2 = blocklist[blockx2][blocky]#part of solution
            if block != None:
                if block.getCollsion() == 1:
                    #changed when considering different types of collsions
                    collsion = True
                else:
                    #solution
                    if block2 != None:
                        if block2.getCollsion() == 1:
                            collsion = True
                if block.getCollsion() == 2:
                    self.__Die()

            if level.PowerUpCollection:
                #check if list empty
                #redo in 'neater' way so ot using Levels variable directly
                for item in level.PowerUpCollection:
                    if blockx == item[1] and blocky == item[2]:
                        self.PowerUp(item, level)

            if level.MobCollection:
                #check if list empty
                for mob in level.MobCollection:
                    yPosT += 5
                    if (yPosT >= mob.getYMov() and yPosT < mob.getYMov() + mob.getSize()) or  (yPosB >= mob.getYMov() and yPosB < mob.getYMov() + mob.getSize()) :
                        if (self.x+31) >= mob.getXMov() and (self.x+31) < mob.getXMov() + mob.getSize():
                            self.__Die()

        except IndexError:
            self.__Die()
        return collsion

    def update(self, level, tick):
        if(self.velocity < 0):
            #Y collsion + Jump***********
            self.falling=True

        #*
        #Sprite animation
        if tick == 60:
            #PowerUp
            if self.counter < 5 and self.Xspeed == Player.SSMAX_movX:
                #Speed
                self.counter+=1
            elif self.counter >= 5 and self.Xspeed == Player.SSMAX_movX:
                self.BacktoNormal()


            #print("1 sec")
            #print(self.Sprite)
        #May need to change how works
        if self.onground:#Jumping is only one sprite
            if tick <= 15:
                self.Sprite = self.SpriteSet[0]
            elif tick > 15 and tick<= 30:
                self.Sprite = self.SpriteSet[1]
            elif tick > 30 and tick<= 45:
                self.Sprite = self.SpriteSet[2]
            elif tick > 45 and tick<= 60:
                self.Sprite = self.SpriteSet[3]
        else:
            self.Sprite = JumpSprite

        #Xmovement
        if not self.Xcollsion(level):
            self.x += self.movX

        #Y collsion + Jump*****************
        #need to work out collsion for both up and down
            #if collsion will travelling up velocity = 0 and starts decreasing
            #if collsion while travelling down velocity just = 0 (onground = true)
        if self.Ycollsion(level):
            self.velocity = 0
            if self.falling:
                self.falling = False
            else:
                blocky = int((self.y-self.velocity)/self.TileSize)
                self.y = blocky * self.TileSize
            self.onground = True
        else:
            self.onground = False
            self.velocity -= 0.5
        self.y -= self.velocity

    def getOffset(self):
        return (self.x - self.screenx), (self.y - self.screeny)

    def render(self, window):
        image = self.Sprite.Sprite()
        if self.Dir == 1:
            image = pygame.transform.flip(image, True, False)
        window.blit(image, (self.screenx, self.screeny))

        #HUD
        HUDFont = pygame.font.SysFont("ardestineopentype", 20)
        """
        HUDClock = pygame.font.SysFont("ardestineopentype", 50).render("00:00", 1, (0, 0, 255))
        HUDClockPos = (400, 0)"""

        #Lives
        HUDLives = pygame.Surface((32*5, 32))
        HUDLives.fill((0, 205, 33))
        for i in range(self.lives):
            HUDLives.blit(self.HeartImg, (32*i, 2))
        HUDLives.set_colorkey((0, 205, 33))
        window.blit(HUDLives, (5, 5))
        #Power Up
        if self.Xspeed == Player.SSMAX_movX:
            #so only when power up in use
            #get rid of later
            HUDTimerPU = pygame.font.SysFont("ardestineopentype", 120).render(str(5-self.counter), 1, (255, 0, 0))
            HUDTimerPUPos = (425, 20)
            window.blit(HUDTimerPU, HUDTimerPUPos)
        """window.blit(HUDLives, HUDLivesPos)
        window.blit(HUDClock, HUDClockPos)"""
