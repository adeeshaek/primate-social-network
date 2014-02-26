import constants
import copy

class AgentClass:
	"""
	defines an agent (in this case, a toque Macaque) in the Simulation
	"""
	#these values are defined in class seedgenerator. 
	age = 0
	sex = ""
	is_alpha = False
	parent = None
	sisters = []
	aggressive = []
	friends = []
	children = []
	index = 0

	def __init__(self, age, sex, is_alpha, parent, sisters, 
		aggressive, friends, index, children=None):
		"""
		constructor
		-----------
		parameters
		----------
		number - the identification number of the individual in the group
		sex - sex of the individual as defined in constants.py
		age - age of individual in years
		rank - whether or not the individual is the alpha male/female

		relationship-related parameters
		-------------------------------
		parent - the mother of this individual
		sister - the sister(s) of this individual. Multiple entries separated by
		comma.
		aggressive - aggressive relationships formed by this individual. Binary
		value.
		friendship - friendships formed by this individual. Binary value. Multiple
		entries separated by commas.
		index - the index of this agent 
		children - list of indices of this agent's children
		"""
		#make sure age class and sex are valid
		assert (constants.SEX_DICT.has_key(sex))

		self.age = int(age)
		self.sex = sex
		self.is_alpha = is_alpha
		self.parent = parent
		self.sisters = sisters
		self.aggressive = aggressive
		self.friends = friends
		self.index = index
		self.children = children

		#make sure sisters, aggressive, friends are empty lists not
		#null references
		if self.sisters == None:
			self.sisters = []

		if self.aggressive == None:
			self.aggressive = []

		if self.friends == None:
			self.friends = []

		if self.children == None:
			self.children = set()

		#make sure that children is a set
		assert(type(self.children) is set)

	def get_selfstring(self):
		"""
		returns the name of the agent in dot syntax
		"""
		selfstring = ""

		if (self.sex == "m"):
			selfstring = str(self.index)

		else:
			selfstring = str(self.index) + " [shape=box]"

		selfstring += "[label=" + str(self.age) + "]"

		return selfstring

	def update_indices(self, top_index):
		"""
		increments all indices by top_index, to
		keep a unique index for an individual across
		a population
		"""
		self.index += top_index
		children_list = list(self.children)
		for i in range(len(children_list)):
			children_list[i] += top_index
		self.children = set(children_list)
		for i in range(len(self.sisters)):
			self.sisters[i] += top_index
		for i in range(len(self.aggressive)):
			self.aggressive[i] += top_index
		for i in range(len(self.friends)):
			self.friends[i] += top_index

	def get_dot_string(self):
		"""
		returns a string with the agent in dot syntax
		"""
		outputstring = ""

		outputstring += self.get_selfstring() + ";\n"

		for child_index in self.children:
			outputstring += str(self.index) + " -> " +\
			 str(child_index) + "[color=red];\n"

		for sister_index in self.sisters:
			outputstring += str(self.index) + " -> " +\
			 str(sister_index) + "[color=green];\n"

		for aggressive_index in self.aggressive:
			outputstring += str(self.index) + " -> " +\
			 str(aggressive_index) + "[color=blue];\n"

		for friend_index in self.friends:
			outputstring += str(self.index) + " -> " +\
			 str(friend_index) + "[color=orange];\n"

		return outputstring

	def __str__(self):
		"""
		returns human readable class description
		"""
		output_string = "age:" + str(self.age) +\
			" sex:" + self.sex + " alpha: " + \
			str(self.is_alpha) + " index: " +\
			str(self.index)

		return output_string
	"""
	def __copy__(self):
		new_agent = AgentClass(self.age, self.sex, self.is_alpha, self.parent,
			self.sisters, self.aggressive, self.friends)
		return new_agent

	def __deepcopy__(self, memo):
		new_sisters = copy.deepcopy(self.sisters)
		new_friends = copy.deepcopy(self.friends)
		new_aggressive = copy.deepcopy(self.aggressive)
		new_children = copy.deepcopy(self.children)
		new_agent = AgentClass(self.age, self.sex, self.is_alpha, 
			self.parent, new_sisters, new_aggressive, new_friends,
			self.index, new_children)
		return new_agent
	"""

	def edges(self):
		"""
		returns the number of relationships this agent has.
		counts the number of sisters, friends, aggressives,
		children.
		"""
		number_of_edges = len(self.sisters) + len(self.friends) +\
		 len(self.aggressive) + len(self.children)

		return number_of_edges
	















