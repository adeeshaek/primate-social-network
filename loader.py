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
from classes import LifeTable

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

		return life_table_sheet

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

		life_table = LifeTable()

		for row_index in range (self.STARTING_ROW, seedsheet.nrows):


