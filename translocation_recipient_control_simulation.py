from control_simulation import ControlSimulation
from translocation_table import TranslocationTable
import constants
from random_module import RandomModule
from agent import AgentClass
__metaclass__ = type

class TranslocationRecipientControlSimulation(ControlSimulation):

	INDIVIDUALS_INTRODUCED_PER_GENERATION = 3
	CHANCE_OF_NEW_FEMALE = 0.7
	AGENT_AGE_LOWER_BOUND = 5
	AGENT_AGE_UPPER_BOUND = 30

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
			table_data)

	def conduct_changes_unique_to_experiment_at_gen(self,
		this_generation_population, next_generation_population,
		generation_index, number_of_generations, table_data):
		"""
		since this is a donor population, this simulation will
		add a certain number of new agents per generation to the
		population
		"""
		ControlSimulation.conduct_changes_unique_to_experiment_at_gen(
			self, this_generation_population, next_generation_population,
			generation_index, number_of_generations, table_data)

		random_module = RandomModule()

		#randomly select agent's age by creating a list of 
		#numbers from 1-30, then shuffling it and picking 
		#the 0th element
		agent_age_list = range(self.AGENT_AGE_LOWER_BOUND,
			self.AGENT_AGE_UPPER_BOUND)
		random_module.shuffle(agent_age_list)
		agent_age = agent_age_list[0]

		for i in range(self.INDIVIDUALS_INTRODUCED_PER_GENERATION):
			agent_sex = "m"

			if (random_module.roll(self.CHANCE_OF_NEW_FEMALE)):
				agent_sex = "f"

			new_agent =\
			 AgentClass(agent_age, agent_sex, False, None, None,
				None, 
				next_generation_population.get_new_agent_index())
			if (new_agent.sex == "m"):
				self.add_new_agent_to_population(
					new_agent, table_data, this_generation_population,
					next_generation_population, random_module)

			else:
				assert(new_agent.sex == "f")
				self.add_new_agent_to_population(
					new_agent, table_data, this_generation_population,
					next_generation_population, random_module)


	def add_new_agent_to_population(self, agent, table_data,
		this_generation_population, next_generation_population,
		random_module):
		groups = this_generation_population.groups
		max_group_index = len(groups)
		group_indices = range(0, max_group_index)

		tries = 0
		while (tries < 3):
			#shuffle groups
			random_module.shuffle(group_indices)
			target_group_index = group_indices[0]
			target_group =\
			 this_generation_population.groups[target_group_index]
			females_to_male =\
			 target_group.get_females_to_male()
			chance_of_acceptance =\
			 table_data.dispersal_table.sexed_chance_of_acceptance(
			 	females_to_male, agent.age, agent.sex)
			if (random_module.roll(chance_of_acceptance[tries])):
				next_generation_population.\
				 groups[target_group_index].add_agent(agent)
				return
			else:
				#check if it dies
				if (random_module.roll(chance_of_acceptance[tries+1])):
					return
				else:
					tries += 2




