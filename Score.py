import pygame
import config

class Score():
	def __init__(self, surface):
		self.surface = surface
		self.score = pygame.font.Font(None, 50)
		self.player1 = 0
		self.player2 = 0

	def draw(self):
		pscore = str(self.player1) + '   ' + str(self.player2)
		pos = (config.config['width']/2, 50)
		self.surface.blit(
			self.score.render(pscore, True, config.colors[config.score['color']]), pos)