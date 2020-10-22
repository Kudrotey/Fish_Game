import sys
import pygame
from time import sleep
from random import randint
import random 
from fish import Fish
from fish import Seaweed
from worm import Worm 
from hook import Hook 
from hook import Line
from play_button import Button 
from score import Score 
from bs_game_stats import GameStats 

from bs_settings import Settings 

class BlueSky:

	def __init__(self):
		# pygame.init is used to deploy the background
		pygame.init()
		# self.screen will display a window with 1200 by 700 screen size
		self.settings = Settings(self)
		self.screen = pygame.display.set_mode((self.settings.screen_width
											,self.settings.screen_height))
		self.screen_rect = self.screen.get_rect()
		# bg_colour will give a background colour
		self.bg_colour = self.settings.bg_colour
		# self.captions will create a title at the top of the window
		pygame.display.set_caption('Blue Sky')

		self.fish = Fish(self)
		self.seaweeds = pygame.sprite.Group()
		self.worms = pygame.sprite.Group()
		self.hook = Hook(self)
		self.line = Line(self)

		self.stats = GameStats(self)

		self._create_fleet()
		self._create_worms()

		self.clock = pygame.time.Clock()
		self.counter = 0
		pygame.time.set_timer(pygame.USEREVENT, 1000)

		self.play = Button(self, 'Play')
		self.sb = Score(self)

	def run_game(self):

		while True:
			self._check_events()

			if self.stats.game_active:
				self.fish.update()
				self.worms.update()
				self._update_hooks()
				self._update_worms()
			
			self._screen_update()

	def _create_fleet(self):
		# Make a seaweed
		seaweed = Seaweed(self)	
		seaweed_width = seaweed.rect.width
		number_seaweeds_x = self.screen_rect.width // seaweed_width

		for number_seaweed in range(number_seaweeds_x):
			# Create a seaweed and place it in position
			seaweed = Seaweed(self)
			seaweed.x = (seaweed_width * number_seaweed)
			seaweed.rect.x = seaweed.x 
			self.seaweeds.add(seaweed)

	def _create_worms(self):
		'''Create a worm'''
		worm = Worm(self)
		worm_width, worm_height = worm.rect.size
		
		for worm_num in range(3):
			worm = Worm(self)
			random_number_x = randint(worm_width, self.settings.screen_width - worm_width)
			worm.rect.x = random_number_x
			self.worms.add(worm)

	def _update_worms(self):
		'''Remove any worms that have reached the bottom of the screen'''
		for worm in self.worms.copy():
			if worm.rect.y > self.settings.screen_height:
				self.worms.remove(worm) 

		collisions = pygame.sprite.spritecollide(self.fish, self.worms, dokill = self.worms)

		if collisions:
			self.stats.score += self.settings.points
			self.sb.prep_score()


		if not self.worms:
			self._create_worms()
			self.settings.change_speed()

	def _update_hooks(self):

		'''Remove the hook when it reaches the bottom of the screen'''
		if self.line.rect.bottom < -20 and self.line.go_up == True and self.hook.go_up == True:
			self.counter = random.uniform(0,10)
			self.hook.center_hook()
			self.line.center_line(self)
			self.hook.go_up = False
			self.line.go_up = False
			self.settings.increase_hook_speed()

		if self.counter <= 0:

			self.hook.update()
			self.line.update(self)


		# Look for collision between fish and hook
		if pygame.sprite.collide_rect(self.fish,self.line):

			self.stats.key_active = False
			self.fish.moving_left = False
			self.fish.moving_down = False
			self.fish.moving_up = False
			self.fish.open_top = True
			self.hook.go_up = True
			self.line.go_up = True

			if self.fish.y < -20:
				self.stats.game_active = False
				pygame.mouse.set_visible(True)

	def _screen_update(self):
		self.screen.fill(self.bg_colour)
		self.fish.blitme()
		self.seaweeds.draw(self.screen)

		self.hook.draw_hook()
		self.line.draw_line()

		self.worms.draw(self.screen)

		self.sb.show_score()

		if not self.stats.game_active:
			self.play.draw_button()



		pygame.display.flip()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if self.stats.key_active:
					if event.key == pygame.K_LEFT:
						self.fish.moving_left = True
					if event.key == pygame.K_UP:
						self.fish.moving_up = True
					if event.key == pygame.K_DOWN:
						self.fish.moving_down = True

				if event.key == pygame.K_q:
					sys.exit()

			elif event.type == pygame.KEYUP:
				self.fish.moving_left = False
				self.fish.moving_up = False
				self.fish.moving_down = False

			elif event.type == pygame.USEREVENT:
				self.counter -= 1

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _check_play_button(self, mouse_pos):

		button_clicked = self.play.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Reset the game statistics
			self.stats.reset_stats()

			# Get rid of any worms
			self.worms.empty()

			# Position the fish and hook
			self.stats.key_active = True
			self.sb.prep_score()
			self.fish.open_top = False
			self.hook.go_up = False
			self.line.go_up = False
			self.fish.fish_pos()
			self.stats.game_active = True

			# Hide the mouse cursor
			pygame.mouse.set_visible(False)


if __name__ == '__main__':
	bs = BlueSky()
	bs.run_game()

