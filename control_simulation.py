from simulation import Simulation
from xlwt import Workbook
import data_saver
import constants
import math

class ControlSimulation(Simulation):

	def conduct_changes_unique_to_experiment(self,
		this_generation_population, next_generation_population,
		this_generation, new_generation, this_agent, new_agent,
		females_to_male, lifetable, random_module):
		"""
		this method can be overloaded to add changes unique
		to this simulation
		"""
		self.last_gen_groups = len(next_generation_population.groups)

	def save_age_stats(self, data_list):
		"""
		collates and saves age-related stats.

		parameters
		----------
		data_list: list of lists, each containing the 
			age of each agent in the population for one
			generation
		"""
		output_list = []

		generation = data_list[-1]

		average_age = 0
		standard_deviation_aggregate = 0

		if len(generation) != 0:
			number_of_agents = len(generation)
		else:
			number_of_agents = 0.00001 #avoid div by 0

		#first calculate the average age
		for agent_age in generation:
			average_age += agent_age

		average_age = average_age/number_of_agents

		#now calculate standard dev
		for agent_age in generation:
			standard_deviation_increment =\
			 math.pow((agent_age - average_age), 2)
			standard_deviation_aggregate +=\
			 standard_deviation_increment

		standard_deviation = math.sqrt(
			(standard_deviation_aggregate/number_of_agents)
			)

		self.last_gen_avg_age = average_age
		self.last_gen_sd_age = standard_deviation

	def save_data(self,
	 population_record_list, male_population_record_list,
	 female_population_record_list, age_record_list, 
	 real_birth_rate_list, real_death_rate_list,
	 average_edges_per_agent, 
	 adult_females_per_males_list,
	 group_composition_list):
		"""
		saves output data to a file.

		parameters
		----------
		population_record_list: contains data about age
			in the form of a list of tuples. Each tuple contains
			(average_age, standard_deviation) for a generation
		age_record_list: contains data about population. It is
			a list of integers representing population for a 
			generation
		"""
		self.save_age_stats(age_record_list)
		self.last_gen_population = population_record_list[-1]
		self.last_gen_fpm = adult_females_per_males_list[-1]
		self.last_gen_epa = average_edges_per_agent[-1]

	def per_generation_printout(self, generation_index):
		print self.simulation_index, "of", self.total_simulations, generation_index
