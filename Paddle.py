import pygame
import config

class Paddle():
    def __init__(self, surface, side, keyStatus):
        self.surface = surface
        self.side = side
        self.keyStatus = keyStatus
        self.screen_height = self.surface.get_height()

        if self.side == 1:
            self.init_x = self.surface.get_width() - config.paddle['width'] - config.paddle['width'] / 2
            self.init_y = self.surface.get_height()/2
        else:
            self.init_x = 0 - config.paddle['width']/2
            self.init_y = self.surface.get_height()/2

        self.rect = pygame.Rect(self.init_x, self.init_y, config.paddle['width'], config.paddle['height'])
        self.speed = config.paddle['speed']
        self.color = config.colors[config.paddle['color']]
        self.hitmask = self.get_full_hitmask(self.rect)

    def update(self):
        if pygame.K_UP in self.keyStatus and self.rect.top + self.rect.size[1]/2 >= 0:
            self.rect.y -= self.speed
        if pygame.K_DOWN in self.keyStatus and self.rect.bottom + self.rect.size[1]/2 <= self.screen_height:
            self.rect.y += self.speed
        self.hitmask = self.get_full_hitmask(self.rect)

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