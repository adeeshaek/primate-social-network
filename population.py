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

class Population():
	"""
	contains array containing all the current groups in a 
	population. Also keeps track of the highest used index
	for an agent, in order to keep all agent names in a 
	population unique
	"""
	groups = []
	top_index = 1

	def __init__(self):
		self.groups = []
		self.top_index = 1

	def add_group(self, new_group):
		"""
		adds a new group into the population
		"""
		self.groups.append(new_group)

	def get_new_agent_index(self):
		"""
		gets a unique index for a new agent in the population
		"""
		self.top_index += 1 #pre increment the top_index
		return self.top_index - 1 #send the old top_index


