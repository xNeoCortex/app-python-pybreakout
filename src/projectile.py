import pygame
import constants

class Projectile:

    def __init__(self, screen):

        self.screen = screen

        self.positionX = 0
        self.positionY = 0

        self.velocity = 0
        self.angle = 0

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

    def draw(self):
        pygame.draw.circle(self.screen, constants.colourRed, (self.positionX, self.positionY), 10, 10)
