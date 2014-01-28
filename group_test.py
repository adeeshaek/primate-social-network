import unittest
from group import AgentGroup
from agent import AgentClass

class TestAgentGroup(unittest.TestCase):

	def setUp(self):
		self.group = AgentGroup()
		self.tracking_dict = {} #used to track specific references

		parent = AgentClass(12, "f", "A", None, [], [], [])#1
		underage_male_1 =\
			AgentClass(6, "m", None, 1, [], [], [])#2
		underage_female_1 =\
			AgentClass(4, "f", None, 1, [], [], [])#3
		of_age_male_1 = AgentClass(6, "m", None, 1, [], [], [])#4
		of_age_male_2 = AgentClass(6, "m", None, 1, [], [], [])#5
		of_age_female_1 = AgentClass(6, "f", None, 1, [], [], [])#6
		of_age_female_2 = AgentClass(6, "f", None, 1, [], [], [])#7
		focus_male = AgentClass(8, "m", None, 1, [], [], [])#8
		focus_female = AgentClass(8, "f", None, 1, [], [], [])#9

		self.group.add_agent(parent)
		self.group.add_agent(underage_male_1)
		self.group.add_agent(underage_female_1)
		self.group.add_agent(of_age_male_1)
		self.group.add_agent(of_age_male_2)
		self.group.add_agent(of_age_female_1)
		self.group.add_agent(of_age_female_2)
		self.group.add_agent(focus_male)
		self.group.add_agent(focus_female)
		self.group.mark_as_parent(parent)

	def tearDown(self):
		#if not for this snipppet, the group will not clear itself
		#del self.group.agent_array[0:len(self.group.agent_array)]
		del self.group

	def test_kill_agent(self):
		self.add_agents()
		underage_male = self.tracking_dict["UM2"]
		self.group.mark_agent_as_dead(underage_male)

		found = underage_male in self.group.whole_set
		self.assertFalse(found)
		self.group.add_agent(underage_male)
		self.remove_agents()

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

	def test_get_unrelated_members_of_age(self):
		self.mark_agents_as_friends()
		self.mark_agents_as_aggressive()
		self.mark_agents_as_sisters()
		focus_male = self.group.agent_array[8]
		focus_female = self.group.agent_array[9]

		male_agents_friends =\
		 list(self.group.get_unrelated_members_of_age(focus_male))

		female_agents_friends =\
		 list(self.group.get_unrelated_members_of_age(focus_female))

		self.assertEqual(len(male_agents_friends), 1)
		self.assertEqual(len(female_agents_friends), 1)
		self.assertEqual(male_agents_friends[0], focus_female)
		self.assertEqual(female_agents_friends[0], focus_male)

		self.unmark_agents_as_friends()
		self.unmark_agents_as_aggressive()

	def test_mark_agents_as_friends(self):
		friend_a = self.group.agent_array[6]
		friend_b = self.group.agent_array[7]

		self.mark_agents_as_friends()

		#check that they are friends
		self.assertTrue(friend_a in self.group.in_relationships_set)
		self.assertTrue(friend_b in self.group.in_relationships_set)
		self.assertEqual(friend_a.friends[0], friend_b)
		self.assertEqual(friend_b.friends[0], friend_a)		

		self.unmark_agents_as_friends()

	def test_mark_agents_as_aggressive(self):
		male_a = self.group.agent_array[4]
		male_b = self.group.agent_array[5]

		self.mark_agents_as_aggressive()

		#check that they are aggressive
		self.assertTrue(male_a in self.group.in_relationships_set)
		self.assertTrue(male_b in self.group.in_relationships_set)
		self.assertEqual(male_a.aggressive[0], male_b)
		self.assertEqual(male_b.aggressive[0], male_a)		

		self.unmark_agents_as_aggressive()

	def test_mark_agents_as_sisters(self):
		sister_a = self.group.agent_array[6]
		sister_b = self.group.agent_array[7]
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
			AgentClass(6, "m", None, 1, [], [], [])#1
		underage_female_2 =\
			AgentClass(4, "f", None, 1, [], [], [])#2
		of_age_male_3 = AgentClass(8, "m", None, 1, [], [], [])

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
		friend_a = self.group.agent_array[6]
		friend_b = self.group.agent_array[7]
		#mark 5 and 6 as sisters 
		self.group.mark_agents_as_friends(friend_a, friend_b)

	def unmark_agents_as_friends(self):
		friend_a = self.group.agent_array[6]
		friend_b = self.group.agent_array[7]
		friend_a.friends = [] #clear the list of sisters
		friend_b.friends = []
		#remove from set manually
		self.group.in_relationships_set.remove(friend_a) 
		self.group.in_relationships_set.remove(friend_b)

	def mark_agents_as_sisters(self):
		sister_a = self.group.agent_array[6]
		sister_b = self.group.agent_array[7]
		#mark 5 and 6 as sisters 
		self.group.mark_agents_as_sisters(sister_a, sister_b)

	def unmark_agents_as_sisters(self):
		sister_a = self.group.agent_array[6]
		sister_b = self.group.agent_array[7]
		sister_a.sisters = [] #clear the list of sisters
		sister_b.sisters = []
		#remove from set manually
		self.group.in_relationships_set.remove(sister_a) 
		self.group.in_relationships_set.remove(sister_b)

	def mark_agents_as_aggressive(self):
		male_a = self.group.agent_array[4]
		male_b = self.group.agent_array[5]
		#mark 5 and 6 as sisters 
		self.group.mark_agents_as_aggressive(male_a, male_b)

	def unmark_agents_as_aggressive(self):
		male_a = self.group.agent_array[4]
		male_b = self.group.agent_array[5]
		male_a.aggressive = [] #clear the list of sisters
		male_b.aggressive = []
		#remove from set manually
		self.group.in_relationships_set.remove(male_a) 
		self.group.in_relationships_set.remove(male_b)

if __name__ == '__main__':
	unittest.main()
