import pygame.font 

class Score:

	def __init__(self, bs_game):
		self.screen = bs_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = bs_game.settings
		self.stats = bs_game.stats

		self.text_colour = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)

		self.prep_score()

	def prep_score(self):
		# Turn the score into a rendered image
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str,
			True, self.text_colour, self.settings.bg_colour)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)