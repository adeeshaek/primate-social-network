"""
Macaque Simulation Project
Adeesha Ekanayake 
5/12/2013

loader.py
---------
loads data from excel document into memory. The excel workbook must be
structured as follows:
	There must be 4 sheets in the book in the following order:
	1. Life table
	2. Dispersal table
	3. Friendship table
	4. Dominance table
"""

import xlrd
from lifetable import LifeTable
from dispersaltable import DispersalTable

def load_data():
	"""
	convenient method to quickly load data from excel file

	returns
	-------
	data from the excel sheet as described by class Loader
	"""
	loader = Loader()
	loader.load_data()

	return loader

class Loader:
	"""
	loads data from the excel document on the following areas:
		* Lifetable
		* Dispersal
		* Friendships
		* Dominance
	"""

	life_table = None
	dispersal_table = None

	EXCEL_FILENAME = "Excel Files/life_table.xlsx"
	STARTING_ROW = 2 #the first 2 rows are headers, so reader must avoid them

	def test(self):
		"""
		convenience class used for testing
		"""
		#load the excel book
		book = xlrd.open_workbook(self.EXCEL_FILENAME)

		#load dispersaltable
		dispersal_table_sheet = book.sheet_by_index(1)
		self.dispersal_table = self.load_dispersal_table(dispersal_table_sheet)

		print self.dispersal_table.emigration

		print self.dispersal_table.immigration

	def load_data(self):
		"""
		loads data from the excel file into memory

		returns
		-------
		dictionary with the following structure
			|- "life_table_dict" : LifeTable object
			|- DispersalTable object
			|- FriendshipTable object
			|- DominanceTable object
		"""

		#load the excel book
		book = xlrd.open_workbook(self.EXCEL_FILENAME)

		#load lifetable
		life_table_sheet = book.sheet_by_index(0)
		self.life_table = self.load_life_table(life_table_sheet)

		#load dispersaltable
		dispersal_table_sheet = book.sheet_by_index(1)
		self.dispersal_table = self.load_dispersal_table(dispersal_table_sheet)

	def load_life_table(self, life_table_sheet):
		"""
		loads the life table into memory

		lifetable must be formatted as follows:
		-------------------------------------------------------
		|male					  | |female				      |
		-------------------------------------------------------
		|age_class| |qx|bx|lx|lxbx| |age_class| |qx|bx|lx|lxbx|
		-------------------------------------------------------

		qx: chance of dying this year
		bx: chance of giving birth this year
		lx: count of individuals who reach this age class
		lxbx: lx * bx

		parameters
		----------
		life_table_sheet: the sheet with the life table in it

		returns
		-------
		a LifeTable object
		"""
		end_flag = True #used to let user customize number of rows in excel
						 #file by setting an END flag at the end of the table

		life_table = LifeTable()

		for row_index in range (self.STARTING_ROW, life_table_sheet.nrows):

			if life_table_sheet.cell_value(row_index,0) == 'END':
				end_flag = False

			if end_flag:
				#parameters for female
				age = life_table_sheet.cell_value(row_index,1)
				qx = life_table_sheet.cell_value(row_index,3)
				bx = life_table_sheet.cell_value(row_index,4)

				life_table.female_life_table[age] = (qx, bx)

				#parameters for male
				age = life_table_sheet.cell_value(row_index,9)
				qx = life_table_sheet.cell_value(row_index,11)
				bx = life_table_sheet.cell_value(row_index,12)

				life_table.male_life_table[age] = (qx, bx)			

		return life_table

	def load_dispersal_table(self, dispersal_table_sheet):
		"""
		loads dispersal table into memory.

		This table contains data on emigration and immigration for males
		by age class. Since females do not leave the group in our 
		model, this table only concerns males.
		"""
		end_flag = True #used to let user customize number of rows in excel
						 #file by setting an END flag at the end of the table

		dispersal_table = DispersalTable()

		for row_index in range (self.STARTING_ROW, dispersal_table_sheet.nrows):

			if dispersal_table_sheet.cell_value(row_index,0) == 'END':
				end_flag = False

			elif end_flag:
				age = dispersal_table_sheet.cell_value(row_index,1)
	
				#emigration
				chance_of_emigration =\
					dispersal_table_sheet.cell_value(row_index,2)
				dispersal_table.emigration[age] = chance_of_emigration

				#immigration
				chance_of_acceptance =\
					dispersal_table_sheet.cell_value(row_index,3)

				chance_of_death_first_rejection =\
					dispersal_table_sheet.cell_value(row_index,4)

				chance_of_acceptance_first_rejection =\
					dispersal_table_sheet.cell_value(row_index,5)				

				chance_of_death_second_rejection =\
					dispersal_table_sheet.cell_value(row_index,6)	

				dispersal_table.immigration[age] = (chance_of_acceptance,
					chance_of_death_first_rejection, 
					chance_of_acceptance_first_rejection,
					chance_of_death_second_rejection)			

		return dispersal_table

































