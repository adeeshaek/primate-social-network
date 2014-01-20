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

	def test_mark_agents_as_friends(self):
		friend_a = self.group.agent_array[5]
		friend_b = self.group.agent_array[6]

		self.mark_agents_as_friends()

		#check that they are aggressive
		self.assertTrue(friend_a in self.group.in_relationships_set)
		self.assertTrue(friend_b in self.group.in_relationships_set)
		self.assertEqual(friend_a.friends[0], friend_b)
		self.assertEqual(friend_b.friends[0], friend_a)		

		self.unmark_agents_as_friends()

	def test_mark_agents_as_aggressive(self):
		male_a = self.group.agent_array[3]
		male_b = self.group.agent_array[4]

		self.mark_agents_as_aggressive()

		#check that they are aggressive
		self.assertTrue(male_a in self.group.in_relationships_set)
		self.assertTrue(male_b in self.group.in_relationships_set)
		self.assertEqual(male_a.aggressive[0], male_b)
		self.assertEqual(male_b.aggressive[0], male_a)		

		self.unmark_agents_as_aggressive()

	def test_mark_agents_as_sisters(self):
		sister_a = self.group.agent_array[5]
		sister_b = self.group.agent_array[6]
		self.mark_agents_as_sisters()

		#check that they are sisters
		self.assertTrue(sister_a in self.group.in_relationships_set)
		self.assertTrue(sister_b in self.group.in_relationships_set)
		self.assertEqual(sister_a.sisters[0], sister_b)
		self.assertEqual(sister_b.sisters[0], sister_a)

		#unmark as sisters 
		self.unmark_agents_as_sisters()

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

	def mark_agents_as_friends(self):
		friend_a = self.group.agent_array[5]
		friend_b = self.group.agent_array[6]
		#mark 5 and 6 as sisters 
		self.group.mark_agents_as_friends(friend_a, friend_b)

	def unmark_agents_as_friends(self):
		friend_a = self.group.agent_array[5]
		friend_b = self.group.agent_array[6]
		friend_a.friends = [] #clear the list of sisters
		friend_b.friends = []
		#remove from set manually
		self.group.in_relationships_set.remove(friend_a) 
		self.group.in_relationships_set.remove(friend_b)

	def mark_agents_as_sisters(self):
		sister_a = self.group.agent_array[5]
		sister_b = self.group.agent_array[6]
		#mark 5 and 6 as sisters 
		self.group.mark_agents_as_sisters(sister_a, sister_b)

	def unmark_agents_as_sisters(self):
		sister_a = self.group.agent_array[5]
		sister_b = self.group.agent_array[6]
		sister_a.sisters = [] #clear the list of sisters
		sister_b.sisters = []
		#remove from set manually
		self.group.in_relationships_set.remove(sister_a) 
		self.group.in_relationships_set.remove(sister_b)

	def mark_agents_as_aggressive(self):
		male_a = self.group.agent_array[3]
		male_b = self.group.agent_array[4]
		#mark 5 and 6 as sisters 
		self.group.mark_agents_as_aggressive(male_a, male_b)

	def unmark_agents_as_aggressive(self):
		male_a = self.group.agent_array[3]
		male_b = self.group.agent_array[4]
		male_a.aggressive = [] #clear the list of sisters
		male_b.aggressive = []
		#remove from set manually
		self.group.in_relationships_set.remove(male_a) 
		self.group.in_relationships_set.remove(male_b)
