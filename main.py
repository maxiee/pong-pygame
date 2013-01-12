import pygame
import config
import sys
import Input
import Paddle
import Ball

class Game():
    def __init__(self):
        self.running = True
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.surfaceObject = pygame.display.set_mode((config.config['width'], config.config['height']))
        self.keys = Input.UserInput()
        self.ball = Ball.Ball(self.surfaceObject)

    def update(self):
        pygame.display.set_caption('PyPong FPS: %d' %self.mainClock.get_fps())
        self.ball.update()

    def draw(self):
        self.surfaceObject.fill(config.colors['black'])
        self.ball.draw()

    def flip(self):
        pygame.display.update()

    def run(self):
        while self.running:
            self.keys.get_input()
            self.update()
            self.draw()
            self.flip()
            self.mainClock.tick(config.config['FPS'])

if __name__=='__main__':
    app = Game()
    app.run()