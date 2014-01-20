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

	def test_add_agent(self):
		underage_male_2 =\
			AgentClass(6, "m", None, 0, [], [], [])#1
		underage_female_2 =\
			AgentClass(4, "f", None, 0, [], [], [])#2
		of_age_male_3 = AgentClass(6, "m", None, 0, [], [], [])

		self.group.add_agent(underage_male_2)
		self.group.add_agent(underage_female_2)
		self.group.add_agent(of_age_male_3)

		self.tracking_dict["UM2"] = underage_male_2
		self.tracking_dict["UF2"] = underage_female_2
		self.tracking_dict["OM3"] = of_age_male_3

		for key in self.tracking_dict:
			self.assertTrue(self.tracking_dict[key] in self.group.whole_set)
	
