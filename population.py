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

class Population():
	"""
	contains array containing all the current groups in a 
	population. Also keeps track of the highest used index
	for an agent, in order to keep all agent names in a 
	population unique
	"""
	groups = []
	top_index = 0
	group_top_index = 0

	def __init__(self):
		self.groups = []
		self.top_index = 0
		self.group_top_index = 0

	def __deepcopy__(self, memo):
		new_population = Population()
		new_population.top_index = self.top_index
		new_population.groups = []
		for i in range(len(self.groups)):
			new_population.groups.append(copy.deepcopy(self.groups[i]))
			new_population.groups[i].parent_population = new_population
		return new_population

	def add_group(self, new_group):
		"""
		adds a new group into the population
		"""
		new_group.parent_population = self
		new_group.group_index = self.group_top_index

		#go through the group, and increment all indices
		#to the top index
		#then find the new index.
		#the purpose of this is to keep all indexes
		#unique
		new_top_index = 0
		current_top_index = self.top_index
		self.top_index = new_group.update_indices(current_top_index)
		self.group_top_index += 1
		self.groups.append(new_group)

	def get_new_agent_index(self):
		"""
		gets a unique index for a new agent in the population
		"""
		self.top_index += 1 #pre increment the top_index
		return self.top_index - 1 #send the old top_index

	def get_dot_string(self):
		"""
		returns a string with a graphical representation of the
		population in dot syntax
		"""
		output_string = ""
		for group in self.groups:
			output_string += group.get_dot_string()

		return output_string


