import unittest
import constants
import seed
from population import Population

class TestSeedGroup(unittest.TestCase):
	
	def setUp(self):
		population = Population()
		self.generator = seed.SeedGenerator()
		self.seed_group = self.generator.generate_seed(population)

	def test_parents(self):
		#every agent in the seed group should have a parent
		#given that they are below young adulthood
		male_adulthood_age = constants.ADULTHOOD_AGE["m"]
		female_adulthood_age = constants.ADULTHOOD_AGE["f"]
		adulthood_age = 0

		for agent_index in self.seed_group.whole_set:
			agent = self.seed_group.agent_dict[agent_index]
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
		for agent_index in self.seed_group.whole_set:
			agent = self.seed_group.agent_dict[agent_index]
			if (agent != None):
				if (agent.sisters != None):
					one_sister_found = True

		self.assertTrue(one_sister_found)

	def test_index(self):
		#test the index of each individual to make sure it
		#refers to the correct one
		for agent_index in self.seed_group.whole_set:
			self.assertEquals(agent_index, 
				self.seed_group.agent_dict[agent_index].index)


