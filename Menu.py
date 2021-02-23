import pygame

from pygame.locals import *
from Level import *
from Files import *

class Menu:
    #DOCUMENT
     def __init__(self):
        self.Rects = []
        self.RectsPos = []
        #0 - Pre-Main, 1 - Main, 2 - Options, 3 - Level selector, 4 - Stat Menu
        self.changeMenu(0)#Pre - cahnge to 0

        self.currentLevel = None#Sought out later
        self.state = 0#0 - Menu(Normal/Defualt), 1 - Start, 2 - Exit

        self.background = load("res/Menu/MenuBackground.jpg", "Background")
        #Get load procdure from Level

     def changeMenu(self, menu):
          #changed so self.currentMenu keeps track of menu
          #but procdure handles changing menu by itself
          #Not sure if bother documenting
          self.currentMenu = menu
          self.MenuOptionsFont = pygame.font.SysFont("ardestineopentype", 120)
          if menu == 0:
            self.MenuOptionsFont = pygame.font.SysFont("ardestineopentype", 60)
            self.PreMenu()
          elif menu == 1:
            self.MenuOptionsFont = pygame.font.SysFont("ardestineopentype", 60)
            self.MainMenu()
          elif menu == 2:
            self.OptionMenu()
          elif menu == 3:
            self.LevelSelector()
          elif menu == 4:
            self.StatsMenu()

     def LevelSelector(self):
        LevelLabel = self.MenuOptionsFont.render("Level!", 1, (0, 0, 0))
        LevelPos = (320, 50)

        #Level Boxs
        self.box = load("res/Menu/boxEmpty.png", "box")#Possibly Temp
        self.box2 = load("res/Menu/boxEmpty2.png", "box 2")#Poswsibly Temp

        #If document, document self.box.copy()
        self.Rects = [LevelLabel]
        self.RectsPos = [LevelPos]
        self.AltBoxes = []#for when mouse over box, more efficent than alt way

        xPos = 95
        yPos = 200

        Level = savefile.Load("Level")
        if Level == -1:
            Level = len(AllLevels)
        Level+=1
        for i in range(1, Level):
             box = self.box.copy()
             box2 = self.box2.copy()
             if i < 10:
                  numImg = pygame.transform.scale(load("res/Menu/hud_%s.png" %(i), "Level %s num"%(i)), (40, 40))
                  box.blit(numImg, (15, 15))

                  box2.blit(numImg, (15, 15))
             elif i >= 10 and i < 22:
                  Digit1Img = pygame.transform.scale(load("res/Menu/hud_%s.png" %(str(i)[0]), "Level %s num"%(str(i)[0])), (30, 40))
                  Digit2Img = pygame.transform.scale(load("res/Menu/hud_%s.png" %(str(i)[1]), "Level %s num"%(str(i)[1])), (30, 40))
                  box.blit(Digit1Img, (5, 15))
                  box.blit(Digit2Img, (35, 15))

                  box2.blit(Digit1Img, (5, 15))
                  box2.blit(Digit2Img, (35, 15))
             else:
                  #if i > than 21 no more level buttons
                  #max of 21 buttons fit on level selector
                  break

             #the load assumes levels only 0 - 9
             self.Rects.append(box)
             self.RectsPos.append((xPos, yPos))
             self.AltBoxes.append(box2)

             xPos+=110
             if xPos > 756:
                  #max 755
                  xPos = 95
                  yPos += 110
                  #assumes levels wont go o to go off display

        BackMsglbl = pygame.font.SysFont("ardestineopentype", 20).render("Backspace to return to main menu", 1, (0, 0, 0))
        BackMsglblPos = (290, 20)
        self.Rects.append(BackMsglbl)
        self.RectsPos.append(BackMsglblPos)

     def PreMenu(self):
          #Pre Menu
          #Might get rid of
          self.alpha = 255
          PressEnterText = self.MenuOptionsFont.render("[Press Enter]", 1, (79, 255, 20))
          PressEnterLabel = pygame.Surface((390, 75))
          PressEnterLabel.fill((0, 205, 33))
          PressEnterLabel.blit(PressEnterText, (0, 0))
          PressEnterLabel.set_colorkey((0, 205, 33))
          PressEnterPos = (280, 215)
          alpha = 255

          self.Rects = [PressEnterLabel]
          self.RectsPos = [PressEnterPos]

     def MainMenu(self):
          #Main Menu
          PlayLb = self.MenuOptionsFont.render("Play!", 1, (38, 38, 38))
          PlayLbPos = (100, 100)
          OptionsLb = self.MenuOptionsFont.render("Options!", 1, (38, 38, 38))
          OptionsLbPos = (100, 200)
          StatsLb = self.MenuOptionsFont.render("Stats!", 1, (38, 38, 38))
          StatsLbPos = (100, 300)
          ExitLb = self.MenuOptionsFont.render("Exit!", 1, (38, 38, 38))
          ExitLbPos = (100, 400)

          #render
          self.Rects = [PlayLb, OptionsLb, StatsLb, ExitLb]
          self.RectsPos = [PlayLbPos, OptionsLbPos, StatsLbPos, ExitLbPos]

     def OptionMenu(self):
          #Options Menu
          OptionsLabel = self.MenuOptionsFont.render("Controls!", 1, (0, 0, 0))
          OptionsPos = (240, 50)

          keySetBox = pygame.Surface((835,238))
          keySetBoxPos = (33, 297)

          #Need to retirve several times cause when set vaiable think ressting name
          KeyFont = pygame.font.SysFont("papyrus", 20)
          LeftKey = load("res/Menu/key.png", "Key Image")
          LeftKey.blit(KeyFont.render("A", 1, (0, 0, 0)), (5,0))
          RightKey = load("res/Menu/key.png", "Key Image")
          RightKey.blit(KeyFont.render("D", 1, (0, 0, 0)), (5,0))
          JumpKey = load("res/Menu/key.png", "Key Image")
          JumpKey.blit(KeyFont.render('W', 1, (0, 0, 0)), (5,0))
          #SpecialKey = load("res/key.png", "Key Image")
          #SpecialKey.blit(KeyFont.render("L", 1, (0, 0, 0)), (5,0))

          PauseKey = load("res/Menu/key.png", "Key Image")
          PauseKey.blit(KeyFont.render("P", 1, (0, 0, 0)), (5,0))
          MuteKey = load("res/Menu/key.png", "Key Image")
          MuteKey.blit(KeyFont.render("M", 1, (0, 0, 0)), (5,0))

          keySetBox.blit(KeyFont.render("Alt key:", 1, (255, 255, 255)), (25, 185))
          keySetBox.blit(KeyFont.render("Right          Left", 1, (255, 255, 255)), (140, 185))
          keySetBox.blit(KeyFont.render("(arrow key)", 1, (255, 255, 255)), (150, 210))
          keySetBox.blit(KeyFont.render("Spacebar", 1, (255, 255, 255)), (430, 185))

          keySetBox.blit(LeftKey, (147, 147))
          keySetBox.blit(RightKey, (231,147))
          keySetBox.blit(KeyFont.render("Movement", 1, (255, 255, 255)), (155, 10))#Movement Label
          keySetBox.blit(load("res/PlayerSprites/walk1.png", "Player Walk img"), (175, 80))

          keySetBox.blit(JumpKey, (457, 147))
          keySetBox.blit(KeyFont.render("Jump", 1, (255, 255, 255)), (445, 10))#Jump Label
          keySetBox.blit(load("res/PlayerSprites/jump.png", "Player Jump img"), (450, 45))

          keySetBox.blit(PauseKey, (625, 143))
          keySetBox.blit(KeyFont.render("~ Pause", 1, (255, 255, 255)), (667, 145))#Pause Label

          #render
          self.Rects = [OptionsLabel, keySetBox]
          self.RectsPos = [OptionsPos, keySetBoxPos]

          BackMsglbl = pygame.font.SysFont("ardestineopentype", 20).render("Backspace to return to main menu", 1, (0, 0, 0))
          BackMsglblPos = (290, 20)
          self.Rects.append(BackMsglbl)
          self.RectsPos.append(BackMsglblPos)

     def StatsMenu(self):
        StatsLbl = self.MenuOptionsFont.render("Stats!", 1, (0, 0, 0))
        StatsLblPos = (270, 50)

        Deaths = savefile.Load("Deaths")
        lives = savefile.Load("Lives")
        Levels = savefile.Load("Level")
        Progress = str(int((Levels-1)/len(AllLevels) * 100)) + "%"
        if Levels == -1:
            Levels = len(AllLevels)
            Progress = "100%"

        StatsBox = pygame.Surface((400, 350))

        StatsFont = pygame.font.SysFont("gabriola ", 40)
        StatsBox.blit(StatsFont.render("Lives Left: " + str(lives), 1, (255, 255, 255)), (20, 30))
        StatsBox.blit(StatsFont.render("Current Level: " + str(Levels), 1, (255, 255, 255)), (20, 110))
        StatsBox.blit(StatsFont.render("Total Progress: " + Progress, 1, (255, 255, 255)), (20, 190))
        StatsBox.blit(StatsFont.render("Total Deaths: " + str(Deaths), 1, (255, 255, 255)), (20, 270))

        StatsBoxPos = (230, 170)


        self.Rects = [StatsLbl, StatsBox]
        self.RectsPos = [StatsLblPos, StatsBoxPos]

        BackMsglbl = pygame.font.SysFont("ardestineopentype", 20).render("Backspace to return to main menu", 1, (0, 0, 0))
        BackMsglblPos = (290, 20)
        self.Rects.append(BackMsglbl)
        self.RectsPos.append(BackMsglblPos)

     def Events(self, event):
          if (event.type == pygame.KEYDOWN):
            if (event.key == K_RETURN):
                 #Enter Key
                if self.currentMenu == 0:#Pre
                    #Go to Main Menu
                    self.changeMenu(1)#Main
            if (event.key == K_BACKSPACE):
                #go back from stats and options
                if self.currentMenu == 2 or self.currentMenu == 3 or self.currentMenu == 4:
                     #Options, Selector or Stats
                    self.changeMenu(1)#Main


     def update(self, buttonpressed):
        pos = pygame.mouse.get_pos()
        #pos[x, y] - postion of mouse

        self.state = 0

        if self.currentMenu == 0:#Pre
            self.Rects[0].set_alpha(abs(self.alpha))
            self.alpha -= 5
            if self.alpha <= -255:
                self.alpha = 255

        elif self.currentMenu == 1:#Main
            #Maybe Temp
            self.Rects[0] = self.MenuOptionsFont.render("Play!", 1, (38, 38, 38))
            self.Rects[1] = self.MenuOptionsFont.render("Controls!", 1, (38, 38, 38))
            self.Rects[2] = self.MenuOptionsFont.render("Stats!", 1, (38, 38, 38))
            self.Rects[3] = self.MenuOptionsFont.render("Exit!", 1, (38, 38, 38))

            if(pos[0] > self.RectsPos[0][0] and pos[0] < self.RectsPos[0][0] + 130):
                if (pos[1] > self.RectsPos[0][1] and pos[1] < self.RectsPos[0][1] + 70):
                    #Play Button/Label
                    #Goes to Level Selector
                    self.Rects[0] = self.MenuOptionsFont.render("Play!", 1, (179, 179, 179))
                    if buttonpressed:
                        self.changeMenu(3)#Level Selector
                        return


            if (pos[0] > self.RectsPos[1][0] and pos[0] < self.RectsPos[1][0] + 220):
                if (pos[1] > self.RectsPos[1][1] and pos[1] < self.RectsPos[1][1] + 70):
                    #Option Button/Label
                    #Goes to Options Menu
                    self.Rects[1]= OptionsLb = self.MenuOptionsFont.render("Controls!", 1, (179, 179, 179))
                    if buttonpressed:
                        self.changeMenu(2)#Options
                        return

            if (pos[0] > self.RectsPos[2][0] and pos[0] < self.RectsPos[2][0] + 165):
                if (pos[1] > self.RectsPos[2][1] and pos[1] < self.RectsPos[2][1] + 70):
                    #Stats Button/Label
                    #Stas
                    self.Rects[2] = self.MenuOptionsFont.render("Stats!", 1, (179, 179, 179))
                    if buttonpressed:
                         self.changeMenu(4)#Stats
                         return

            if (pos[0] > self.RectsPos[3][0] and pos[0] < self.RectsPos[3][0] + 130):
                if (pos[1] > self.RectsPos[3][1] and pos[1] < self.RectsPos[3][1] + 55):
                    #Exit Button/Label
                    #Exit - break out of while loop
                    self.Rects[3] = self.MenuOptionsFont.render("Exit!", 1, (179, 179, 179))
                    if buttonpressed:
                        self.state = 2
                        return

        elif self.currentMenu == 3:#Level Selector
            #Need someway to return level choosen

            self.LevelSelector()#Also Document

            if len(self.Rects) > 1:
                 #to make sure theres actully buttons
                 for i in range(1, len(self.Rects)-1):
                      if((pos[0] > self.RectsPos[i][0]) and (pos[0] < (self.RectsPos[i][0] + 70))):
                          if ((pos[1] > self.RectsPos[i][1]) and (pos[1] < (self.RectsPos[i][1] + 70))):
                              #Level i Button
                              #Goes to Level i
                              self.Rects[i] = self.AltBoxes[i-1]
                              if buttonpressed:
                                   CurrentLevel[0] = AllLevels[i-1]#sets level
                                   CurrentLevel[1] = i
                                   self.state = 1
                                   return

     def getState(self):
        #Might change to return state so can change to game when needed
        return self.state

     def render(self, window):
        window.blit(self.background, (0, 0))#Background
        for i in range(len(self.Rects)):
            window.blit(self.Rects[i], self.RectsPos[i])
