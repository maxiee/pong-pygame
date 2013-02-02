import pygame
import config

class Paddle():
    def __init__(self, surface, side, keyStatus):
        self.surface = surface
        self.side = side
        self.keyStatus = keyStatus
        self.screen_height = self.surface.get_height()

        if self.side == 1:
            self.init_x = self.surface.get_width() - config.paddle['width']
            self.init_y = self.surface.get_height()/2
        else:
            self.init_x = 0
            self.init_y = self.surface.get_height()/2

        self.rect = pygame.Rect(self.init_x, self.init_y, config.paddle['width'], config.paddle['height'])
        self.speed = config.paddle['speed']
        self.color = config.colors[config.paddle['color']]

    def update(self):
        if pygame.K_UP in self.keyStatus and self.rect.top >= 0:
            self.rect.y -= self.speed
        if pygame.K_DOWN in self.keyStatus and self.rect.bottom <= self.screen_height:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)