import pygame
import sys

from pygame.locals import *

#from Tile import *
from Level import *
from Player import *

from Files import *
from Menu import *

pygame.init()
pygame.mixer.init()

#Display
WIDTH = 900
HEIGHT = 550

Window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer: Developer stage")

#Sound
Mute = False

#File
#If new Game or just missing
if  savefile.Load("Lives") == None:
    savefile.Save("Lives", Player.MAX_LIVES)
if not savefile.Load("Level"):
    #if None(not there)
    savefile.Save("Level", 1)
if savefile.Load("Deaths") == None:
    #new game/player
    savefile.Save("Deaths", 0)
UnlockedLevelNum = savefile.Load("Level")
gameOver = 0
#0 - no game over, 1 - game over you lost all lives, 2 - game over you won

#Game state
Menus = Menu()
#lives lost overall, all power ups obtained

Pausedlbl = pygame.font.SysFont("ardestineopentype", 120).render("Paused!", 1, (0, 255, 0))
BackMsglbl = pygame.font.SysFont("ardestineopentype", 20).render("Backspace to return", 1, (0, 255, 0))
QuitMsglbl = pygame.font.SysFont("ardestineopentype", 20).render("Q to Quit", 1, (0, 255, 0))
PauseControls = pygame.font.SysFont("ardestineopentype", 20).render("Controls: A/Left arrow key - Left, W/Spacebar - jump, D/Right arrow key - Right", 1, (0, 255, 0))
PauselblPos = (250, 200)
BackMsglblPos = (360, 350)
QuitMsglblPos = (410, 390)

#0 - Menu, 1 - Game, 2 - Pause (if implemented)
#way to say whether Menu(Pre Game), The Game or paused etc.
gameState = 0#change back to 0
MainPlayer = Player(3, -1, ((WIDTH-Tile.TILESIZE)/2), ((HEIGHT-Tile.TILESIZE)/2), Tile.TILESIZE)
#1 & player def to skip menu

#Colours
black = (0,0,0)
skyblue = (135, 206, 235)
red = (255, 0, 0)

keys = []#All keys pressed might cap a length
def GameEvent(event):
    #Player
    MainPlayer.keyDown(event)
    MainPlayer.keyUp(event)

#Game Loop
running = True
tick = 0
secs = 0
clock=pygame.time.Clock()
while running:
    buttonpressed = False
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

        if (event.type == pygame.MOUSEBUTTONUP):
            buttonpressed = True
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_m):
            #Mute
            if not Mute:
                pygame.mixer.pause()
                Mute = True
            else:
                pygame.mixer.unpause()
                Mute = False
                #Mute promblems with sfx

        #If Menu or Game or Pause
        if gameState == 0:
            Menus.Events(event)
        elif gameState == 1:
            GameEvent(event)
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_p):
                    gameState = 2
        elif gameState == 2:
            #Pause menu events(button or backspace)
            MainPlayer.keyUp(event)
            if (event.type == pygame.KEYDOWN):
                if (event.key == K_BACKSPACE):
                    if gameOver == 1 or gameOver == 2:  
                        gameState = 0
                        gameOver = 0
                    else:
                        gameState = 1
                    #PauselblPos = (250, 200)
                    Pausedlbl = pygame.font.SysFont("ardestineopentype", 120).render("Paused!", 1, (0, 255, 0))
                if (event.key == K_q):
                    #Q only when paused
                    running = False

    if gameState == 0:
        #Update
        Menus.update(buttonpressed)
        #if chnage to stste return number reprsenting state
        #0 - defualt aka menu
        #1 - Change to game
        #2 - Exit
        MenuOptions = Menus.getState()
        if MenuOptions == 1:
            #start game

            MainPlayer = Player(3, 0, ((WIDTH-Tile.TILESIZE)/2), ((HEIGHT-Tile.TILESIZE)/2), Tile.TILESIZE)#cahnges each time menu changed

            gameState = 1#Change to game

        elif MenuOptions == 2:
            running = False

        #Render
        Menus.render(Window)

    elif gameState == 1:
        #If game being played
        #Update
        CurrentLevel[0].update(tick)
        MainPlayer.update(CurrentLevel[0], tick)
        xOffset, yOffset = MainPlayer.getOffset()

        #Render
        Window.fill(black)#set background colour
        CurrentLevel[0].render(Window, xOffset, yOffset)#Level Render
        MainPlayer.render(Window)#Player Render

        #something to take back to Level Selector
        if MainPlayer.EndReached() == 1:
            CurrentLevel[0].Reset()
            gameState = 0
            #Next Level unlocked
            #when level finished unlock next level, save fact that next level unlocked


            if CurrentLevel[1] == UnlockedLevelNum:
                if UnlockedLevelNum < len(AllLevels) :
                    UnlockedLevelNum+=1
                    savefile.Save("Level", UnlockedLevelNum)
                    #Can now access CurrentLevelNum lEVEL FROM selector
                    #can be done by accessing UnlockedLevelNum from Menu class in level selector

                elif UnlockedLevelNum == len(AllLevels):
                    if UnlockedLevelNum != -1:
                        #if this isnt your first time completing the final level
                        #You Win
                        print("You win")
                        Window.fill((255, 255, 0))
                        Pausedlbl = pygame.font.SysFont("ardestineopentype", 120).render("Victory!", 1, (0, 0, 0)) 
                        gameOver = 2
                        gameState = 2
                    UnlockedLevelNum = -1#This means game complete
                    savefile.Save("Level", UnlockedLevelNum)

        elif MainPlayer.EndReached() == 2:
            CurrentLevel[0].Reset()

            UnlockedLevelNum = 1#This means game complete
            savefile.Save("Level", UnlockedLevelNum)
            savefile.Save("Lives", Player.MAX_LIVES)
            gameState = 2#Menu, Level Selector speciffically
            Pausedlbl = pygame.font.SysFont("ardestineopentype", 120).render("Game Over!", 1, (255, 0, 0))
            PauselblPos = (150, 200)
            Window.fill((0, 0, 0))
            gameOver = 1


    elif gameState == 2:
        #Pause render & update
        Window.blit(Pausedlbl, PauselblPos)
        Window.blit(BackMsglbl, BackMsglblPos)
        Window.blit(QuitMsglbl, QuitMsglblPos)

        if gameOver == 0:
            Window.blit(PauseControls, (40, 430))

    tick +=1
    if tick > 60:
        secs += 1
        tick = 0
    clock.tick(60)
    pygame.display.update()
pygame.quit()
