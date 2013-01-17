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
        self.paddle1 = Paddle.Paddle(self.surfaceObject, 0, self.keys.keyStatus)
        self.paddle2 = Paddle.Paddle(self.surfaceObject, 1, self.keys.keyStatus)

    def update(self):
        pygame.display.set_caption('PyPong FPS: %d' %self.mainClock.get_fps())
        self.ball.update()
        self.paddle1.update()
        self.paddle2.update()
        self.collide_with_paddle()

    def draw(self):
        self.surfaceObject.fill(config.colors['black'])
        self.ball.draw()
        self.paddle1.draw()
        self.paddle2.draw()

    def flip(self):
        pygame.display.update()

    def collide_with_paddle(self):
        if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
            self.ball.collide_with_paddle()
        elif self.ball.rect.contains(self.paddle1.rect) or self.ball.rect.contains(self.paddle2.rect):
            self.ball.collide_with_paddle()

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