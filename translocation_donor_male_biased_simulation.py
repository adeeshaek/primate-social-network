from control_simulation import ControlSimulation
from translocation_table import TranslocationTable
import constants
__metaclass__ = type

class TranslocationDonorMaleBiasedSimulation(ControlSimulation):

	def conduct_changes_unique_to_experiment_at_agent(self,
		this_generation_population, next_generation_population,
		this_generation, new_generation, this_agent, new_agent,
		females_to_male, lifetable, random_module, table_data):
		"""
		this method can be overloaded to add changes unique
		to this simulation
		"""
		ControlSimulation.conduct_changes_unique_to_experiment_at_agent(
			self,
			this_generation_population, 
			next_generation_population,
			this_generation, new_generation, 
			this_agent, new_agent,
			females_to_male, lifetable, random_module,
			table_data
			)

		probability_of_translocation = 0.0

		#remove the adult based on the translocation table
		if (this_agent.sex == "m"):
			if (this_agent.age > constants.ADULTHOOD_AGE['m']):
				probability_of_translocation =\
				 table_data.translocation_table.\
				 male_biased_translocation_likelihood[this_agent.age][0]

		else:
			assert(this_agent.sex == "f")
			if (this_agent.age > constants.ADULTHOOD_AGE['f']):
				probability_of_translocation =\
				table_data.translocation_table.\
				male_biased_translocation_likelihood[this_agent.age][1]

		if (random_module.roll(probability_of_translocation)):
			new_generation.mark_agent_as_dead(new_agent)