"""	
Macaque Simulation Project
Adeesha Ekanayake 
5/12/2013

main.py
-------
Main run loop

To do:
* Convert single group into several groups. [x]
* Add analytics 
	- Age: Avg, StdD
	- Edges per individual: Avg, StdD
* When parent dies, kill child of that parent if 
	below a target age [x]
* Group fission and death
* Consider dispersal
* Consider adding and removing new friendships
* Removing friendships?
"""

from agent import AgentClass
from group import AgentGroup
from lifetable import LifeTable
import seed
import copy
import loader
from random_module import RandomModule
import math
import data_saver
from xlwt import Workbook
import constants

NUMBER_OF_GENERATIONS = 100
NUMBER_OF_SEED_GROUPS = 5

def main():
	#import Seed and lifetable data
	seed_group = seed.load_group()
	table_data = loader.load_data()
	lifetable = table_data.life_table
	dispersal_table =\
	 table_data.dispersal_table
	random_module = RandomModule()

	all_groups = []
	this_generation = None
	new_generation = None

	#create analytics lists
	age_record_list = []
	population_record_list = []

	#assign all_groups by creating several copies of the 
	#seed generation
	for i in range(0, NUMBER_OF_SEED_GROUPS):
		all_groups.append(seed_group)
	
	for i in range (0, NUMBER_OF_GENERATIONS):

		#analytics
		this_age_record = []
		this_population_record = 0

		#run the simulation for each sub_group.
		for i in range(0, len(all_groups)):	
			this_generation = all_groups[i]

			females_to_male =\
			 this_generation.get_females_to_male()

			#copy the group 
			new_generation = copy.deepcopy(this_generation)

			for agent_index in this_generation.whole_set:
				this_agent =\
				 this_generation.agent_array[agent_index]
				new_agent =\
				 new_generation.agent_array[agent_index]

				#increment age
				new_generation.promote_agent(new_agent)

				#check for birth
				check_for_birth(this_generation, new_generation,
					this_agent, new_agent, females_to_male,
					agent_index, lifetable, random_module)

				#check for death
				check_for_death(lifetable, females_to_male, 
					this_agent, new_agent, new_generation,
					random_module)

				#check for dispersal

				#check for friendships

				#analytics
				this_age_record.append(this_agent.age)
				this_population_record += 1

			#set the old gen to the new one
			"""
			Assignment not working
			"""
			del(this_generation)
			all_groups[i] = new_generation
			if (i == NUMBER_OF_GENERATIONS - 1):
				#print the new generation
				for agent_index in new_generation.whole_set:
					print this_generation.agent_array[agent_index]

		age_record_list.append(this_age_record)
		population_record_list.append(this_population_record)

	book = Workbook()
	save_age_stats(age_record_list, book)
	data_saver.save_number_of_indivs(population_record_list, 
		book)
	output_directory =\
	 constants.OUTPUT_FOLDER + "output_data.xls"
	book.save(output_directory)

def check_for_death(lifetable, females_to_male, this_agent,
	new_agent, new_generation, random_module):
	"""
	checks if an agent should die by getting the probability
	from the lifetable, then performing a dieroll for that
	probability. If true is returned, the agent in the 
	new_generation is marked as being dead
	"""
	chance_of_death = lifetable.chance_of_death(
		females_to_male, this_agent.age, this_agent.sex)

	if (random_module.roll(chance_of_death)):
		new_generation.mark_agent_as_dead(new_agent)

def check_for_birth(
	this_generation, new_generation, this_agent, new_agent,
	females_to_male, agent_index, lifetable, random_module):
	"""
	checks if an agent is about to give birth, by getting the
	probability of giving birth from the lifetable. If so, performs
	a die roll. If die roll returns true, then the newborn is added
	to the group

	parameters
	----------
	this_generation:
	new_generation:
	this_agent:
	new_agent:
	females_to_male:
	agent_index:
	lifetable:
	random_module:

	properties modified
	-------------------
	new_generation: if newborn added
	new_agent: marked as parent if newborn added 
	"""
	#check for birth
	if (agent_index in this_generation.female_set):
		chance_of_giving_birth =\
		 lifetable.chance_of_birth(
		 	females_to_male, this_agent.age)

		#do a die roll
		if (random_module.roll(chance_of_giving_birth)):
			new_generation.give_birth_to_agent(
				new_agent, random_module, new_generation)

def save_age_stats(data_list, book):
	"""
	collates and saves age-related stats.

	parameters
	----------
	data_list: list of lists, each containing the 
		age of each agent in the population for one
		generation
	"""
	output_list = []

	for generation in data_list:
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

		output_list.append((average_age, standard_deviation))

	#save the average age
	data_saver.save_age_data(output_list, book)

if __name__ == '__main__':
	main()