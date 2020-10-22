import pygame
from pygame.sprite import Sprite 
import random

class Worm(Sprite):
	'''This class focuses on worms'''
	
	def __init__(self, bs_game):
		'''Initialize the worm assets and behaviour'''
		super().__init__()
		self.screen = bs_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = bs_game.settings

		self.image = pygame.image.load('worm.bmp')
		self.image = pygame.transform.scale(self.image, (60,30))
		self.rect = self.image.get_rect()
		self.rect.y = random.uniform(0, self.screen_rect.height/2)
		self.y = float(self.rect.y)

	def update(self):
		'''Make the worm drop down'''

		self.y += self.settings.random_speed

		self.rect.y = self.y
