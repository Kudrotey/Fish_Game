import pygame
from pygame.sprite import Sprite
from random import randint, uniform

class Hook(Sprite):

	def __init__(self, bs_game):
		super().__init__()
		self.screen = bs_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = bs_game.settings
		self.colour = (0,0,0)

		# Creating a hook
		self.rect = pygame.Rect(0,0,15,700)
		self.rect.midbottom = self.screen_rect.midtop

		self.y = float(self.rect.y)

		self.go_up = False

	def update(self):

		if not self.go_up:
			self.y += self.settings.increase_speed

		if self.go_up:
			self.y -= 0.5

		self.rect.y = self.y

	def center_hook(self):
		'''Center the ship on the screen'''
		random_number_x = randint(50, self.settings.screen_width - 150)
		self.rect.x = random_number_x
		self.y = float(self.rect.y)
	
	def draw_hook(self):
		pygame.draw.rect(self.screen, self.colour, self.rect)


class Line(Sprite):

	def __init__(self, bs_game):
		super().__init__()
		self.screen = bs_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = bs_game.settings
		self.colour = (100,100,100)

		# Creating a hook line
		self.rect = pygame.Rect(0,0,3,40)
		self.rect.midtop = bs_game.hook.rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.go_up = False

	def update(self, bs_game):

		if not self.go_up:
			self.y += self.settings.increase_speed
		
		if self.rect.bottom >= self.screen_rect.bottom:
			self.go_up = True
			bs_game.hook.go_up = True

		if self.go_up:
			self.y -= 0.5


		self.rect.y = self.y

	def center_line(self, bs_game):
		'''Center the ship on the screen'''
		self.rect.midtop = bs_game.hook.rect.midbottom
		self.y = float(self.rect.y)
	
	def draw_line(self):
		pygame.draw.rect(self.screen, self.colour, self.rect)

