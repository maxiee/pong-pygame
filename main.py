import pygame
import config
import sys

class Ball():
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.radius = config.config['ballRadius']
        self.speed = speed
        self.color = color

    def update(self):
        self.x += self.speed
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    def reflect(self):
        self.x *= -1
        self.y *= -1

    def on_collide(self):
        pass

class Paddle():
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pass

    def on_collide(self):
        pass

class UserInput():
    def __init__(self):
        self.keyStatus = []

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #self.keyStatus.append(pygame.QUIT)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.keyStatus.append(event.key)
            if event.type == pygame.KEYUP:
                self.keyStatus.remove(event.key)

class Game():
    def __init__(self):
        self.running = True
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.surfaceObject = pygame.display.set_mode((config.config['width'], config.config['height']))
        self.keys = UserInput()
        self.deltaTime = 0

    def update(self):
        pygame.display.set_caption('PyPong FPS: %d' %self.mainClock.get_fps())
        if self.player1.top > 0:
            if pygame.K_UP in self.keyStatus.keys():
                if self.keyStatus[pygame.K_UP]:
                    self.player1.top -= config['speed']
        if self.player1.bottom < self.surfaceObject.get_height():
            if pygame.K_DOWN in self.keyStatus.keys():
                if self.keyStatus[pygame.K_DOWN]:
                    self.player1.bottom += config['speed']
        self.ball.move()

    def draw(self):
        self.surfaceObject.fill((0,0,0))
        pygame.draw.rect(self.surfaceObject, colors['white'], self.player1)
        pygame.draw.rect(self.surfaceObject, colors['white'], self.player2)
        self.ball.draw()

    def flip(self):
        pygame.display.update()

    def run(self):
        while self.running:
            self.keys.get_input()
            self.update()
            self.draw()
            self.flip()
            self.deltaTime = self.mainClock.tick(config['FPS'])

if __name__=='__main__':
    app = Game()
    app.run()