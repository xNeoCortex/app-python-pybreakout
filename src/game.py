#Requirements
import sys
import pygame
from pygame.locals import *
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
        self.backgroundColour = (255,255,255)
        self.foregroundColour = (0,99,207)

        self.clock = pygame.time.Clock()

        self.fontScore = pygame.font.SysFont("Arial Black", 21, bold=False)

        self.gameScore = 0
        self.gameBatsLeft = 3
        self.gameBricksLeft = 120

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

    def draw(self, gameTime):
        self.screen.fill(self.backgroundColour)

        labelBricksLeft = self.fontScore.render("Bricks Left: %d" % self.gameBricksLeft, 1, self.foregroundColour)
        labelBatsLeft = self.fontScore.render("Bats Left: %d" % self.gameBatsLeft, 1, self.foregroundColour)
        labelScore = self.fontScore.render("Score: %d" % self.gameScore, 1, self.foregroundColour)
        self.screen.blit(labelBricksLeft, (20,20))
        self.screen.blit(labelBatsLeft, (370,20))
        self.screen.blit(labelScore, (710,20))

        pygame.display.flip()

if __name__ == "__main__":
    game = PyBreakout()
