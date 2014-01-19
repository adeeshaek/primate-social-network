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
	number = 0

	def __init__(self, age, sex, is_alpha, parent, sisters, 
		aggressive, friends):
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
		parent - the parent of this individual
		sister - the sister(s) of this individual. Multiple entries separated by
		comma.
		aggressive - aggressive relationships formed by this individual. Binary
		value.
		friendship - friendships formed by this individual. Binary value. Multiple
		entries separated by commas.
		"""
		#make sure age class and sex are valid
		assert (constants.SEX_DICT.has_key(sex))

		self.age = age
		self.sex = sex
		self.is_alpha = is_alpha
		self.parent = parent
		self.sisters = sisters
		self.aggressive = aggressive
		self.friends = friends

	def __str__(self):
		"""
		returns human readable class description
		"""
		output_string = "age:" + str(self.age) +\
			" sex:" + self.sex + " alpha: " + \
			self.is_alpha 

		return output_string

	def __copy__(self):
		new_agent = AgentClass(self.age, self.sex, self.is_alpha, self.parent,
			self.sisters, self.aggressive, self.friends)
		return new_agent

	def __deepcopy__(self, memo):
		return copy.copy(self)




	














