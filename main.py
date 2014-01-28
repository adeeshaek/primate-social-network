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

def main():
	#import Seed
	this_generation = seed.load_group()

	for i in range (0, 10):

		#copy the group 
		new_generation = copy.deepcopy(this_generation)

		for agent in this_generation.whole_set:
			
			print agent



if __name__ == '__main__':
	main()