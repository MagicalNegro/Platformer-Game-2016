import pygame

class SoundFX():
    #Call instance of class for each sound FX then call when needed
    def __init__(self, FileName):
        self.__sound = pygame.mixer.Sound(FileName)

    def play(self, loops=0):
        #loop: 0 - 1 time (0 times repeated)
        self.__sound.play(loops)

    def setVolume(pcent):
        vol = pcent / 100
        self.__sound = set_volume(vol)

    def getVolume(self):
        volStr = str(int(self.__sound.get_volume() * 100)) + "%"
        return volStr

    def getLength(self):
        soulen = str(self.__sound.get_length()) + " seconds"
        return soulen

#List of Sounds
pygame.mixer.init()#cause these called before pygam init()
DeathSFX = SoundFX("res/Audio/laser.wav")
PowerUpSFX = SoundFX("res/Audio/pickup.wav")


