import constants

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
	immigration = {} 
	emigration = {}

	def chance_of_emigration(self, females_to_male, age):
		"""
		calculates the chance for a male to emigrate, for the given number
		of females per male

		parameters
		----------
		females_to_male: proportion of females per male in the group
		age: age of the individual

		returns
		-------
		chance of emigration
		"""
		if age > constants.MAX_AGE:
			return 0

		likelihood_by_age = self.emigration[age]

		likelihood_by_number_of_females = -0.7 * females_to_male + 2.2

		likelihood_of_emigration =\
			likelihood_by_age #* likelihood_by_number_of_females

		if likelihood_of_emigration < 0:
			likelihood_of_emigration = 0 #any number < 0 is not a valid likelihood

		return likelihood_of_emigration

	def sexed_chance_of_acceptance(self, females_to_male, age,
		sex):
		if (sex == "m"):
			return self.chance_of_acceptance(females_to_male, age)

		else:
			assert(sex == "f")
			return (0.85, 0.25, 0.85, 1)

	def chance_of_acceptance(self, females_to_male, age):
		"""
		calculates the chance for a male of a given age to be accepted
		by a group

		chance of acceptance = 
			likelihood by age * likelihood by number of females

		likelihood by number of females = .4 * females_to_male

		parameters
		----------
		females_to_male: proportion of females per male in the group
		age: age of the individual

		returns
		-------
		chance of acceptance
		"""
		likelihood_by_age = (self.immigration[age][0],
			self.immigration[age][1], self.immigration[age][2],
			self.immigration[age][3])

		likelihood_by_number_of_females = females_to_male * 0.4

		#likelihood by age is a 4-tuple, and elements 0 and 2 
		#determine chance of immigration, while elements 1 and 3
		#determine chance of death, respectively. Chance of death
		#is not affected by the number of females in a group

		new_likelihood_by_age_1 =\
			likelihood_by_age[0] * likelihood_by_number_of_females

		new_likelihood_by_age_2 =\
			likelihood_by_age[2] * likelihood_by_number_of_females

		new_likelihood_by_age =\
			(new_likelihood_by_age_1, likelihood_by_age[1],
				new_likelihood_by_age_2, likelihood_by_age[3])

		return new_likelihood_by_age


	