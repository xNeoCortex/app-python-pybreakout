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

        self.time = 0

        #angle controller to me moved to a function
        self.angle = 90
        self.gradient = 1

    def setPosX(self, x):
        self.positionX = x
    def setPosY(self, y):
        self.positionY = y
    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y
    def setAngle(self, a):
        self.angle = int(a)
    def getPosX(self):
        return self.positionX
    def getPosY(self):
        return self.positionY
    def getPosition(self):
        return (self.positionX, self.positionY)
    def reflect(self):
        self.angle = self.angle + 180
        if self.angle > 360:
            self.angle = self.angle - 360
    def reflectGrad(self):
        self.gradient = (self.gradient * -1)
    def setGrad(self, g):
        self.gradient = g

    def draw(self):
        pygame.draw.circle(self.screen, constants.colourRed, (self.positionX, self.positionY), 5, 0)

    def move(self):
        self.time += 1
        self.velocity = 10 * math.sin(self.time / 10.0)

        if self.angle >= 180:
            self.velocity = self.velocity = -10
        elif self.angle <= 180:
            self.velocity = self.velocity = 10

        x = self.positionX + (self.velocity * self.gradient)

        y = self.positionY - self.velocity

        self.setPosition(int(x), int(y))
