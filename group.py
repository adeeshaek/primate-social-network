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

FEMALE_MINIMUM_AGE = 5
MALE_MINIMUM_AGE = 7

class AgentGroup():
	agent_array = [] #array of references to group members
	female_set = set()
	male_set = set()
	underage_set = set()
	in_relationships_set = set()
	whole_set = set()

	def promote_agent(self, agent):
		"""
		makes an agent older, and if need be, removes them from the
		underage_set
		
		parameters
		----------
		agent: agent to promote
		"""
		if agent.age > MALE_MINIMUM_AGE:
			agent.age = agent.age + 1

		elif agent.age == (MALE_MINIMUM_AGE - 1) and agent.sex == "m":
			self.underage_set.remove(agent)
			self.male_set.add(agent)
			agent.age = agent.age + 1

		elif agent.age == (FEMALE_MINIMUM_AGE - 1) and agent.sex == "f":
			self.underage_set.remove(agent)
			self.female_set.add(agent)
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
		self.whole_set.add(agent)

		if (agent.age < FEMALE_MINIMUM_AGE):
			self.underage_set.add(agent)

		elif (agent.age < MALE_MINIMUM_AGE and agent.sex == "m"):
			self.underage_set.add(agent)

		elif (agent.sex == "m"):
			self.male_set.add(agent)

		else:
			self.female_set.add(agent)

	def remove_agent(self, agent):
		"""
		removes agent from the group. This method consolidates
		the removal
		
		parameters
		----------
		agent: agent to remove
		"""
		self.whole_set.remove(agent)

		if (agent.age < FEMALE_MINIMUM_AGE):
			self.underage_set.remove(agent)

		elif (agent.age < MALE_MINIMUM_AGE and agent.sex == "m"):
			self.underage_set.remove(agent)

		elif (agent in self.male_set):
			self.male_set.remove(agent)

		else:
			self.female_set.remove(agent)

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
			 self.female_set.difference(self.in_relationships_set)
			eligible_females = eligible_females.difference(agent.parent)
			return eligible_females

		else:
			eligible_males =\
			 self.male_set.difference(self.in_relationships_set)
			return eligible_males

	def mark_agents_as_friends(self, agent_a, agent_b):
		"""
		marks 2 agents as being each other's friends

		parameters
		----------
		agent_a, agent_b: agents to mark as friends
		"""
		agent_a.friends.append(agent_b)
		agent_b.friends.append(agent_a)
		self.in_relationships_set.add(agent_a)
		self.in_relationships_set.add(agent_b)

	def mark_agents_as_sisters(self, agent_a, agent_b):
		"""
		marks 2 agents as being each other's sisters

		parameters
		----------
		agent_a, agent_b: agents to mark as sisters
		"""
		agent_a.sisters.append(agent_b)
		agent_b.sisters.append(agent_a)
		self.in_relationships_set.add(agent_a)
		self.in_relationships_set.add(agent_b)

	def mark_agents_as_aggressive(self, agent_a, agent_b):
		"""
		marks two agents as being in aggressive relationship with each
		other

		parameters
		----------
		agent_a, agent_b: agents in aggressive relationship
		"""	
		agent_a.aggressive.append(agent_b)
		agent_b.aggressive.append(agent_a)
		self.in_relationships_set.add(agent_a)
		self.in_relationships_set.add(agent_b)

	def mark_agents_as_having_a_relationship(self, agent):
		"""
		marks an agent as having a relationship. Agents who have
		one of any kind of relationships are ineligible to become
		friends

		parameters
		----------
		agent: the agent whom to mark as having a related_members
		"""
		self.in_relationships_set.add(agent)

		
