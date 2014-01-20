import unittest
import friendships
from agent import AgentClass
from random_module import FakeRandomModule

class TestFriendships(unittest.TestCase):

	def test_chance_of_making_friends(self):
		self.assertEqual(friendships.chance_of_making_friends(3), 0)
		self.assertEqual(friendships.chance_of_making_friends(2), 0.05)
		self.assertEqual(friendships.chance_of_making_friends(1), 0.1)
		self.assertEqual(friendships.chance_of_making_friends(0), 0.15)

	def test_make_friend(self):
		fake_random_module = FakeRandomModule()

		parent = AgentClass(12, "f", "A", None, None, None, None)#0
		underage_male =\
			AgentClass(6, "m", None, 0, None, None, None)#1
		underage_female =\
			AgentClass(4, "f", None, 0, None, None, None)#2
		of_age_male_1 = AgentClass(6, "m", None, 0, 0, 0, 0)#3
		of_age_male_2 = AgentClass(6, "m", None, 0, 0, 0, 0)#4
		of_age_female_1 = AgentClass(6, "m", None, 0, 0, 0, 0)#5
		of_age_female_2 = AgentClass(6, "m", None, 0, 0, 0, 0)#6

		group = []
		group.append(parent)
		group.append(underage_male)
		group.append(underage_female)
		group.append(of_age_male_1)
		group.append(of_age_male_2)

		#underage male shouldn't be able to make friendships
		self.assertEqual(friendships.make_friend(underage_male,
		 group, fake_random_module), None)

		#underage female shouldn't be able to make friendships
		self.assertEqual(friendships.make_friend(underage_female,
		 group, fake_random_module), None)

				