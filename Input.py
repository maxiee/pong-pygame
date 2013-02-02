import pygame
import sys

class UserInput():
    def __init__(self):
        self.keyStatus = []

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keyStatus.append(event.key)
            if event.type == pygame.KEYUP:
                if event.key in self.keyStatus:
                    self.keyStatus.remove(event.key)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                    