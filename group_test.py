import unittest
from group import AgentGroup
from agent import AgentClass

class TestAgentGroup(unittest.TestCase):

	def setUp(self):
		self.group = AgentGroup()
		self.tracking_dict = {} #used to track specific references

		parent = AgentClass(12, "f", "A", None, [], [], [])#0
		underage_male_1 =\
			AgentClass(6, "m", None, 0, [], [], [])#1
		underage_female_1 =\
			AgentClass(4, "f", None, 0, [], [], [])#2
		of_age_male_1 = AgentClass(6, "m", None, 0, [], [], [])#3
		of_age_male_2 = AgentClass(6, "m", None, 0, [], [], [])#4
		of_age_female_1 = AgentClass(6, "m", None, 0, [], [], [])#5
		of_age_female_2 = AgentClass(6, "m", None, 0, [], [], [])#6
		fake_target_male = AgentClass(9, "m", None, 0, [], [], [])#7
		real_target_female = AgentClass(9, "f", None, 0, [], [], [])#8
		focus_male = AgentClass(8, "m", None, 0, [], [], [])#9

		self.group.add_agent(parent)
		self.group.add_agent(underage_male_1)
		self.group.add_agent(underage_female_1)
		self.group.add_agent(of_age_male_1)
		self.group.add_agent(of_age_male_2)
		self.group.add_agent(of_age_female_1)
		self.group.add_agent(of_age_female_2)
		self.group.add_agent(fake_target_male)
		self.group.add_agent(real_target_female)
		self.group.add_agent(focus_male)

	def test_add_and_remove_agent(self):
		self.add_agents()

		for key in self.tracking_dict:
			self.assertTrue
			(self.tracking_dict[key] in self.group.whole_set)

		self.remove_agents()

		for key in self.tracking_dict:
			self.assertTrue
			(self.tracking_dict[key] not in self.group.whole_set)

	def test_promote_agent(self):
		self.add_agents()
		of_age_male = self.tracking_dict["OM3"]
		underage_female = self.tracking_dict["UF2"]
		underage_male = self.tracking_dict["UM2"]

		#promote of age male
		self.group.promote_agent(of_age_male)
		#check age
		self.assertEqual(of_age_male.age, 9)

		#promote underage male and female
		self.group.promote_agent(underage_male)
		self.group.promote_agent(underage_female)

		#check if they are no longer in the underage set
		self.assertFalse(underage_male in self.group.underage_set)
		self.assertFalse(underage_female in self.group.underage_set)

		#check that they are now in the respective sexed sets
		self.assertTrue(underage_male in self.group.male_set)
		self.assertTrue(underage_female in self.group.female_set)

		#check if age has been correctly incremented
		self.assertEqual(underage_female.age, 5)
		self.assertEqual(underage_male.age, 7)

		self.remove_agents()

	def test_mark_agents_as_sisters(self):
		


	def add_agents(self):
		underage_male_2 =\
			AgentClass(6, "m", None, 0, [], [], [])#1
		underage_female_2 =\
			AgentClass(4, "f", None, 0, [], [], [])#2
		of_age_male_3 = AgentClass(8, "m", None, 0, [], [], [])

		self.group.add_agent(underage_male_2)
		self.group.add_agent(underage_female_2)
		self.group.add_agent(of_age_male_3)

		self.tracking_dict["UM2"] = underage_male_2
		self.tracking_dict["UF2"] = underage_female_2
		self.tracking_dict["OM3"] = of_age_male_3

	def remove_agents(self):
		for key in self.tracking_dict:
			agent = self.tracking_dict[key]
			self.group.remove_agent(agent)

	def mark_agents_as_sisters(self):
		agent_a = self.group.agent_array[5]		
		agent_b = self.group.agent_array[6]
		





	
