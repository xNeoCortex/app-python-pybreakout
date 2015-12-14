import pygame
import constants

class Brick:

    def __init__(self, screen):
        self.__brickPosX = 0
        self.__brickPosY = 0
        self.screen = screen

        self.__brickSizeX = 66
        self.__brickSizeY = 18

        self.colourArr = [constants.colourRed,constants.colourPink,constants.colourOrange,constants.colourGreen,constants.colourYellow]

    def setPosX(self, x):
        self.__brickPosX = x

    def setPosY(self, y):
        self.__brickPosY = y

    def getPosX(self):
        return self.__brickPosX

    def getPosY(self):
        return self.__brickPosY

    def getPosition(self):
        return (self.__brickPosX, self.__brickPosY)

    def draw(self,c):
        pygame.draw.rect(self.screen, self.colourArr[c], [self.__brickPosX, self.__brickPosY,self.__brickSizeX,self.__brickSizeY])
