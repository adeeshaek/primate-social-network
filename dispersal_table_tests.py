import unittest
import loader

class TestDispersalTable(unittest.TestCase):

	def setUp(self):
		self.data = loader.load_data()

	def test_chance_of_emigration(self):
		#there are no negative likelihoods
		chance = self.data.dispersal_table.chance_of_emigration(10000, 3)
		self.assertFalse(chance < 0)

