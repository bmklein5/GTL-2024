# GOAL: Check whether a specified value is contained within a list of values
# prints 'True' or 'False'
# get the value to check for from the user (between 0 and 10)

# EXAMPLE:
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# HELPER CODE: this will generate a random list of numbers between 0 and 10, don't worry how it works
import random
N = 5 # change this number to control the size of the list
num_list = [ random.randint(0,10) for i in range(N) ] # use this list to check for the user's number
print(num_list)

# YOUR CODE HERE

