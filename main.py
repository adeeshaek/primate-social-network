"""	
Macaque Simulation Project
Adeesha Ekanayake 
5/12/2013

main.py
-------
Main run loop
"""

from agent import AgentClass
from group import AgentGroup
from lifetable import LifeTable
import seed
import copy
import loader
from random_module import RandomModule

def main():
	#import Seed and lifetable data
	this_generation = seed.load_group()
	table_data = loader.load_data()
	lifetable = table_data.life_table
	dispersal_table =\
	 table_data.dispersal_table
	random_module = RandomModule()

	for i in range (0, 10):

		#copy the group 
		new_generation = copy.deepcopy(this_generation)
		for agent in this_generation.whole_set:

			#check for birth
			if (agent in this_generation.female_set):
				females_to_male =\
				 this_generation.get_females_to_male()
				chance_of_giving_birth =\
				 lifetable.chance_of_birth(
				 	females_to_male, agent.age)

				#do a die roll
				if (random_module.roll(chance_of_giving_birth)):
					new_generation.give_birth_to_agent(
						agent, random_module, new_generation)

			#check for death


			#check for dispersal

		#set the old gen to the new one
		this_generation = new_generation

	#print the new generation
	for agent in this_generation.whole_set:
		print agent
if __name__ == '__main__':
	main()