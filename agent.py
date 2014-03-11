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
	friends = []
	children = []
	index = 0
	#how many years ago did it last migrate, if male?
	last_migration = 0 
	young_migration = True #whether it has migrated btw 5-6 ys

	#index of the next aggressive relationship
	aggressive_next = None
	aggressive_prev = None

	def __init__(self, age, sex, is_alpha, parent, sisters, 
		friends, index, children=None):
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
		self.friends = friends
		self.index = index
		self.children = children
		self.aggressive_next = None
		self.aggressive_prev = None

		#make sure sisters, aggressive, friends are empty lists not
		#null references
		if self.sisters == None:
			self.sisters = []

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
		if self.parent:
			self.parent += top_index
		children_list = list(self.children)
		for i in range(len(children_list)):
			children_list[i] += top_index
		self.children = set(children_list)
		for i in range(len(self.sisters)):
			self.sisters[i] += top_index
		for i in range(len(self.friends)):
			self.friends[i] += top_index

		if (self.aggressive_next != None):
			self.aggressive_next += top_index

		if (self.aggressive_prev != None):
			self.aggressive_prev += top_index

	def get_dot_string(self, parent_group):
		"""
		returns a string with the agent in dot syntax
		"""
		outputstring = ""

		outputstring += self.get_selfstring() + ";\n"

		for child_index in self.children:
			if (child_index in parent_group.whole_set):
				outputstring += str(self.index) + " -> " +\
				 str(child_index) + "[color=red];\n"

		for sister_index in self.sisters:
			if sister_index in parent_group.whole_set:
				outputstring += str(self.index) + " -> " +\
				 str(sister_index) + "[color=green];\n"

		for friend_index in self.friends:
			if friend_index in parent_group.whole_set:
				outputstring += str(self.index) + " -> " +\
				 str(friend_index) + "[color=orange];\n"

		if (self.aggressive_next != None):
			outputstring += str(self.index) + " -> " +\
			 str(self.aggressive_next) + "[color=blue];\n"

		if (self.aggressive_prev != None):
			outputstring += str(self.index) + " -> " +\
			 str(self.aggressive_prev) + "[color=blue];\n"

		return outputstring

	def get_json_name(self):
		"""
		returns the name of this object in JSON. This 
		is used for visualizing populations in javascript
		"""
		name_dict = {"name":self.index,
		 "age":self.age, "sex":self.sex}

		return name_dict

	def get_json_links(self):
		"""
		returns links relating to this object in JSON.
		Used for visualizing populations in javascript
		"""
		output = []

		for child_index in self.children:
			output_dict = {"source":self.index,
			"target":child_index}
			output.append(output_dict)

		return output

	def __str__(self):
		"""
		returns human readable class description
		"""
		output_string = "age:" + str(self.age) +\
			" sex:" + self.sex + " alpha: " + \
			str(self.is_alpha) + " index: " +\
			str(self.index)

		return output_string

	def edges(self):
		"""
		returns the number of relationships this agent has.
		counts the number of sisters, friends, aggressives,
		children.
		"""
		number_of_edges = len(self.sisters) + len(self.friends) +\
		 + len(self.children)

		if (self.parent != None):
		 number_of_edges += 1

		if (self.aggressive_prev != None):
		 number_of_edges += 1

		if (self.aggressive_next != None):
		 number_of_edges += 1

		return number_of_edges
	















