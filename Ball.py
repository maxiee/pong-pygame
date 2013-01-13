import pygame
import config
import random
import math
import Vec2d

class Ball():
    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(self.surface.get_width()/2.0, self.surface.get_height()/2.0, config.ball['size'], config.ball['size'])
        self.acc = config.ball['acc']
        self.max_speed = config.ball['max_speed']
        self.color = config.colors[config.ball['color']]
        self.screen_height = self.surface.get_height()
        self.screen_width = self.surface.get_width()
        self.direction = Vec2d.Vec2d(-0.2, -1.0)
        self.velocity = Vec2d.Vec2d(0.0, 0.0)

    def update(self):
        self.velocity.x += self.acc
        self.velocity.y += self.acc
        self.cap_acc()

        self.rect.x += self.direction.x * self.velocity.x
        self.rect.y += self.direction.y * self.velocity.y
        if self.collide_with_wall():
            self.direction.y *= -1.0

    def collide_with_wall(self):
        if self.rect.y < 0 - config.ball['size']/2.0:
            return True
        if self.rect.y > self.screen_height - config.ball['size']:
            return True
        return False

    def cap_acc(self):
        if self.velocity.x > self.max_speed:
            self.velocity.x = self.max_speed
        if self.velocity.y > self.max_speed:
            self.velocity.y = self.max_speed

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.rect.center, self.rect.size))

    def on_collide(self):
        pass