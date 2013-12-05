"""
Macaque Simulation Project
Adeesha Ekanayake 
5/12/2013

classes.py
----------
Defines the container classes used, such as the agent class
"""

import constants

class AgentClass:
	"""
	defines an agent (in this case, a toque Macaque) in the Simulation
	"""
	#these values are defined in class seedgenerator. 
	age = 0
	age_class = ""
	sex = ""
	is_alpha = False
	parent = None
	sisters = []
	aggressive = []
	friends = []
	number = 0

	def __init__(self, age, age_class, sex, is_alpha, parent, sisters, 
		aggressive, friends):
		"""
		constructor
		-----------
			parameters
			----------
			number - the identification number of the individual in the group
			ageclass - the ageclass of the individual, as recorded in constants.py
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
		assert (constants.AGECLASS_DICT.has_key(age_class)) 
		assert (constants.SEX_DICT.has_key(sex))

		self.age = age
		self.age_class = age_class
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
		output_string = "age:" + str(self.age) + " age class:" + \
			self.age_class + " sex:" + self.sex + " alpha: " + \
			self.is_alpha 

		return output_string










