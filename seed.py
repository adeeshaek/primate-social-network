"""	
Macaque Simulation Project
Adeesha Ekanayake 
5/12/2013

seed.py
-------
This class is used to generate a seed group agents. The seed group is defined
using the excel file defined in this class

rules for relationships are defined in the test class located at the bottom 
of this module
"""

import xlrd
import constants
from common import read_CSV
from agent import AgentClass
from group import AgentGroup
from population import Population

def load_group(parent_population):
	"""
	convenient method to quickly load group from excel file

	parameters
	----------
	parent_population: parent population containing the group

	returns
	-------
	group as described in excel file
	"""
	generator = SeedGenerator()
	group = generator.generate_seed(parent_population)

	return group

def print_seed_group(destination_filename):
	"""
	prints seed group, by writing to a file in dot syntax
	"""
	parent_population = Population()
	generator = SeedGenerator()
	group = generator.generate_seed(parent_population)

	dot_string = group.get_dot_string()

	savefile = open(destination_filename, "wr+")
	savefile.write(dot_string)

class SeedGenerator:
	"""
	Generates a seed according to the data set out in seed.xlsx. This document
	has the following format:
	|number|ageclass|sex|age|rank|parent-child|sister|aggressive|friend|

	number - the identification number of the individual in the group
	ageclass - the ageclass of the individual, as recorded in constants.py
	sex - sex of the individual as defined in constants.py
	age - age of individual in years
	rank - whether or not the individual is the alpha male/female

	relationship-related parameters
	-------------------------------
	parent - the parent of this individual
	sister - the sister(s) of this individual. Multiple entries separated by
		comma.
	aggressive - aggressive relationships formed by this individual. Binary
		value.
	friendship - friendships formed by this individual. Binary value. Multiple
		entries separated by commas.

	*note - multiple entries in a field should be written as |a, b, c|.
	""" 

	SEED_FILENAME = "Excel Files/seed.xlsx"
	STARTING_ROW = 2 #the first two rows in the excel sheet are headers

	def generate_seed(self, parent_population):
		"""
		generates the default sheet defined as SEED_FILENAME

		parameters
		----------
		parent_population: the parent population containing this 
		 group

		returns
		-------
		a group as defined in the excel spreadsheet in SEED_FILENAME
		"""
		book = xlrd.open_workbook(self.SEED_FILENAME)

		#the seed is looked for in the first sheet of the workbook
		seedsheet = book.sheet_by_index(0) 

		group = AgentGroup(parent_population)

		#iterate through the rows
		for row_index in range (self.STARTING_ROW, seedsheet.nrows):
			
			#get parameters
			sex = seedsheet.cell_value(row_index, 2)
			age_in_years = seedsheet.cell_value(row_index, 3)
			rank = seedsheet.cell_value(row_index, 4)

			#relationships are arrays, so read them into lists using read_CSV
			parent = seedsheet.cell_value(row_index, 5)
			sister = seedsheet.cell_value(row_index, 6)
			aggressive = seedsheet.cell_value(row_index, 7)
			friend = seedsheet.cell_value(row_index, 8)

			sister = read_CSV(sister)
			aggressive = read_CSV(aggressive)
			friend = read_CSV(friend)

			#create new agent
			this_agent = AgentClass(age_in_years, sex, \
				rank, parent, sister, aggressive, friend, row_index - 1)
			#add agent to group

			group.add_agent(this_agent)

		#make a pass through the group marking parents
		for agent_key in group.agent_dict:
			if (group.agent_dict[agent_key]):
				agent = group.agent_dict[agent_key]
				if (agent.parent != None and agent.parent != ''):
					group.mark_as_parent(
						group.agent_dict[int(agent.parent)],
						agent)

		return group



if __name__ == '__main__':
	print_seed_group("output//seed.dot")

















