Primate Social Network Simulation Project (pre-release)
=======================================================

This project aims to simulate a population of monkeys in the wild, and determine the effect of catch-and-release programs on their social networks. 

The project is conducted by [Marcy S. Weber](http://marcysweber.com), and [Adeesha Ekanayake](http://adeeshaek.com).

Implementation details
----------------------
1. The main 

2. Unit tests can be run using nosetest

3. Groups of Agents are represented by a container class, which keeps track of them using an array. Python arrays are arrays of references, and the array representing a group is an array of references to elements of class AgentClass. 

This means that an agent's individual identity is expressed by its index in the array. Once a monkey moves on to a new group, or dies, it's reference in the group array will be made null. This means that the array will continue to grow as the group gains new members. Although this is a memory leak, because the memory overhead of arrays is small, its effect should be negligible, and the cost of memory should be offset by the speed of access. 




