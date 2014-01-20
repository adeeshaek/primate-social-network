"""
Macaque Simulation Project
Adeesha Ekanayake 
19/1/2014

random_module.py
----------------
acts as a die-roller, converting a probability into a yes or no
"""
import random

class RandomModule(random.Random):

	ceiling = 5000 #upper limit used to calculate probability

	def roll(self, probability):
		"""
		executes a die-roll for given probability, by generating a random
		number between 0 and ceiling. If the generated random number is
		less than the probability * ceiling, then the method returns true

		parameters
		----------
		probability: the probability of the event, between 0 and 1

		returns
		-------
		True if dieroll is successful, or False if not
		"""
		#+1 prevents occasional failures when probability is 1
		#because of the +1, the ceiling must be a relatively big
		#number
		threshold = (probability * self.ceiling) + 1 

		random_value = self.randint(0, self.ceiling)

		if (random_value < threshold):
			return True

		else:
			return False

class FakeRandomModule(RandomModule):
	"""
	used for testing methods that use randomness. This method overloads
	roll so that it always returns true
	"""

	def roll(self, probability):
		"""
		fake roll method that always returns true
		"""
		return True

