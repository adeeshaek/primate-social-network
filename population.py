"""	
Macaque Simulation Project

Adeesha Ekanayake 
5/12/2013

population.py
-------------
This class defines a population of several groups

It contains a list. Its main function is 
keeping track of the highest index used to name an agent.
By doing so, it ensures that all agents in a population
have unique indices, which also function as names. The
unique indices are used to construct a graph of each 
stage of the simulation.
"""
import collections
import copy
import json

class Population():
	"""
	contains array containing all the current groups in a 
	population. Also keeps track of the highest used index
	for an agent, in order to keep all agent names in a 
	population unique
	"""
	groups = []
	top_index = 0 #highest agent index in the population
	group_top_index = 1 #highest group index in the pop
	generation = 0

	def __init__(self):
		self.groups = []
		self.top_index = 2
		self.group_top_index = 0

	def __deepcopy__(self, memo):
		new_population = Population()
		new_population.top_index = self.top_index
		new_population.groups = []
		new_population.generation =\
		 self.generation
		for i in range(len(self.groups)):
			new_population.groups.append(copy.deepcopy(self.groups[i]))
			new_population.groups[i].parent_population = new_population
		return new_population

	def add_group(self, new_group):
		"""
		adds a new group into the population
		"""
		new_group.parent_population = self
		self.group_top_index += 1
		new_group.group_index = self.group_top_index

		#go through the group, and increment all indices
		#to the top index
		#then find the new index.
		#the purpose of this is to keep all indexes
		#unique
		self.top_index = new_group.update_indices(self.top_index)
		self.groups.append(new_group)

	def get_new_agent_index(self):
		"""
		gets a unique index for a new agent in the population
		"""
		self.top_index += 1 #pre increment the top_index
		return self.top_index #send the old top_index

	def get_json_string(self):
		"""
		returns a string with a graphical representation of the 
		population in json. This can be visualized using the 
		javascript files.
		"""
		nodes = []
		links = []

		for group in self.groups:
			for agent_index in group.agent_dict:
				agent = group.agent_dict[agent_index]
				agent_json = agent.get_json_name()
				agent_json["group"] = group.group_index
				nodes.append(agent_json)
				links += agent.get_json_links(group)

		return json.dumps({"nodes":nodes, "links":links})


	def get_dot_string(self):
		"""
		returns a string with a graphical representation of the
		population in dot syntax
		"""
		output_string = ""
		output_string = "digraph group {\n"
		output_string += "size=\"20,20\";\n"
		output_string += "layout=\"circo\";\n"
		for group in self.groups:
			output_string += group.get_dot_string()
		output_string += "}"

		return output_string

	def get_population_relationship_stats(self):
		"""
		returns the number of relationships of this pop as a 
		tuple where (parent-child, sisters, aggressive, friends)
		"""
		friendships = 0
		parent_child = 0
		sisters = 0
		aggressive = 0

		for group in self.groups:

			group_stats = group.get_group_relationship_stats()
			parent_child += group_stats[0]
			sisters += group_stats[1]
			aggressive += group_stats[2]
			friendships += group_stats[3]

		return (parent_child, sisters, aggressive, friendships)













