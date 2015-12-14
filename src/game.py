#Requirements
import sys
import pygame
from pygame.locals import *
import constants
#import player
import bricks
import player
pygame.init()

#Start Class Declaration
class PyBreakout:

    def __init__(self):
        self.initialize()
        self.mainLoop()

    #Declare variables and initialization classes here
    def initialize(self):
        pygame.init()

        self.width = 924
        self.height = 768
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.caption = "pyBreakout"
        pygame.display.set_caption(self.caption)

        self.framerate = 60
        #self.backgroundColour = (255,255,255)
        #self.foregroundColour = (0,99,207)

        self.clock = pygame.time.Clock()

        self.fontScore = pygame.font.SysFont("Arial Black", 21, bold=False)

        self.gameScore = 0
        self.gameBatsLeft = 3
        self.gameBricksLeft = 120

        #self.brick = bricks.Brick(self.screen)

        self.ticks = 0

        #initialize the bricks that will be displayed
        self.bricksArr = []
        # xPos = 44
        # yPos = 160
        # for i in range(12):
        #     brickObj = bricks.Brick(self.screen)
        #     brickObj.setPosX(xPos)
        #     brickObj.setPosY(yPos)
        #     self.bricksArr.append(brickObj)
        #     xPos += 70

        self.initBricks()

        self.bat = player.Bat(self.screen)

    def initBricks(self):
        yPos = 160
        for x in range(10):
            xPos = 44
            for i in range(12):
                brickObj = bricks.Brick(self.screen)
                brickObj.setPosX(xPos)
                brickObj.setPosY(yPos)
                self.bricksArr.append(brickObj)
                xPos += 70
            yPos += 22

    def mainLoop(self):
        while True:
            gameTime = self.clock.get_time()
            self.update(gameTime)
            self.draw(gameTime)
            self.clock.tick(self.framerate)

    def update(self, gameTime):

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.bat.setPosX(self.bat.getPosX() - 10)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.bat.setPosX(self.bat.getPosX() + 10)

        self.ticks = self.ticks + gameTime

    def draw(self, gameTime):
        self.screen.fill(constants.backgroundColour)

        labelBricksLeft = self.fontScore.render("Bricks Left: %d" % self.gameBricksLeft, 1, constants.foregroundColour)
        labelBatsLeft = self.fontScore.render("Bats Left: %d" % self.gameBatsLeft, 1, constants.foregroundColour)
        labelScore = self.fontScore.render("Score: %d" % self.gameScore, 1, constants.foregroundColour)

        #write text to screen
        self.screen.blit(labelBricksLeft, (20,20))
        self.screen.blit(labelBatsLeft, (370,20))
        self.screen.blit(labelScore, (710,20))

        #Draw bounding boxes
        pygame.draw.rect(self.screen, constants.foregroundColour, [20,50,20,650])
        pygame.draw.rect(self.screen, constants.foregroundColour, [20,50,884,20])
        pygame.draw.rect(self.screen, constants.foregroundColour, [884,50,20,650])

        #This is an area for improvemnt through a mathematical function and loops
        c = 0
        for x in range(120):
            self.bricksArr[x].draw(c)
            if (x == 23 or x == 47 or x == 71 or x == 95):
                c = c + 1

        self.bat.draw()


        pygame.display.flip()

if __name__ == "__main__":
    game = PyBreakout()
