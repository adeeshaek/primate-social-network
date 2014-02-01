"""	
Macaque Simulation Project
Adeesha Ekanayake 
5/12/2013

constants.py
------------
Contains a list of constant definitions used in the simulation. These include
definitions of age classes
"""


"""
contains a list of definitions for constants used in the simulation
"""
AGECLASS_FEMALE = {
	0 : "inf",
	2 : "juv",
	5 : "ya",
	10 : "yngtomid",
	15 : "mid",
	20 : "old",
	25 : "sen"
	}

AGECLASS_MALE = {
	0 : "inf",
	2 : "juv",
	5 : "subad",
	7 : "ya",
	10 : "yngtomid",
	15 : "mid",
	20 : "old",
	25 : "sen"
	}

SEX_DICT = {
	"m" : "SEX_MALE",
	"f" : "SEX_FEMALE"
	}

RANK_ALPHA = "A"

#the age at which each sex reaches adulthood
ADULTHOOD_AGE = {
	"m" : 7,
	"f" : 5
}

#the folder to which output files are saved
OUTPUT_FOLDER = "output/"