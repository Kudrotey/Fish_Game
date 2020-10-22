import pygame
from pygame.sprite import Sprite

class Fish(Sprite):

	def __init__(self, bs_game):
		super().__init__()
		self.screen = bs_game.screen
		self.screen_rect = bs_game.screen.get_rect()
		self.settings = bs_game.settings

		self.image = pygame.image.load('fish.bmp')
		self.image = pygame.transform.scale(self.image, (150,150))
		self.rect = self.image.get_rect()

		self.rect.midright = self.screen_rect.midright

		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.open_top = False
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)

	def update(self):
		if self.moving_left:
			self.x -= self.settings.fish_speed_x

		if self.x < -(self.rect.width):
			self.x = self.screen_rect.width + 50

		if not self.open_top:
			if self.moving_up and self.rect.top > 0:
				self.y -= self.settings.fish_speed_y

		if self.open_top:
			if self.rect.bottom > 0:
				self.y -= 0.5

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.fish_speed_y

		self.rect.x = self.x
		self.rect.y = self.y

	def fish_pos(self):
		self.rect.midright = self.screen_rect.midright
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)


	def blitme(self):
		self.screen.blit(self.image, self.rect)



class Seaweed(Sprite):

	def __init__(self, bs_game):
		super().__init__()
		self.screen = bs_game.screen
		self.screen_rect = bs_game.screen.get_rect()

		self.image = pygame.image.load('seaweed.bmp')
		self.image = pygame.transform.scale(self.image, (150, 200))
		self.rect = self.image.get_rect()

		self.rect.bottomleft = self.screen_rect.bottomleft


	