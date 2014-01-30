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

		chance_counter = 0
		for i in range(10000):
			if (self.random_module.roll(.5)):
				chance_counter = chance_counter + 1

		self.assertTrue(
			chance_counter < 6000 and chance_counter > 4000)

		print chance_counter


if __name__ == '__main__':
	unittest.main()