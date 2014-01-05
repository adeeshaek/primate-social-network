import constants

class LifeTable:
	"""
	defines life-table data.

	container for 2 dictionaries of this structure:
	life_table[age_in_years] = (qx, bx)

	the 2 dictionaries are for males and females. 
	"""

	male_life_table = {}
	female_life_table = {}