import pygame

class UserInput():
    def __init__(self):
        self.keyStatus = []

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.keyStatus.append(event.key)
            if event.type == pygame.KEYUP:
                try:
                    self.keyStatus.remove(event.key)
                except e:
                    print e