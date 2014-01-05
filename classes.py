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


class LifeTable:
	"""
	defines life-table data.

	container for 2 dictionaries of this structure:
	life_table[age_in_years] = (qx, bx)

	the 2 dictionaries are for males and females. 
	"""

	male_life_table = {}
	female_life_table = {}

class DispersalTable:
	"""
	defines dispersal-table data. **this applies only to males**

	emigration is stored as follows:
	chance_of_emigration[age] = x

	immigration is stored as follows:
	immigration[age] = (chance_of_being_accepted, 
		chance_of_death_if_not_accepted, chance_of_2nd_group_if_surviving,
		chance_of_death_if_not_accepted_for_2nd_time)
	"""
	immigration = [] 
	emigration = []

	def chance_of_emigration(self, females_to_male, age):
		"""
		calculates the chance for a male to emigrate, for the given number
		of females per male

		chance of emigration = 
			likelihood by age * likelihood by number of females

		likelihood by number of females = -0.7F + 2.2, where F=number of females
		for 1 male

		parameters
		----------
		females_to_male: number of females per male in the group
		age: age of the individual

		returns
		-------
		chance of emigration
		"""
		likelihood_by_age = self.immigration[age]

		likelihood_by_number_of_females = -0.7 * females_to_male + 2.2

		likelihood_of_emigration = likelihood_by_age * likelihood_by_number_of_females

		if likelihood_of_emigration < 0:
			likelihood_of_emigration = 0 #any number < 0 is not a valid likelihood

		return likelihood_of_emigration

	def chance_of_acceptance(self, females_to_male, age):
		"""
		calculates the chance for a male of a given age to be accepted
		by a group

		chance of acceptance = 
			likelihood by age * likelihood by number of females

		likelihood by number of females = 














