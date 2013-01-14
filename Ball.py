import pygame
import config
import random
import math
import Vec2d

class Ball():
    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(self.surface.get_width()/2, self.surface.get_height()/2, config.ball['size'], config.ball['size'])
        self.acc = config.ball['acc']
        self.max_speed = config.ball['max_speed']
        self.color = config.colors[config.ball['color']]
        self.screen_height = self.surface.get_height()
        self.screen_width = self.surface.get_width()
        self.direction = Vec2d.Vec2d(1, 1)
        self.velocity = Vec2d.Vec2d(0, 0)
        self.speed = 0
        self.hitmask = self.get_full_hitmask(self.rect)

    def update(self):
        self.hitmask = self.get_full_hitmask(self.rect)
        self.speed += self.acc
        self.cap_acc()

        self.velocity.x = self.direction.x * self.speed
        self.velocity.y = self.direction.y * self.speed

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.collide_with_wall():
            self.direction.y -= random.uniform(0.1, 0.3)
            self.direction.y *= -1        

    def collide_with_wall(self):
        if self.rect.y <= 0 - config.ball['size']/2:
            return True
        if self.rect.y > self.screen_height - config.ball['size'] -config.ball['size']/2:
            return True
        return False

    def collide_with_paddle(self):
        print 'Collision with paddle'
        self.direction.x -= random.uniform(0.1, 0.3)
        self.direction.x *= -1

    def cap_acc(self):
        if abs(self.speed) > self.max_speed:
            if self.speed < 0:
                self.speed = -self.max_speed
            else:
                self.speed = self.max_speed

    def get_full_hitmask(self, rect):
        """returns a completely full hitmask that fits the image,
           without referencing the images colorkey or alpha."""
        mask=[]
        for x in range(rect.width):
            mask.append([])
            for y in range(rect.height):
                mask[x].append(True)
        return mask

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.rect.center, self.rect.size))