class Player:
	def __init__(self, color, socket = None):
		self.color = color
		self.points = 0
		self.socket = socket

	def points(self, points): 
		self.points += points

	


