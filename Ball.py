import pygame
import config
import math
import Vec2d
import time

class Ball():
    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(self.surface.get_width()/2, self.surface.get_height()/2, config.ball['size'], config.ball['size'])
        self.acc = config.ball['acc']
        self.max_speed = config.ball['max_speed']
        self.color = config.colors[config.ball['color']]
        self.screen_height = self.surface.get_height()
        self.screen_width = self.surface.get_width()
        self.direction = Vec2d.Vec2d(1.0, 1.0)
        self.velocity = Vec2d.Vec2d(0.0, 0.0)
        self.position = Vec2d.Vec2d(float(self.rect.x), float(self.rect.y))
        self.speed = 0.0

    def update(self):
        self.speed += self.acc
        self.cap_acc()

        self.velocity.x = self.direction.x * self.speed
        self.velocity.y = self.direction.y * self.speed

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # self.rect.x += self.velocity.x
        # self.rect.y += self.velocity.y

        self.rect.center = (round(self.position.x), round(self.position.y))

    def collide_with_paddle(self):
        self.direction.x *= -1.0

    def collide_with_wall(self):
        self.direction.y *= -1.0

    def cap_acc(self):
        if abs(self.speed) > self.max_speed:
            if self.speed < 0.0:
                self.speed = -self.max_speed
            else:
                self.speed = self.max_speed

    def reset(self):
        self.position.x = float(self.screen_height/2) 
        self.position.y = float(self.screen_width/2)

    def random_direction(self):
        pass

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)