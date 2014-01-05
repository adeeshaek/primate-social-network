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
from classes import LifeTable, DispersalTable

def load_data():
	"""
	convenient method to quickly load data from excel file

	returns
	-------
	data from the excel sheet as described by class Loader
	"""
	loader = Loader()
	excel_data = loader.load_data()

	return excel_data

class Loader:
	"""
	loads data from the excel document on the following areas:
		* Lifetable
		* Dispersal
		* Friendships
		* Dominance
	"""

	life_table = None

	EXCEL_FILENAME = "Excel Files/life_table.xlsx"
	STARTING_ROW = 2 #the first 2 rows are headers, so reader must avoid them

	def load_data(self):
		"""
		loads data from the excel file into memory

		returns
		-------
		dictionary with the following structure
			|- LifeTable object
			|- DispersalTable object
			|- FriendshipTable object
			|- DominanceTable object
		"""

		#load the excel book
		book = xlrd.open_workbook(self.EXCEL_FILENAME)

		#the life table is the first sheet
		life_table_sheet = book.sheet_by_index(0)

		life_table_dict = self.load_life_table(life_table_sheet)

		return life_table_dict

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
		"""
		end_flag = True #used to let user customize number of rows in excel
						 #file by setting an END flag at the end of the table

		dispersal_table = DispersalTable()

		for row_index in range (self.STARTING_ROW, dispersal_table_sheet.nrows):

			if dispersal_table_sheet.cell_value(row_index,0) == 'END':
				end_flag = False

			if end_flag:
				#parameters for female
				age = dispersal_table_sheet.cell_value(row_index,1)
				qx = dispersal_table_sheet.cell_value(row_index,3)
				bx = dispersal_table_sheet.cell_value(row_index,4)

				life_table.female_life_table[age] = (qx, bx)

				#parameters for male
				age = dispersal_table_sheet.cell_value(row_index,9)
				qx = dispersal_table_sheet.cell_value(row_index,11)
				bx = dispersal_table_sheet.cell_value(row_index,12)

				life_table.male_life_table[age] = (qx, bx)			

		return life_table
































