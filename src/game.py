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

        self.width = 1024
        self.height = 768
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.caption = "pyBreakout"
        pygame.display.set_caption(self.caption)

        self.framerate = 60
        self.backgroundColour = (255,255,255)

        self.clock = pygame.time.Clock()

        self.fontScore = pygame.font.SysFont("Arial", 15)

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

        labelScore = self.fontScore.render("Hello", 1, (0,0,200))
        self.screen.blit(labelScore, (100,100))

        pygame.display.flip()

if __name__ == "__main__":
    game = PyBreakout()
