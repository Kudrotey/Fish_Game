class GameStats:
	"""docstring for GameStats"""
	def __init__(self, bs_game):
		
		self.settings = bs_game.settings
		self.reset_stats()
		self.key_active = True
		self.game_active = False

	def reset_stats(self):
		self.score = 0
		