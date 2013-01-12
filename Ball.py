import pygame
import config
import random
import math

class Ball():
    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(self.surface.get_width()/2.0, self.surface.get_height()/2.0, config.ball['radius'], config.ball['radius'])
        self.acc = config.ball['acc']
        self.angle = random.randint(0, 360)
        #self.angle = 90
        self.angle = (math.pi/180) * self.angle
        self.color = config.colors[config.ball['color']]
        self.vx = 0
        self.vy = 0

    def update(self):
        if abs(self.vx) + self.acc < config.ball['max_speed']:
            self.vx += self.acc
        if abs(self.vy) + self.acc < config.ball['max_speed']:
            self.vy += self.acc
        
        self.rect.x += math.sin(self.angle) * self.vx
        self.rect.y += math.cos(self.angle) * self.vy
        print self.rect.center[1]
        if self.rect.center[1] > 0:
            self.vy *= -1.0
        if self.rect.center[1] < self.surface.get_height() - config.ball['radius']:
            self.vy *= -1.0

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.rect.center, self.rect.size))

    def on_collide(self):
        pass