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
	group_index = 0
	agent_dict = {} #dictionary of references to group members
	female_set = set()
	male_set = set()
	underage_set = set()
	in_relationships_set = set()
	whole_set = set()

	#aggressive relationships in a group are a chain
	#of relationships, in order of age. The youngest
	#agent is added to this chain as the lowest link.
	#these relationships are represented in an implicit
	#linked list, instead of a traditional linked list
	#because collisions can be very common in this list
	#, since agents can often have the same age
	aggressive_chain_head = None

	#this is a stack of agents who have immigrated
	#but are yet to form aggressive relationships
	#agents only get added here if there are no male
	#agents in the group when they immigrate
	aggressive_relationship_stack = set()
	parent_population = None

	def __init__(self, parent_population):
		self.agent_dict = {}
		self.parent_population = parent_population
		#get the minimum ages from constants.py
		self.FEMALE_MINIMUM_AGE = constants.ADULTHOOD_AGE['f']
		self.MALE_MINIMUM_AGE = constants.ADULTHOOD_AGE['m']

	def __deepcopy__(self, memo):
		"""
		NOTE: parent_population set to none in new copy
		"""
		new_group = AgentGroup(None)
		new_group.agent_dict =\
		 copy.deepcopy(self.agent_dict)
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
		new_group.group_index =\
		 self.group_index
		new_group.aggressive_chain_head =\
		 self.aggressive_chain_head
		new_group.aggressive_relationship_stack =\
		 self.aggressive_relationship_stack
		new_group.parent_population =\
		 self.parent_population
		return new_group

	def clear(self):
		"""
		removes all agents from the group, clearing it
		completely
		"""
		self.female_set = set()
		self.male_set = set()
		self.underage_set = set()
		self.in_relationships_set = set()
		self.whole_set = set()
		self.agent_dict = {}
		aggressive_chain_head = None

	def update_indices(self, top_index):
		"""
		intended to increment all the indices in the 
		group by a set amount, in order to keep all indices 
		in the population unique
		
		returns
		-------
		new top index: the highest index in the group, after
		being incremented
		"""
		current_top_index = top_index
		new_top_index = top_index

		list_of_agents_to_add = []

		for agent_index in self.agent_dict:
			agent = self.agent_dict[agent_index]
			agent.update_indices(top_index)

			if (agent.index > new_top_index):
				new_top_index = agent.index
		
			list_of_agents_to_add.append(agent)

		self.aggressive_chain_head += top_index

		#clear the group and re-add agents
		self.clear()

		for agent in list_of_agents_to_add:
			self.add_agent(agent)

		return new_top_index

	def get_dot_string(self):
		"""
		returns a string with a graphical representation of
		 the group in dot syntax
		"""
		outputstring = ""

		for agent_key in self.whole_set:
			agent = self.agent_dict[agent_key]
			outputstring += agent.get_dot_string(self)
			outputstring += "g" + str(self.group_index) +\
			" -> " + str(agent_key) + " [style=dotted];\n"

		return outputstring

	def get_females_to_male(self):
		"""
		gets the number of females to a single male
		in this group
		"""
		females = len(self.female_set)
		males = len(self.male_set)

		if (males == 0):
			males = 0.00001 #avoid division by 0

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
		agent_index =\
		 self.parent_population.get_new_agent_index()
		child_agent = AgentClass(
			1, child_sex, None, parent_agent.index, None,
			None, agent_index)

		#if agent is young and male, it has to be 
		#marked as 'about to migrate'
		if child_sex == "m":
			child_agent.young_migration = False

		#add the new infant to the group
		group.add_agent(child_agent)
		group.mark_as_parent(parent_agent, child_agent)

		#if child is female, mark sisters
		if (child_sex == "f"):
			children_list = parent_agent.children
			for child_index in children_list:
				child = group.agent_dict[child_index]
				if (child.sex == "f" and child.index != agent_index):
					group.mark_agents_as_sisters(child_agent,
					child)

	def mark_agent_as_dead(self, agent):
		"""
		marks an agent as having died. Since the self.all_agents
		set contains all living agents, by removing the agent
		from this set, you mark him or her as having died

		parameters
		----------
		agent: agent to mark as dead
		"""
		#remove all agent's friends
		self.unmark_agents_friends(agent)

		#remove agent from sexed sets, and don't panic
		#for the same reason as below
		try:
			if (agent.sex == 'm'):
				self.remove_male_from_aggressives(agent)
				self.male_set.remove(agent.index)
				#clear the agent's parent
				#to prevent a relationship from
				#skewing the SNG
				parent_agent = self.agent_dict[
				agent.parent]
				agent.parent = None
				if (parent_agent.children != None):
					parent_agent.children.remove(agent.index)

			else:
				self.female_set.remove(agent.index)
		except KeyError:
			pass

		try:
			self.underage_set.remove(agent.index)
		except:
			pass

		#since this method recursively marks all
		#children as being dead, it can be called 
		#several times for a given agent in a single
		#run. Hence, don't panic if the agent is already
		#dead when the method is called
		marked = False
		try:
			self.whole_set.remove(agent.index)
			self.agent_dict[agent.index]
			marked = True
		except KeyError:
			pass

		"""
		#if agent is a parent and if the child is 
		#still underage, kill the child as well
		for child in agent.children:
			if (child in self.underage_set):
				self.mark_agent_as_dead(
					self.agent_dict[child])
		"""
		return marked

	def mark_as_parent(self, agent, child_or_children):
		"""
		marks an agent as being a parent 
		by marking as being in a relationship and
		adding the child's index to the parent's list
		of childrens

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
			"""
			because males are dispersed from group to group,
			it is possible for a male on the cusp of 
			adulthood to be moved from 1 group to another.
			Therefore, don't panic if key not found
			"""
			try:
				self.underage_set.remove(agent.index)
			except KeyError:
				pass
			self.add_male_to_aggressives(agent)
			self.male_set.add(agent.index)
			agent.age = agent.age + 1

		elif agent.age == (self.FEMALE_MINIMUM_AGE - 1) and agent.sex == "f":
			self.underage_set.remove(agent.index)
			self.female_set.add(agent.index)
			agent.age = agent.age + 1

		else:
			agent.age = agent.age + 1

		if agent.sex == "m":
			agent.last_migration += 1

	def add_agent(self, agent):
		"""
		adds existing agent into the group. This method consolidates
		the adding to agent_dict and sexed_set
		
		parameters
		----------
		agent: agent to add
		"""
		self.agent_dict[agent.index] = agent
		self.whole_set.add(agent.index)

		#first check if female or male
		if (agent.sex == "m"):
			#reset immigration counter
			agent.last_migration = 0

			#these checks do not occur during the 0th gen
			#where adults are added to the group
			if (self.parent_population.generation != 0):

				#if agent is a baby who was just born
				if (agent.age == 1):
					self.underage_set.add(agent.index)

				#if male, check if agent is child or adult
				elif (agent.age < self.MALE_MINIMUM_AGE):
					#since it just entered the group
					#it must form an aggressive rel
					assert(agent.parent == None)
					self.add_male_to_aggressives(agent)
					agent.young_migration = True
					self.underage_set.add(agent.index)

				else:
					#first, get an aggressive relationship
					assert(agent.parent == None)
					self.add_male_to_aggressives(agent)
					#even if aggressive relationship does not get
					#added the male has to be added to the set
					#of adult males
					self.male_set.add(agent.index)

			else: #this concerns the first gen.
				if (agent.age <= self.MALE_MINIMUM_AGE):
					self.underage_set.add(agent.index)

				else:
					self.male_set.add(agent.index)

		else:
			assert(agent.sex == "f")

			#except for the first gen, where adult agents are
			#added to the population from the seed group
			#adult females are NEVER added to a group
			if (self.parent_population.generation != 0):
				assert (agent.age == 1)
				self.underage_set.add(agent.index)

			elif agent.age > self.FEMALE_MINIMUM_AGE:
				self.female_set.add(agent.index)

			else:
				assert (agent.age <= self.FEMALE_MINIMUM_AGE)
				self.underage_set.add(agent.index)


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
		if (agent_a.index in self.whole_set and\
			agent_b.index in self.whole_set):
			agent_a.friends.add(agent_b.index)
			agent_b.friends.add(agent_a.index)
			self.in_relationships_set.add(agent_a.index)
			self.in_relationships_set.add(agent_b.index)
			assert(agent_a.index in agent_b.friends)
			assert(agent_b.index in agent_a.friends)


	def unmark_agents_friends(self, agent):
		"""
		removes all friendships from an agent

		parameters
		----------
		agent: target agent
		"""
		for friend_index in agent.friends:
			friend = self.agent_dict[friend_index]
			try:
				friend.friends.remove(agent.index)
			except:
				#if the friend doesn't recognize you,
				#don't panic
				pass 
		agent.friends = set()
			

	def mark_agents_as_sisters(self, agent_a, agent_b):
		"""
		marks 2 agents as being each other's sisters

		parameters
		----------
		agent_a, agent_b: agents to mark as sisters
		"""
		assert(agent_a != agent_b)
		assert(agent_a.index != agent_b.index)
		agent_a.sisters.append(agent_b.index)
		agent_b.sisters.append(agent_a.index)
		self.in_relationships_set.add(agent_a.index)
		self.in_relationships_set.add(agent_b.index)

	def remove_male_from_aggressives(self, agent):
		"""
		removes the male from this group's chain
		of aggressive relationships. This method is 
		called prior to the male emigrating from the
		group

		parameters
		----------
		agent: target agent
		"""
		#reset the agent's agg_next and agg_prev
		if (self.aggressive_chain_head == agent.index):
			#agent is at head of list
			if (agent.aggressive_next == None):
				#agent is the only male in list
				self.aggressive_chain_head = None

			else:
				#there are others in the list
				list_next_male =\
				self.agent_dict[agent.aggressive_next]
				self.aggressive_chain_head =\
				list_next_male.index
				list_next_male.aggressive_prev = None

		elif (agent.aggressive_prev != None):
			if (agent.aggressive_next == None):
				#agent is at tail of list
				list_prev_male =\
				self.agent_dict[agent.aggressive_prev]
				list_prev_male.aggressive_next = None

			else:
				#agent is the the middle of the list
				list_prev_male =\
				self.agent_dict[agent.aggressive_prev]
 				list_next_male =\
				self.agent_dict[agent.aggressive_next]
				list_next_male.aggressive_prev =\
				list_prev_male.index
				list_prev_male.aggressive_next =\
				list_next_male.index

		agent.aggressive_next = None
		agent.aggressive_prev = None

	def add_male_to_aggressives(self, agent):
		"""
		adds the agent to the chain of aggressive 
		relationships in the group
		
		parameters
		----------
		agent: target agent
		"""
		#make sure the agent has been removed 
		#from the previous group correctly
		assert(agent.aggressive_next == None)
		assert(agent.aggressive_prev == None)
		assert(agent.sex == 'm')

		if (self.aggressive_chain_head == None):
			self.aggressive_chain_head = agent.index

		else:
			#traverse the list until the correct spot is found
			current_list_agent_index = self.aggressive_chain_head
			current_list_agent =\
			 self.agent_dict[current_list_agent_index]

			while (current_list_agent.age < agent.age and\
				current_list_agent.aggressive_next != None):
				current_list_agent_index =\
				 current_list_agent.aggressive_next
				current_list_agent =\
				 self.agent_dict[current_list_agent_index]

			if current_list_agent.aggressive_next == None:
				#tail of list has been reached
				current_list_agent.aggressive_next =\
				 agent.index
				agent.aggressive_prev = current_list_agent.index

			else:
				#insert in middle of list
				agent.aggressive_next =\
				 current_list_agent.aggressive_next
				agent.aggressive_prev = current_list_agent.index

				current_list_agent.aggressive_next =\
				 agent.index
				next_list_agent = self.agent_dict[
				 agent.aggressive_next]
				next_list_agent.aggressive_prev = agent.index

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
		del self.agent_dict
		self.female_set.clear()
		self.male_set.clear()
		self.underage_set.clear() 
		self.in_relationships_set.clear()
		self.whole_set.clear()

