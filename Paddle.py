import pygame
import config

class Paddle():
    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(0, 0, config.paddle['width'], config.paddle['height'])
        self.speed = config.paddle['speed']
        self.color = config.colors[config.paddle['color']]

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.rect.center, self.rect.size))

    def on_collide(self):
        pass