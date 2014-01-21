Primate Social Network Simulation Project (pre-release)
=======================================================

This project aims to simulate a population of monkeys in the wild, and determine the effect of catch-and-release programs on their social networks. 

The project is conducted by [Marcy S. Weber](http://marcysweber.com), and [Adeesha Ekanayake](http://adeeshaek.com).

Implementation details
----------------------
1. Unit tests can be run using nosetest

2. Groups of Monkeys are represented in an array. Python arrays are arrays of references, and the array representing a group is an array of references to elements of class AgentClass. 

This means that a Monkey's individual identity is expressed by its index in the array. Once a monkey moves on to a new group, or dies, it's reference in the group array will be made null. This means that the array will continue to grow as the group gains new members. Although this is a memory leak, because the memory overhead of arrays is small, its effect should be negligible.




