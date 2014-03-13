from control_simulation import ControlSimulation

__metaclass__ = type

class TranslocationControlSimulation(ControlSimulation):

	def conduct_changes_unique_to_experiment_at_agent(self,
		this_generation_population, next_generation_population,
		this_generation, new_generation, this_agent, new_agent,
		females_to_male, lifetable, random_module):
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
			females_to_male, lifetable, random_module
			)