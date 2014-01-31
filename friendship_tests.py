import unittest
import friendships
from agent import AgentClass
from group import AgentGroup
from random_module import FakeRandomModule

class TestFriendships(unittest.TestCase):

	def test_chance_of_making_friends(self):
		self.assertEqual(friendships.chance_of_making_friends(3), 0)
		self.assertEqual(friendships.chance_of_making_friends(2), 0.05)
		self.assertEqual(friendships.chance_of_making_friends(1), 0.1)
		self.assertEqual(friendships.chance_of_making_friends(0), 0.15)

	def test_make_friend(self):
		fake_random_module = FakeRandomModule()

		parent = AgentClass(
		 12, "f", "A", None, None, None, None, 1)#0
		underage_male =\
			AgentClass(6, "m", None, 0, None, None, None, 2)#1
		underage_female =\
			AgentClass(4, "f", None, 0, None, None, None, 3)#2
		of_age_male_1 = AgentClass(
		 8, "m", None, 0, [], [], [], 4)#3
		of_age_male_2 = AgentClass(
		 8, "m", None, 0, [], [], [], 5)#4
		of_age_female_1 = AgentClass(
		 6, "f", None, 0, [], [], [], 6)#5
		of_age_female_2 = AgentClass(
		 6, "f", None, 0, [], [], [], 7)#6

		group = AgentGroup()
		group.add_agent(parent)
		group.add_agent(underage_male)
		group.add_agent(underage_female)
		group.add_agent(of_age_male_1)
		group.add_agent(of_age_male_2)
		group.add_agent(of_age_female_1)
		group.add_agent(of_age_female_2)
		group.mark_as_parent(parent, [2,3,4,5,6,7])

		#underage male shouldn't be able to make friendships
		self.assertEqual(friendships.make_friend(underage_male,
		 group, fake_random_module), None)

		#underage female shouldn't be able to make friendships
		self.assertEqual(friendships.make_friend(underage_female,
		 group, fake_random_module), None)

		#there should be one of the two random females for the 
		#of_age male
		result_for_male = friendships.make_friend(
			of_age_male_1, group, fake_random_module)
		truth_value_for_male =\
		 result_for_male == of_age_female_1.index or \
		  result_for_male == of_age_female_2.index
		self.assertTrue(truth_value_for_male)

		#there should be one of the two random males for the
		#of age female
		result_for_female = friendships.make_friend(
			of_age_female_1, group, fake_random_module)
		truth_value_for_female =\
		 result_for_female == of_age_male_1.index or \
		  result_for_female == of_age_male_2.index
		self.assertTrue(truth_value_for_female)

if __name__ == '__main__':
	unittest.main()