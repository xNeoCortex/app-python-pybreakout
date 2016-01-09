import pygame
import constants

class Bat:

    def __init__(self, screen):
        self.positionX = 500
        self.positionY = 650

        self.sizeX = 85
        self.sizey = 15

        self.screen = screen

    def setPosX(self, x):
        self.positionX = x

    def getPosX(self):
        return self.positionX

    def getPosY(self):
        return self.positionY

    def draw(self):
        pygame.draw.rect(self.screen, constants.foregroundColour, [self.positionX, self.positionY,self.sizeX,self.sizey])

class Projectile:

    def __init__(self, screen):

        self.screen = screen

        self.positionX = 0
        self.positionY = 0

        self.velocity = 10
        self.angle = 0

    def setPosX(self, x):
        self.positionX = x
    def setPosY(self, y):
        self.positionY = y
    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y
    def getPosX(self):
        return self.positionX
    def getPosY(self):
        return self.positionY
    def getPosition(self):
        return (self.positionX, self.positionY)

    def draw(self):
        pygame.draw.circle(self.screen, constants.colourRed, (self.positionX, self.positionY), 5, 0)

    def move(self):
        self.positionY = self.positionY - self.velocity

    
