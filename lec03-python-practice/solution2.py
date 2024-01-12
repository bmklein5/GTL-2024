# GOAL: sum all numbers in a list and print result

# HELPER CODE: this will generate a random list of numbers between 0 and 10, don't worry how it works
import random
N = 5 # change this number to control the size of the list
num_list = [ random.randint(0,10) for i in range(N) ]
print(num_list)

# HINTS:
# the += operator may very useful here
# for loop may also very usefule

# YOUR CODE HERE

# better solution
total = sum(num_list)
print("the sum of the list is", total)

# another solution
total_ = 0
for num in num_list:
    total_ += num
print("the sum of the list is", total_)


