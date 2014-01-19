import unittest
import constants
import seed

class TestSeedGroup(unittest.TestCase):
	
	def setUp(self):
		self.generator = seed.SeedGenerator()
		self.seed_group = self.generator.generate_seed()

	def test_parents(self):
		#every agent in the seed group should have a parent
		#given that they are below young adulthood
		male_adulthood_age = constants.ADULTHOOD_AGE["m"]
		female_adulthood_age = constants.ADULTHOOD_AGE["f"]
		adulthood_age = 0

		for agent in self.seed_group:

			if (agent != None):
				if (agent.sex == "SEX_MALE"):
					adulthood_age = male_adulthood_age
				else:
					adulthood_age = female_adulthood_age

				if (agent.age < adulthood_age):
					self.assertIsNotNone(agent.parent)

	def test_sisters(self):
		#there must be at least one pair of sisters in the seed
		#only two females can be sisters
		one_sister_found = False 

		for agent in self.seed_group:
			if (agent != None):
				if (agent.sisters != None):
					one_sister_found = True
