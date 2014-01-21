"""
Macaque Simulation Project
Adeesha Ekanayake 
18/1/2013

friendships.py
--------------
defines factors related to friendships.

rules for forming friendships:
1. both have to be adults (fem > 5 years, male > 7)
2. the two individuals can't already have a relationship, 
	such as kin or aggressive
3. friendships have to be male-female or female-female

procedure for making new friends
1. decide if a new friend is about to be made
2. select the likely candidates for friendship
3. randomly select an individual from the pool of potential friends
"""

import agent
import random_module

def chance_of_making_friends(number_of_friends):
	if (number_of_friends > 2):
		return 0

	elif (number_of_friends == 2):
		return 0.05

	elif (number_of_friends == 1):
		return 0.1

	elif (number_of_friends == 0):
		return 0.15

def make_friend(agent, group, random_module):
	"""
	checks whether the agent is able to make friends. If it can,
	returns the index of an individual in the group who is to be a
	friend. If it cannot, it returns None.

	parameters
	----------
	agent: the method checks if this agent can make a new friend
	group: the agent's group
	random_module: used to calculate chance
	"""

	if (agent.age < 5):
		return None

	elif (agent.age < 7 and agent.sex == "m"):
		return None

	else:
		#dieroll
		probability = chance_of_making_friends(len(agent.friends))

		if random_module.roll(probability):
			list_of_candidates =\
			 group.get_unrelated_members_of_age(agent)	

			new_friend =\
			 random_module.shuffle(list_of_candidates)[0]

			return new_friend






















