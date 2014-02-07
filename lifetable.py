import constants

class LifeTable:
	"""
	defines life-table data.

	container for 2 dictionaries of this structure:
	life_table[age_in_years] = (qx, bx)

	the 2 dictionaries are for males and females. 
	"""

	male_life_table = {}
	female_life_table = {}

	def chance_of_death(self, females_to_male, age, sex):
		"""
		returns the probability of an individual dying this year.
		chance_of_death = chance_of_death_by_age * chance_of_death_by_proportion

		for females:
			chance_of_death_by_proportion = 120 - (10 * females_to_male)

		for males:
			chance_of_death_by_proportion = 70 + (10 * females_to_male)

		chance_of_death_by_proportion is always > 0

		parameters
		----------
		females_to_male: the number of females to one male
		age: age in years as integer
		sex: SEX_FEMALE or SEX_MALE
		"""
		age = float(age)
		chance_of_death_by_age = 0
		chance_of_death_by_proportion = 0

		if (age == 31):
			return 1 #always kill 'em if over 30 (Logans run)

		if (sex == "f"):
			chance_of_death_by_age = self.female_life_table[str(age)][0]

			if (age < constants.ADULTHOOD_AGE['f']):
				chance_of_death_by_proportion =\
				 (120 - (10 * females_to_male))/100.0
			else:
				chance_of_death_by_proportion = 1

		else:
			chance_of_death_by_age = self.male_life_table[str(age)][0]

			if (age < constants.ADULTHOOD_AGE['m']):
				chance_of_death_by_proportion =\
				 (70 + (10 * females_to_male))/100.0
			else:
				chance_of_death_by_proportion = 1

		chance_of_death = chance_of_death_by_age * chance_of_death_by_proportion

		return chance_of_death

	def chance_of_birth(self, females_to_male, age):
		"""
		returns the probability that a female will give birth this year. 
		chance_of_birth = chance_of_birth_by_age * chance_of_birth_by_proportion

		chance_of_birth_by_proportion = 120 - (10 * females_to_male)
		"""
		age = float(age)

		chance_of_birth_by_age = self.female_life_table[str(age)][1]

		chance_of_birth_by_proportion = 120 - (10 * females_to_male)

		chance_of_birth = chance_of_birth_by_age * chance_of_birth_by_proportion

		return chance_of_birth














