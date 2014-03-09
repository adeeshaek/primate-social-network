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
		if (self.count == 0):
			#this is to avoid div by 0 error
			return 0.0000001 
		else:
			return self.count
