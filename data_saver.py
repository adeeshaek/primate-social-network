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

def save_number_of_indivs(data_list, book):
	"""
	saves data to the specified excel workbook

	parameters
	----------
	data_list: list of integers. Each int is the pop
		of its generation.
	"""
	pop_sheet = book.add_sheet('Population')

	#init the sheet
	pop_sheet.write(0,0,'Generation')
	pop_sheet.write(0,1,'Population')

	for i in range(0, len(data_list)):
		pop_sheet.write(i+1,0,i+1)
		pop_sheet.write(i+1,1,data_list[i])

