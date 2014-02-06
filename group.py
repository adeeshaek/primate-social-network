"""
Macaque Simulation Project
Adeesha Ekanayake 
19/1/2014

group.py
--------
represents a group of agents. Refers to the agents using an array,
but also maintains set structure for set operations

NOTE: Throughout this method it is assumed that 
	FEMALE_MINIMUM_AGE < MALE_MINIMUM_AGE
"""

from agent import AgentClass
import copy
import constants

class AgentGroup():
	agent_array = [] #array of references to group members
	female_set = set()
	male_set = set()
	underage_set = set()
	in_relationships_set = set()
	whole_set = set()

	def __init__(self):
		self.agent_array = []
		#ensures the array can be accessed in order
		self.agent_array.append(None)

		#get the minimum ages from constants.py
		self.FEMALE_MINIMUM_AGE = constants.ADULTHOOD_AGE['f']
		self.MALE_MINIMUM_AGE = constants.ADULTHOOD_AGE['m']

	def __deepcopy__(self, memo):
		new_group = AgentGroup()
		new_group.agent_array =\
		 copy.deepcopy(self.agent_array)
		new_group.female_set =\
		 copy.deepcopy(self.female_set)
		new_group.male_set =\
		 copy.deepcopy(self.male_set)
		new_group.underage_set =\
		 copy.deepcopy(self.underage_set)
		new_group.in_relationships_set =\
		 copy.deepcopy(self.in_relationships_set)
		new_group.whole_set =\
		 copy.deepcopy(self.whole_set)
		return new_group

	def get_females_to_male(self):
		"""
		gets the number of females to a single male
		in this group
		"""
		females = len(self.female_set)
		males = len(self.male_set)
		females_to_male = int(females/males)

		return females_to_male

	def give_birth_to_agent(
		self, parent_agent, random_module, 
		group):
		"""
		makes a female agent into a parent, by generating a 
		new infant, and marking the parent_agent as a parent

		parameters
		----------
		parent_agent: agent who is about to give birth
		random_module: used to generate randomness
		group: group to add the new child into
		"""
		#make sure that parent is female
		assert parent_agent.sex == "f"

		#generate a new infant
		PROBABILITY_OF_MALE = 0.5
		child_sex = "f"
		if (random_module.roll(PROBABILITY_OF_MALE)):
			child_sex = "m"
		agent_index = len(group.agent_array)
		child_agent = AgentClass(
			1, child_sex, None, parent_agent.index, None,
			None, None, agent_index)

		#add the new infant to the group
		group.add_agent(child_agent)

	def mark_agent_as_dead(self, agent):
		"""
		marks an agent as having died. Since the self.all_agents
		set contains all living agents, by removing the agent
		from this set, you mark him or her as having died

		parameters
		----------
		agent: agent to mark as dead
		"""
		#since this method recursively marks all
		#children as being dead, it can be called 
		#several times for a given agent in a single
		#run. Hence, don't panic if the agent is already
		#dead when the method is called
		marked = False
		try:
			self.whole_set.remove(agent.index)
			marked = True
		except KeyError:
			pass

		#if agent is a parent and if the child is 
		#still underage, kill the child as well
		"""
		for child in agent.children:
			if (child in self.underage_set):
				self.mark_agent_as_dead(
					self.agent_array[child])
		"""
		return marked

	def mark_as_parent(self, agent, child_or_children):
		"""
		marks an agent as being a parent 
		by marking as being in a relationship and
		adding the child's index to the parent's list
		of children

		parameters
		----------
		agent: agent to mark as being a parent
		child_or_children: agent to mark as child,
		 or list of indices representing children
		"""
		self.mark_as_in_relationship(agent.index)

		#make sure the child or children don't already
		#have a parent
		#duck typing!
		try:
			agent.chidren = agent.children.union(
				child_or_children)

		except TypeError:
			agent.children.add(child_or_children.index)

	def mark_as_in_relationship(self, agent):
		"""
		marks an agent as being in a relationship, 
		by moving it to the in_relationships_set

		parameters
		----------
		agent: agent to mark as being in a relationship
		"""
		self.in_relationships_set.add(agent)

	def promote_agent(self, agent):
		"""
		makes an agent older, and if need be, removes them from the
		underage_set
		
		parameters
		----------
		agent: agent to promote
		"""
		if agent.age > self.MALE_MINIMUM_AGE:
			agent.age = agent.age + 1

		elif agent.age == (self.MALE_MINIMUM_AGE - 1) and agent.sex == "m":
			self.underage_set.remove(agent.index)
			self.male_set.add(agent.index)
			agent.age = agent.age + 1

		elif agent.age == (self.FEMALE_MINIMUM_AGE - 1) and agent.sex == "f":
			self.underage_set.remove(agent.index)
			self.female_set.add(agent.index)
			agent.age = agent.age + 1

	def add_agent(self, agent):
		"""
		adds a new agent into the group. This method consolidates
		the adding to agent_array and sexed_set
		
		parameters
		----------
		agent: agent to add
		"""
		self.agent_array.append(agent)
		self.whole_set.add(agent.index)

		if (agent.age < self.FEMALE_MINIMUM_AGE):
			self.underage_set.add(agent.index)

		elif (
			agent.age < self.MALE_MINIMUM_AGE and agent.sex == "m"):
			self.underage_set.add(agent.index)

		elif (agent.sex == "m"):
			self.male_set.add(agent.index)

		else:
			self.female_set.add(agent.index)

	def remove_agent(self, agent):
		"""
		removes agent from the group. This method consolidates
		the removal
		
		parameters
		----------
		agent: agent to remove
		"""
		self.whole_set.remove(agent.index)

		if (agent.age < self.FEMALE_MINIMUM_AGE):
			self.underage_set.remove(agent.index)

		elif (agent.age < self.MALE_MINIMUM_AGE and agent.sex == "m"):
			self.underage_set.remove(agent.index)

		elif (agent.index in self.male_set):
			self.male_set.remove(agent.index)

		else:
			self.female_set.remove(agent.index)

	def get_unrelated_members_of_age(self, agent):
		"""
		returns members of the set who are unrelated and are
		not underage

		parameters
		----------
		agent: the one whose unrelated members are sought

		returns
		-------
		list of unrelated members, or [] if there are none
		"""
		#note that underage members are not in the sexed sets
		#first check if agent is male or female
		if (agent.sex == "m"):
			eligible_females =\
			 self.female_set.difference(
			 	self.in_relationships_set)
			return eligible_females

		else:
			eligible_males =\
			 self.male_set.difference(
			 	self.in_relationships_set)
			return eligible_males

	def mark_agents_as_friends(self, agent_a, agent_b):
		"""
		marks 2 agents as being each other's friends

		parameters
		----------
		agent_a, agent_b: agents to mark as friends
		"""
		agent_a.friends.append(agent_b.index)
		agent_b.friends.append(agent_a.index)
		self.in_relationships_set.add(agent_a.index)
		self.in_relationships_set.add(agent_b.index)

	def mark_agents_as_sisters(self, agent_a, agent_b):
		"""
		marks 2 agents as being each other's sisters

		parameters
		----------
		agent_a, agent_b: agents to mark as sisters
		"""
		agent_a.sisters.append(agent_b.index)
		agent_b.sisters.append(agent_a.index)
		self.in_relationships_set.add(agent_a.index)
		self.in_relationships_set.add(agent_b.index)

	def mark_agents_as_aggressive(self, agent_a, agent_b):
		"""
		marks two agents as being in aggressive relationship with each
		other

		parameters
		----------
		agent_a, agent_b: agents in aggressive relationship
		"""	
		agent_a.aggressive.append(agent_b.index)
		agent_b.aggressive.append(agent_a.index)
		self.in_relationships_set.add(agent_a.index)
		self.in_relationships_set.add(agent_b.index)

	def mark_agents_as_having_a_relationship(self, agent):
		"""
		marks an agent as having a relationship. Agents who have
		one of any kind of relationships are ineligible to become
		friends

		parameters
		----------
		agent: the agent whom to mark as having a related_members
		"""
		self.in_relationships_set.add(agent.index)

	def __del__(self):
		del self.agent_array[0:len(self.agent_array)]
		self.female_set.clear()
		self.male_set.clear()
		self.underage_set.clear() 
		self.in_relationships_set.clear()
		self.whole_set.clear()

