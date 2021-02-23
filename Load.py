import pygame
import sys

def load(path, name):
    try:
        image = pygame.image.load(path)
        return image
    except pygame.error:
        #print(name, "Image Load Error")
        return None
