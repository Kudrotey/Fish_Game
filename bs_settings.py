import random

class Settings:

	def __init__(self, bs_game):

		# Game Settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_colour = (0,160,255)

		# Fish Settings
		self.fish_speed_x = 1.0
		self.fish_speed_y = 0.5
		self.fish_limit = 1

		# Worm Settings
		self.worm_allowed = 3
		self.worm_drop_speed = 0.5
		self.speed_scale = 1.1

		# Score settings
		self.points = 50

		self.change_speed()
		self.increase_hook_speed()

	def change_speed(self):
		self.random_speed = random.uniform(0.25,1)

	def increase_hook_speed(self):
		self.increase_speed = 2.5



