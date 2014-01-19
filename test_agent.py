import unittest
import agent
from copy import copy

class TestAgent(unittest.TestCase):

	def setUp(self):

		age = 5
		sex = "m"
		is_alpha = "A"
		
		self.my_agent = agent.AgentClass(age, sex, is_alpha, 
			None, None, None, None)

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


