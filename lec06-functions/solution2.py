import numpy as np

def average_of_list1(lst):
    """ returns the average of a list of numbers
    if lst is the empty list [], return 0
    """
    if not lst:
        return 0
    return np.mean(lst)

def average_of_list2(lst):
    """ another solution
    """
    if len(lst) == 0:
        return 0
    total = sum(lst)
    length = len(lst)
    return total / length


# TEST CASES
assert(average_of_list1([1,2,3]) == 2)
assert(average_of_list1([-1,1,-2,2]) == 0)
assert(average_of_list1([-10,-8,-12,-20]) == -12.5)
assert(average_of_list1([]) == 0)
assert(average_of_list1([50, 100, 150]) == 100)

assert(average_of_list2([1,2,3]) == 2)
assert(average_of_list2([-1,1,-2,2]) == 0)
assert(average_of_list2([-10,-8,-12,-20]) == -12.5)
assert(average_of_list2([]) == 0)
assert(average_of_list2([50, 100, 150]) == 100)

