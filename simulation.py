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
from population import Population
import friendships
import seed
import copy
import loader
from random_module import RandomModule
import math
import data_saver
from xlwt import Workbook
import constants
from counter import Counter

NUMBER_OF_GENERATIONS = 50
NUMBER_OF_SEED_GROUPS = 10

def main():
	simulation = Simulation()
	simulation.run_simulation()

class Simulation:
	"""
	defines a single simulation, with a given set of activities
	taking place in a generation
	"""

	output_xls_name = ""
	dot_directory = ""
	json_directory = ""

	def __init__(self, output_xls_name="output_data.xls",
	 dot_directory="dot/", json_directory="json/"):
		"""
		constructor

		parameters
		----------
		output_xls_name: name of output excel file
		dot_directory: directory in which dot files are saved
		"""
		self.output_xls_name = output_xls_name
		self.dot_directory = dot_directory
		self.json_directory = json_directory

	def run_simulation(self, save_to_dot=True, save_to_json=True):
		#import Seed and lifetable data
		this_generation_population = Population()
		next_generation_population = None

		seed_group = seed.load_group(this_generation_population)
		table_data = loader.load_data()
		lifetable = table_data.life_table
		dispersal_table =\
		 table_data.dispersal_table
		random_module = RandomModule()

		#create analytics lists
		age_record_list = []
		population_record_list = []
		male_population_record_list = []
		female_population_record_list = []

		real_birth_rate_list = []
		real_death_rate_list = []

		edges_per_agent_list = []
		adult_males_list = []
		adult_females_list = []
		adult_females_per_males_list = []

		group_composition_list = []

		death_counter = Counter() #used to make sure the correct number
		#of deaths occur
		birth_counter = Counter() #used to make sure the correct number 
		#of births take place

		#assign all_groups by creating several copies of the 
		#seed generation
		for i in range(0, NUMBER_OF_SEED_GROUPS + 1):
			this_generation_population.add_group(copy.deepcopy(seed_group))
		
		"""
		I was having a strange error where the 0th group 
		was loaded incorrectly. This is a temporary fix

		"""
		del this_generation_population.groups[0]

		for i in range (0, NUMBER_OF_GENERATIONS):
			self.per_generation_printout(i)
			#analytics
			this_age_record = []
			this_population_record = 0
			this_male_population_record = 0
			this_female_population_record = 0
			this_edges_per_agent = 0
			this_generation_adult_males = 0
			this_generation_adult_females = 0
			this_generation_group_composition_list = []

			#reset counters
			death_counter.reset()
			birth_counter.reset()

			#make the next gen population a copy of this gen's pop
			this_generation_population.generation = i

			next_generation_population =\
			 copy.deepcopy(this_generation_population)

			#run the simulation for each sub_group.
			for j in range(0, len(this_generation_population.groups)):	
				this_generation = this_generation_population.groups[j]
				new_generation = next_generation_population.groups[j]

				females_to_male =\
				 this_generation.get_females_to_male()

				for agent_index in this_generation.whole_set:
					#print str(agent_index) + ", " + str(len(this_generation.agent_array))

					this_agent =\
					 this_generation.agent_dict[agent_index]
					new_agent =\
					 new_generation.agent_dict[agent_index]

					#increment age
					new_generation.promote_agent(new_agent)

					#check birth_rate
					if this_agent.index in this_generation.female_set:
						chance_of_birth =\
						 lifetable.chance_of_birth(females_to_male, 
						 	this_agent.age)

					#check for birth
					self.check_for_birth(this_generation, new_generation,
						this_agent, new_agent, females_to_male,
						agent_index, lifetable, random_module,
						birth_counter, male_population_record_list)

					#check for death
					self.check_for_death(lifetable, females_to_male, 
						this_agent, new_agent, new_generation,
						random_module, death_counter)

					#check for dispersal
					self.check_for_dispersal(dispersal_table, females_to_male,
						this_agent, new_agent, this_generation,
						new_generation,
						this_generation_population, 
						next_generation_population, random_module)

					#check for friendships
					friendships.check_for_friendships(this_agent,
						new_agent, this_generation, new_generation,
						random_module)

					#unique changes
					self.conduct_changes_unique_to_experiment_at_agent(
						this_generation_population, 
						next_generation_population,
						this_generation, new_generation, this_agent, 
						new_agent, females_to_male, lifetable, 
						random_module
						)

					#analytics
					this_edges_per_agent += this_agent.edges()

					this_age_record.append(this_agent.age)
					this_population_record += 1

					if (this_agent.index in this_generation.male_set):
						this_male_population_record += 1
					elif (this_agent.index in this_generation.female_set):
						this_female_population_record += 1

				this_generation_adult_males +=\
				 len(this_generation.male_set)
				this_generation_adult_females +=\
				 len(this_generation.female_set)

				this_generation_group_composition_list.append(
					len(this_generation.whole_set)
					)

			self.conduct_changes_unique_to_experiment_at_gen(
				this_generation_population, next_generation_population)

			#set the old gen to the new one
			this_generation_population = next_generation_population

			group_composition_list.append(this_generation_group_composition_list)

			number_of_groups = len(this_generation_population.groups)

			adult_males_per_group =\
			 this_generation_adult_males/number_of_groups
			adult_females_per_group =\
			 this_generation_adult_females/number_of_groups
			adult_males_list.append(adult_males_per_group)
			adult_females_list.append(adult_females_per_group)
			if (adult_males_per_group == 0):
				adult_males_per_group = 0.0000001
			if (adult_females_per_group == 0):
				adult_females_per_group = 0.0000001

			adult_females_per_males_list.append(
				adult_females_per_group/adult_males_per_group
				)

			if (save_to_dot):
				self.save_data_to_dot(this_generation_population.get_dot_string(), i)
			if (save_to_json):
				self.save_data_to_json(this_generation_population.get_json_string(), i)

			average_edges_per_agent =\
			 float(this_edges_per_agent)/this_population_record
			edges_per_agent_list.append(average_edges_per_agent)

			real_death_rate_list.append(
				float(death_counter.getCount())/this_population_record)
			real_birth_rate_list.append(
				float(birth_counter.getCount())/this_population_record)
			age_record_list.append(this_age_record)
			male_population_record_list.append(this_male_population_record)
			female_population_record_list.append(
				this_female_population_record)
			population_record_list.append(this_population_record)

		self.save_data(population_record_list, male_population_record_list,
		 female_population_record_list, age_record_list, 
		 real_birth_rate_list, real_death_rate_list,
		 edges_per_agent_list,
		 adult_females_per_males_list,
		 group_composition_list)

		print (birth_counter.getCount())
		print (death_counter.getCount())

	def per_generation_printout(self, generation_index):
		print generation_index

	def conduct_changes_unique_to_experiment_at_gen(self,
		this_generation_population, next_generation_population):
		"""
		this method can be overloaded to add changes unique
		to the simulation
		"""
		pass

	def conduct_changes_unique_to_experiment_at_agent(self,
		this_generation_population, next_generation_population,
		this_generation, new_generation, this_agent, new_agent,
		females_to_male, lifetable, random_module):
		"""
		this method can be overloaded to add changes unique
		to this simulation
		"""
		pass

	def check_for_death(self, lifetable, females_to_male, this_agent,
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

	def check_for_birth(self,
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

	def check_for_dispersal(self, dispersal_table, females_to_male,
		this_agent, new_agent, this_generation, new_generation,
	 	this_generation_population,
	 	next_generation_population, random_module):
		"""
		checks if this agent is due to be ejected from his group
		and established in a new one by determining the probability
		of dispersal using the dispersal table, then tossing a coin
		with that chance. If the 'coin-toss' comes up heads, the 
		simulation ejects the male from this group. 

		In the wild, males emigrate once between the ages of 4 and
		6, and approximately once every 5 years after they reach 
		adulthood.

		In order to simulate this, the simulation first checks if 
		the agent is a child. If the agent is a child who has not
		migrated yet, the probability of emigration is then determined
		and a coin is tossed to check for emigration. Once the child
		is determined to be emigrating in this year, a counter is 
		started, which measures the number of years since the last 
		time the agent has migrated. Once the agent reaches adulthood,
		it is made to emigrate every five years according to this counter.
		However, once a child has migrated once, it is not made 
		to migrate again until it reaches adulthood.

		If the agent is an adult, the simulation checks if the 
		number of females to a male is more than the constant
		EMIGRATION_THRESHOLD_OF_FTM. The male is only made to emigrate
		if the number of females per male is less than that threshold.
		If this is so, the simulation next checks if the 
		number of years since the last emigration is greater than 
		5. If this is also true, a coin is tossed to determine 
		whether the agent is made to emigrate.

		Once a coin has been tossed, if it comes up heads,
		the simulation randomly shuffles all the other groups 
		and checks if the male is accepted into a group. This is done 
		by checking each group in turn. For each group, the 
		probability of acceptance is first calculated using the 
		dispersal_table. Then, a coin toss of that probability is 
		made. If the toss results in a 'heads', the male is added
		to the new group. 

		If the male is not added to this group, a coin toss is done to 
		check if he should die, using the probability in the dispersal
		table. If the toss comes up heads, the agent is left dead. If it
		does not come up heads, the next group in the shuffled set is 
		selected and this process is repeated. If the male is rejected 
		from two groups, it is left marked as dead.

		returns 
		-------
		true if the agent is leaving this group
		"""
		#check if live mature male
		#make sure the new_agent isn't dead
		if (this_agent.sex == "m") and new_agent.index in this_generation.whole_set:
			#check if child or adult
			if (this_agent.index not in this_generation.male_set and\
				this_agent.young_migration):
				#check if child has migrated
				#if so, don't check for migration
				return

			elif (this_agent.last_migration < \
				constants.MIGRATION_COUNTER_CAP or\
				females_to_male > \
				constants.EMIGRATION_THRESHOLD_OF_FTM):
				#if the adult has been stationary for 
				#less than 5 years, or if the number of
				#females in a group is greater than the
				#threshold defined in constants, then 
				#don't bother him
				return

			else:
				#find the probability of emigration
				probability_of_emigration =\
				 dispersal_table.chance_of_emigration(
				 	females_to_male, this_agent.age)

				#toss a coin with that probability
				toss =\
				 random_module.roll(probability_of_emigration)
				
				#if toss comes up heads, male is emigrating
				if (toss):
					#start by marking this agent as being dead
					new_generation.mark_agent_as_dead(new_agent)
					#now shuffle all groups (while removing this)
					#one. 
					groups = this_generation_population.groups
					chance_of_acceptance =\
					 dispersal_table.chance_of_acceptance(
					 	females_to_male, this_agent.age)
					max_group_index = len(groups)
					group_indices = range(0, max_group_index)

					tries = 0
					while (tries < 3):
						#shuffle groups
						random_module.shuffle(group_indices)
						target_group_index = group_indices[0]

						if (target_group_index != this_generation.group_index):
							if (random_module.roll(chance_of_acceptance[tries])):
								next_generation_population.groups[target_group_index].add_agent(new_agent)
								return
							else:
								#check if it dies
								if (random_module.roll(chance_of_acceptance[tries+1])):
									return
								else:
									tries += 2



	def save_age_stats(self, data_list, book):
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

	def save_group_composition_stats(self, data_list, book):
		"""
		collates and saves group composition stats.

		parameters
		----------
		data_list: list of lists
			data_list = [[1,2,3], [2,3,4]]
			each sublist represents the population of 
			all the groups in a generation. 
			each element in a sublist is the population
			of a group in a generation.
			In the above example, there were two generations
			in the simulation. Both generations had 3 groups.
			In the 1st generation, 1 group had 1 agent,
			another had 2, and the last had 3.
		"""
		output_list = []

		for generation in data_list:
			average_population = 0
			standard_deviation_aggregate = 0

			if len(generation) != 0:
				number_of_groups = len(generation)
			else:
				number_of_groups = 0.00001 #avoid div by 0

			#first calculate the average age
			for group_population in generation:
				average_population += group_population

			average_population = average_population/\
			 number_of_groups

			#now calculate standard dev
			for group_population in generation:
				standard_deviation_increment =\
				 math.pow((group_population - average_population), 2)
				standard_deviation_aggregate +=\
				 standard_deviation_increment

			standard_deviation = math.sqrt(
				(standard_deviation_aggregate/number_of_groups)
				)

			output_list.append((average_population, standard_deviation))

		#save the average age
		data_saver.save_group_composition_data(
			output_list, book
			)

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
		book = Workbook()
		self.save_age_stats(age_record_list, book)
		self.save_group_composition_stats(
			group_composition_list, book
			)
		data_saver.save_number_of_indivs(population_record_list, 
			male_population_record_list, female_population_record_list, 
			real_birth_rate_list, real_death_rate_list,
			average_edges_per_agent, 
			adult_females_per_males_list, book)
		output_directory =\
		 constants.OUTPUT_FOLDER + self.output_xls_name
		book.save(output_directory)

	def save_data_to_dot(self, dot_string, generation_number):
		generation_number_string = '%03d' % generation_number
		filename = self.dot_directory + generation_number_string + ".dot"
		destination_file = open(filename, "w+")
		destination_file.write(dot_string)

	def save_data_to_json(self, data_string, generation_number):
		generation_number_string = '%03d' % generation_number
		filename = self.json_directory + generation_number_string + ".json"
		destination_file = open(filename, "w+")
		destination_file.write(data_string)

if __name__ == '__main__':
	main()