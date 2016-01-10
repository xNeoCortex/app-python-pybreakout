import pygame
import constants

class Brick:

    def __init__(self, screen):
        self.positionX = 0
        self.positionY = 0
        self.screen = screen

        self.sizeX = 66
        self.sizeY = 18

        self.colourArr = [constants.colourRed,constants.colourPink,constants.colourOrange,constants.colourGreen,constants.colourYellow,constants.colourSpecial]

#Positioning
    def setPosX(self, x):
        self.positionX = x
    def setPosY(self, y):
        self.positionY = y
    def getPosX(self):
        return self.positionX
    def getPosY(self):
        return self.positionY
    def getPosition(self):
        return (self.positionX, self.positionY)
#/End Positioning

    def draw(self,c):
        pygame.draw.rect(self.screen, self.colourArr[c], [self.positionX, self.positionY,self.sizeX,self.sizeY])
