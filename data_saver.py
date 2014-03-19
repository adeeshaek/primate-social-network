"""	
Macaque Simulation Project
Adeesha Ekanayake 
1/02/2014

data_saver.py
-------------
Saves analytical data to disk, using xlwt
"""
from xlwt import Workbook
from tempfile import TemporaryFile
import constants

def save_age_data(data_list, book):
	"""
	saves data to an excel file in the specified workbook

	parameters
	----------
	data_list: should be in the form of a list of tuples.
		each tuple represents a generation and is of the 
		form (average_age, standard_dev)
	book: a workbook to save data to
	"""
	age_sheet = book.add_sheet('Age')

	#init the sheet
	age_sheet.write(0,0,'Generation')
	age_sheet.write(0,1,'Average age')
	age_sheet.write(0,2,'Standard deviation')

	for i in range(0, len(data_list)):
		current_generation = data_list[i]
		age_sheet.write(i+1,0,i+1)
		age_sheet.write(i+1,1,current_generation[0])
		age_sheet.write(i+1,2,current_generation[1])

def save_group_composition_data_for_simulation(data_list, book):
	"""
	saves data to an excel file in the specified workbook

	parameters
	----------
	data_list: should be in the form of a list of tuples.
		each tuple represents a generation and is of the 
		form (average_age, standard_dev)
	book: a workbook to save data to
	"""
	age_sheet = book.add_sheet('Groups')

	#init the sheet
	age_sheet.write(0,0,'Generation')
	age_sheet.write(0,1,'Avg agents per group')
	age_sheet.write(0,2,'Standard deviation')

	for i in range(0, len(data_list)):
		current_generation = data_list[i]
		age_sheet.write(i+1,0,i+1)
		age_sheet.write(i+1,1,current_generation[0])
		age_sheet.write(i+1,2,current_generation[1])

def save_number_of_indivs(data_list, male_data_list,
 female_data_list,
 real_birth_rate_list, real_death_rate_list,
 average_edges_per_agent, 
 adult_females_per_males_list, book):
	"""
	saves data to the specified excel workbook

	parameters
	----------
	data_list: list of integers. Each int is the pop
		of its generation.
	male_data_list: list of integers. Each int is the 
		pop of its generation (males only)
	"""
	pop_sheet = book.add_sheet('Population')

	#init the sheet
	pop_sheet.write(0,0,'Generation')
	pop_sheet.write(0,1,'Population')
	pop_sheet.write(0,2,'Number of Males')
	pop_sheet.write(0,3,'Number of Females')
	pop_sheet.write(0,4,'birth rate')
	pop_sheet.write(0,5,'death rate')
	pop_sheet.write(0,6,'Edges per agent')
	pop_sheet.write(0,7,'Adult females per male')

	for i in range(0, len(data_list)):
		pop_sheet.write(i+1,0,i+1)
		pop_sheet.write(i+1,1,data_list[i])
		pop_sheet.write(i+1,2,male_data_list[i])
		pop_sheet.write(i+1,3,female_data_list[i])
		pop_sheet.write(i+1,4,real_birth_rate_list[i])
		pop_sheet.write(i+1,5,real_death_rate_list[i])
		pop_sheet.write(i+1,6,average_edges_per_agent[i])
		pop_sheet.write(i+1,7,adult_females_per_males_list[i])

def save_experiment_data(book,
	total_population_list, total_age_list, 
	total_age_sd_list, total_groups_list,
	total_males_to_females_list,
	total_edges_per_agent_list):
	
	data_sheet = book.add_sheet('Data')

	data_sheet.write(0,1,'Population')
	data_sheet.write(0,2,'Age')
	data_sheet.write(0,3,'Age - SD')
	data_sheet.write(0,4,'Number of groups')
	data_sheet.write(0,5,'Females per Male')
	data_sheet.write(0,6,'Edges per Agent')

	for i in range(0, len(total_population_list)):
		data_sheet.write(i+1, 0, i)
		data_sheet.write(i+1, 1, total_population_list[i])
		data_sheet.write(i+1, 2, total_age_list[i])
		data_sheet.write(i+1, 3, total_age_sd_list[i])
		data_sheet.write(i+1, 4, total_groups_list[i])
		data_sheet.write(i+1, 5, total_males_to_females_list[i])
		data_sheet.write(i+1, 6, total_edges_per_agent_list[i])

def save_experiment_population_data(book,
	last_gen_population_breakdown, total_population_list):
	data_sheet = book.add_sheet('Population breakdown')

	data_sheet.write(0,0,'Simulation number')
	data_sheet.write(0,1,'Adult Males')
	data_sheet.write(0,2,'Male Children')
	data_sheet.write(0,3,'Adult Females')
	data_sheet.write(0,4,'Female Children')
	data_sheet.write(0,5,'Total Population')

	for i in range(0, len(last_gen_population_breakdown)):
		data_sheet.write(i+1,0, i)
		data_sheet.write(i+1,1, last_gen_population_breakdown[i][0])
		data_sheet.write(i+1,2, last_gen_population_breakdown[i][2])
		data_sheet.write(i+1,3, last_gen_population_breakdown[i][1])
		data_sheet.write(i+1,4, last_gen_population_breakdown[i][3])
		data_sheet.write(i+1,5, total_population_list[i])

def save_experiment_relationship_data(book,
	relationships_list):
	data_sheet = book.add_sheet('Relationships')

	data_sheet.write(0,0,'Simulation number')
	data_sheet.write(0,1,'Parent-child')
	data_sheet.write(0,2,'Sisters')
	data_sheet.write(0,3,'Aggressive')
	data_sheet.write(0,4,'Friendships')

	for i in range(0, len(relationships_list)):
		data_sheet.write(i+1,0, i)
		data_sheet.write(i+1,1, relationships_list[i][0])
		data_sheet.write(i+1,2, relationships_list[i][1])
		data_sheet.write(i+1,3, relationships_list[i][2])
		data_sheet.write(i+1,4, relationships_list[i][3])


def save_group_composition_data(book,
	group_composition_list):
	age_sheet = book.add_sheet('Groups')

	#init the sheet
	age_sheet.write(0,0,'Generation')
	age_sheet.write(0,1,'Avg agents per group')
	age_sheet.write(0,2,'Standard deviation')

	for i in range(0, len(group_composition_list)):
		current_generation = group_composition_list[i]
		age_sheet.write(i+1,0,i+1)
		age_sheet.write(i+1,1,current_generation[0])
		age_sheet.write(i+1,2,current_generation[1])



