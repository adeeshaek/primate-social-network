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
import constants

def chance_of_making_friends(agent):
	"""
	returns the probability that an agent can make friends.

	parameters
	----------
	agent: target agent
	"""
	number_of_friends = len(agent.friends)

	if (number_of_friends > 2):
		return 0

	elif (number_of_friends == 2):
		return 0.05

	elif (number_of_friends == 1):
		return 0.1

	elif (number_of_friends == 0):
		return 0.15

def check_for_friendships(this_agent, new_agent,
	this_generation, new_generation, random_module):
	"""
	checks if an agent is eligible to make friends.
	If so, it obtains the probability that the agent
	will make a friend. It then flips a coin to check
	if a friendship will be made, where the probability
	of the coin coming up heads is the probability of the 
	agent making friends. If the coin comes up heads, a 
	friendship is formed between the agent and a suitable
	other agent from within the group.

	Males can only make friends with females, whereas
	females can also form friendships with other females.
	Sisters cannot form friendships with each other.

	parameters
	----------
	agent: target agent
	"""
	probability_of_making_friends = chance_of_making_friends(
		this_agent)

	if (random_module.roll(probability_of_making_friends)):

		#select a friend
		if (new_agent.sex == "m"):
			target_population =\
			 new_generation.whole_set -\
			 set([new_agent.index])

			if (len(target_population) == 0):
				return

			randomized_population = list(target_population)
			random_module.shuffle(randomized_population)

			target_friend_index = randomized_population[0]
			target_friend = new_generation.agent_dict[
			 target_friend_index]
			new_generation.mark_agents_as_friends(
				new_agent, target_friend)

		else:
			assert(new_agent.sex == "f")
			agent_sisters_set = set(new_agent.sisters)
			target_population =\
			 new_generation.whole_set -\
			 set([new_agent.index]) -\
			 set(new_agent.sisters)

			if (len(target_population) == 0):
				return

			randomized_population = list(target_population)
			random_module.shuffle(randomized_population)

			target_friend_index = randomized_population[0]			
			target_friend = new_generation.agent_dict[
			 target_friend_index]
			new_generation.mark_agents_as_friends(
				new_agent, target_friend)



















