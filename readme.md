Primate Social Network Simulation Project 
=======================================================

This project aims to simulate a population of monkeys in the wild, and determine the effect of catch-and-release programs on their social networks. 

The project is conducted by [Marcy S. Weber](http://marcysweber.com), and [Adeesha Ekanayake](http://adeeshaek.com).

How to run
-----------
* To run the entire experiment, execute 
```
    run_all.sh
```
  * The machine running this experiment must have at least 8gb of memory available in order to execute it in a reasonable timeframe
  * We are working on a python script to execute the project
  * 

* To obtain social network graphs of the simulation, please execute
```
    run_all_simulations.py
```
  * once this script finishes executing, navigate to the /dot directory, and execute 
  ```
  dotify.sh
  ```
  * This will convert the social network graphs into png files. 
  * To execute dotify.sh, you must have graphviz installed.



