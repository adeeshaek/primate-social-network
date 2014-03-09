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

def save_population_data(data_list, book):
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