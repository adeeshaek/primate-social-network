import unittest
import agent
from copy import copy, deepcopy

class TestAgent(unittest.TestCase):

	def setUp(self):

		age = 5
		sex = "m"
		is_alpha = "A"
		
		self.my_agent = agent.AgentClass(age, sex, is_alpha, 
			None, 0, None, [])

	def test_copy(self):
		new_agent = copy(self.my_agent)

		self.assertEqual(self.my_agent.age, new_agent.age)
		self.assertEqual(self.my_agent.sex, new_agent.sex)
		self.assertEqual(self.my_agent.is_alpha, new_agent.is_alpha)

		#alter the age, sex and is_alpha of new_agent
		new_agent.age = 1
		new_agent.sex = "f"
		new_agent.is_alpha = ""

		#check if the other agent has also been affected
		self.assertNotEqual(self.my_agent.age, new_agent.age)
		self.assertNotEqual(self.my_agent.sex, new_agent.sex)
		self.assertNotEqual(self.my_agent.is_alpha, new_agent.is_alpha)


	def test_deep_copy(self):
		first_list = []
		first_list.append(self.my_agent)

		second_list = deepcopy(first_list)

		self.assertEqual(first_list[0].age, second_list[0].age)
		self.assertEqual(first_list[0].sex, second_list[0].sex)
		self.assertEqual(first_list[0].is_alpha, second_list[0].is_alpha)

		#alter the age, sex and is_alpha of new_agent
		second_list[0].age = 1
		second_list[0].sex = "f"
		second_list[0].is_alpha = ""

		#check if the other agent has also been affected
		self.assertNotEqual(first_list[0].age, second_list[0].age)
		self.assertNotEqual(first_list[0].sex, second_list[0].sex)
		self.assertNotEqual(first_list[0].is_alpha, second_list[0].is_alpha)
