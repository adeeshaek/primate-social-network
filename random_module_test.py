import unittest
import random_module

class TestRandomModule(unittest.TestCase):

	def setUp(self):
		self.random_module = random_module.RandomModule()

	def test_roll(self):
		for i in range(10):
			#an event given a probability of 0 should not happen
			self.assertFalse(self.random_module.roll(0))

			#an event given a probability of 1 should happen
			self.assertTrue(self.random_module.roll(1))
