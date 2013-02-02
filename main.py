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
        self.ball.randomize_direction()
        self.paddle1 = Paddle.Paddle(self.surfaceObject, 0, self.keys.keyStatus)
        self.paddle2 = Paddle.Paddle(self.surfaceObject, 1, self.keys.keyStatus)
        self.score = Score.Score(self.surfaceObject)
        pygame.mixer.init()
        # pygame.mixer.pre_init(44100, -16, 2, 2048)
        self.snd_bounce = pygame.mixer.Sound("res\\paddle_bounce.wav")
        self.snd_bounce.set_volume(0.3)
        self.snd_main = pygame.mixer.Sound("res\\main_loop.ogg")
        self.snd_main.set_volume(0.5)
        self.snd_main.play(-1)

    def update(self):
        # pygame.display.set_caption('PyPong FPS: %d' %self.mainClock.get_fps())
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
            self.snd_bounce.play()
        elif self.ball.rect.contains(self.paddle1.rect) or self.ball.rect.contains(self.paddle2.rect):
            self.ball.collide_with_paddle()
            self.snd_bounce.play()

        #Checks wall collisions
        if self.ball.rect.top <= 0.0 - config.ball['size']/2:
            self.ball.collide_with_wall()
        if self.ball.rect.top > self.ball.screen_height - config.ball['size']/2:
            self.ball.collide_with_wall()

    def ball_out_of_screen(self):
        if self.ball.rect.right < 0:
            self.score.player2 += 1
            self.ball.randomize_direction()
            self.ball.reset()
        if self.ball.rect.left > self.surfaceObject.get_width():
            self.score.player1 += 1
            self.ball.randomize_direction()
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
            self.mainClock.tick_busy_loop(config.config['FPS'])

if __name__=='__main__':
    game = Game()
    game.run()