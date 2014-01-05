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

	def chance_of_death(self, females_to_male, agent):
		"""
		returns the probability of an individual dying this year.
		chance_of_death = chance_of_death_by_age * chance_of_death_by_proportion

		for females:
			chance_of_death_by_proportion = 120 - (10 * females_to_male)

		for males:
			chance_of_death_by_proportion = 70 + (10 * females_to_male)

		chance_of_death_by_proportion is always > 0
		"""
		age = agent.age
		chance_of_death_by_age = 0
		chance_of_death_by_proportion = 0

		if (agent.sex = "SEX_FEMALE"):
			chance_of_death_by_age = self.female_life_table[age][0]
			chance_of_death_by_proportion = 120 - (10 * females_to_male)

		else:
			chance_of_death_by_age = self.male_life_table[age][0]
			chance_of_death_by_proportion = 70 + (10 & females_to_male)

		chance_of_death = chance_of_death_by_age * chance_of_death_by_proportion

		return chance_of_death

	def chance_of_birth(self, females_to_male, agent):
		"""
		returns the probability that a female will give birth this year. 
		chance_of_birth = chance_of_birth_by_age * chance_of_birth_by_proportion

		chance_of_birth_by_proportion = 120 - (10 * females_to_male)
		"""
		chance_of_birth_by_age = self.female_life_table[agent.age][1]

		chance_of_birth_by_proportion = 120 - (10 * females_to_male)

		chance_of_birth = chance_of_birth_by_age * chance_of_birth_by_proportion

		return chance_of_birth














