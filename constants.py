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

#number of years a male can stay in a group 
#before he is made to migrate
MIGRATION_COUNTER_CAP = 5 

#the maximum number of females to a male
#there can be in a group, for a male to still
#emigrate. If there are > 4 females per male
#in a group, males will not emigrate in a year.
EMIGRATION_THRESHOLD_OF_FTM = 4

#the age at which each sex reaches adulthood
ADULTHOOD_AGE = {
	"m" : 7,
	"f" : 5
}

#any adults over this age are killed
MAX_AGE = 30

#the maximum number of adults in a group
#if there are more than this number, 
#the group is split
GROUP_SPLIT_SIZE = 36

#the folder to which output files are saved
OUTPUT_FOLDER = "output/"

#the file to which seed 
LOADED_PICKLE_FILE_NAME = "loaded_data.pickle"