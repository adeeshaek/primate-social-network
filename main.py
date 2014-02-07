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
from counter import Counter

NUMBER_OF_GENERATIONS = 100
NUMBER_OF_SEED_GROUPS = 10

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
	male_population_record_list = []
	female_population_record_list = []

	birth_rate_record_list = []
	death_rate_record_list = []
	real_birth_rate_list = []
	real_death_rate_list = []

	death_counter = Counter() #used to make sure the correct number
	#of deaths occur
	birth_counter = Counter() #used to make sure the correct number 
	#of births take place

	#assign all_groups by creating several copies of the 
	#seed generation
	for i in range(0, NUMBER_OF_SEED_GROUPS):
		all_groups.append(seed_group)
	
	for i in range (0, NUMBER_OF_GENERATIONS):
		print i
		#analytics
		this_age_record = []
		this_population_record = 0
		this_male_population_record = 0
		this_female_population_record = 0
		this_birth_rate_record = []
		this_death_rate_record = []

		#reset counters
		death_counter.reset()
		birth_counter.reset()

		#run the simulation for each sub_group.
		for j in range(0, len(all_groups)):	

			this_generation = all_groups[j]

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

				#check birth_rate
				if this_agent.index in this_generation.female_set:
					chance_of_birth =\
					 lifetable.chance_of_birth(females_to_male, 
					 	this_agent.age)
					this_birth_rate_record.append(chance_of_birth)

				#check death_rate
				this_death_rate_record.append(
					lifetable.chance_of_death(
						females_to_male, this_agent.age,
						this_agent.sex))

				#check for birth
				check_for_birth(this_generation, new_generation,
					this_agent, new_agent, females_to_male,
					agent_index, lifetable, random_module,
					birth_counter, male_population_record_list)

				#check for death
				check_for_death(lifetable, females_to_male, 
					this_agent, new_agent, new_generation,
					random_module, death_counter)

				#check for dispersal

				#check for friendships

				#analytics
				this_age_record.append(this_agent.age)
				this_population_record += 1

				if (this_agent.index in this_generation.male_set):
					this_male_population_record += 1
				elif (this_agent.index in this_generation.female_set):
					this_female_population_record += 1

			#set the old gen to the new one
			del(this_generation)
			all_groups[j] = new_generation

		real_death_rate_list.append(
			float(death_counter.getCount())/this_population_record)
		real_birth_rate_list.append(
			float(birth_counter.getCount())/this_population_record)
		age_record_list.append(this_age_record)
		male_population_record_list.append(this_male_population_record)
		female_population_record_list.append(
			this_female_population_record)
		population_record_list.append(this_population_record)

		average_birth_rate = 0
		for i in range(0, len(this_birth_rate_record)):
			average_birth_rate += this_birth_rate_record[i]
		average_birth_rate = average_birth_rate / len(this_birth_rate_record)

		average_death_rate = 0
		for i in range(0, len(this_death_rate_record)):
			average_death_rate += this_death_rate_record[i]
		average_death_rate = average_death_rate / len(this_death_rate_record)
		death_rate_record_list.append(average_death_rate)
		birth_rate_record_list.append(average_birth_rate)

	save_data(population_record_list, male_population_record_list,
	 female_population_record_list, age_record_list, 
	 birth_rate_record_list, death_rate_record_list,
	 real_birth_rate_list, real_death_rate_list)


	print birth_counter.getCount()
	print death_counter.getCount()

def save_data(population_record_list, male_population_record_list,
 female_population_record_list, age_record_list, average_birth_rate,
 average_death_rate, real_birth_rate_list, real_death_rate_list):
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
	book = Workbook()
	save_age_stats(age_record_list, book)
	data_saver.save_number_of_indivs(population_record_list, 
		male_population_record_list, female_population_record_list,
		average_birth_rate, average_death_rate, 
		real_birth_rate_list, real_death_rate_list, book)
	output_directory =\
	 constants.OUTPUT_FOLDER + "output_data.xls"
	book.save(output_directory)

def check_for_death(lifetable, females_to_male, this_agent,
	new_agent, new_generation, random_module, counter):
	"""
	checks if an agent should die by getting the probability
	from the lifetable, then performing a dieroll for that
	probability. If true is returned, the agent in the 
	new_generation is marked as being dead

	parameters
	----------
	
	"""
	chance_of_death = lifetable.chance_of_death(
		females_to_male, this_agent.age, this_agent.sex)
	if (random_module.roll(chance_of_death)):
		if(
		new_generation.mark_agent_as_dead(new_agent)
		):
			counter.increment()

def check_for_birth(
	this_generation, new_generation, this_agent, new_agent,
	females_to_male, agent_index, lifetable, random_module, 
	counter, male_population_record_list):
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
			counter.increment()

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