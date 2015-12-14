import pygame
import constants

class Bat:

    def __init__(self, screen):
        self.__batPosX = 500
        self.__batPosY = 650

        self.__batSizeX = 85
        self.__batSizeY = 15

        self.screen = screen

    def setPosX(self, x):
        self.__batPosX = x

    def getPosX(self):
        return self.__batPosX

    def draw(self):
        pygame.draw.rect(self.screen, constants.foregroundColour, [self.__batPosX, self.__batPosY,self.__batSizeX,self.__batSizeY])
