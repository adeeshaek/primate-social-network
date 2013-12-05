"""	
Macaque Simulation Project
Adeesha Ekanayake 
5/12/2013

common.py
---------
Common methods
"""

def read_CSV(inputString):
	"""
	reads passed in string in csv format into an array of values. Deals with
	possibility of csv values in an excel cell

	parameters
	----------
	inputString: raw input string. Can be 1 value or multiple values

	returns
	-------
	array of elements
	"""
	if inputString == True: #make sure input is not empty cell
		split_array = inputString.split(',')
		int_array = [int(x) for x in split_array]
	
	else:
		int_array = []

	return int_array
