"""
Macaque Simulation Project
Adeesha Ekanayake 
1/02/2014

counter.py
----------
counts the number of individuals
"""

class Counter:
	"""
	a convenient way to quickly count values
	"""

	def __init__(self):
		self.count = 0

	def increment(self):
		self.count += 1

	def reset(self):
		self.count = 0

	def getCount(self):
		return self.count
