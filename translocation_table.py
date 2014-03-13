

class TranslocationTable():
	"""
	the values for each age is a tuple =
	 (male likelihood, female likelihood)
	"""
	control_translocation_likelihood = {}
	male_biased_translocation_likelihood = {}
	female_biased_translocation_likelihood = {}

	def __str__(self):
		output = ""
		for key in self.control_translocation_likelihood:
			output += str(self.control_translocation_likelihood[key]) +\
			str(self.male_biased_translocation_likelihood[key]) +\
			str(self.female_biased_translocation_likelihood[key]) +\
			"\n"
		return output