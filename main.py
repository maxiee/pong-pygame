import pygame
import config
import sys
import Input
import Paddle
import Ball
import Score

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
        self.score = Score.Score(self.surfaceObject)

    def update(self):
        pygame.display.set_caption('PyPong FPS: %d' %self.mainClock.get_fps())
        self.ball.update()
        self.paddle1.update()
        self.paddle2.update()
        self.check_collisions()
        self.ball_out_of_screen()

    def draw(self):
        self.surfaceObject.fill(config.colors['black'])
        self.ball.draw()
        self.paddle1.draw()
        self.paddle2.draw()
        self.score.draw()

    def check_collisions(self):
        #Checks paddle collisions
        if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
            self.ball.collide_with_paddle()
        elif self.ball.rect.contains(self.paddle1.rect) or self.ball.rect.contains(self.paddle2.rect):
            self.ball.collide_with_paddle()
        #Checks wall collisions
        if self.ball.rect.y <= 0.0 - config.ball['size']/2.0:
            self.ball.collide_with_wall()
        if self.ball.rect.y > self.ball.screen_height - config.ball['size'] - config.ball['size']/2:
            self.ball.collide_with_wall()

    def ball_out_of_screen(self):
        if self.ball.rect.right < 0:
            self.score.player1 += 1
            self.ball.reset()
        if self.ball.rect.left > self.surfaceObject.get_width():
            self.score.player2 += 1
            self.ball.reset()
        
    def run(self):
        while self.running:
            if pygame.K_ESCAPE in self.keys.keyStatus:
                pygame.quit()
                sys.exit()
            self.keys.get_input()
            self.update()
            self.draw()
            pygame.display.flip()
            self.mainClock.tick(config.config['FPS'])

if __name__=='__main__':
    game = Game()
    game.run()