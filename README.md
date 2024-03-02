Unnecessary loops can lead to unintelligible code. It is therefore advisable to avoid them in all ways if possible. 
In our code(flat.py), we have two functions doing the same thing but differently. The second one seems to flatten our list 
seamlessly, by use of function itertools.chain.
Comparing the two, the latter seems a better approach. 

In our second code (std_dev_mean.py), we have two functions whose operational difference can be seen by close observation. In the first one, we go the long way in the calculation of mean and standard deviation for a given list(data). The numpy module's functions for mean and standard deviation calculation seems to offer the take-route to avoid the for loop.
Check the execution time for both functions.
Avoid unnecessary loops in all ways possible.
