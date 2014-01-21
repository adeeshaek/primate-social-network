"""	
Macaque Simulation Project
Adeesha Ekanayake 
5/12/2013

common.py
---------
Common methods
"""

def read_CSV(inputValue):
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
	if inputValue == '':
		return []

	elif isinstance(inputValue, basestring): 

		#make sure input is not empty cell
		split_array = inputValue.split(',')

		#if int(x) was used instead of int(float(x)) a valueError is thrown
		int_array = [int(float(x)) for x in split_array] 

	else:
		int_array = []
		int_array.append(int(inputValue)) #make it int to keep type consistent

	return int_array


