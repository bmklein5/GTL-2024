def reverse_string1(string):
    """returns the reverse of a given string
    HINT: google string slicing
    """
    # this syntax tells us to read the string backwards
    return string[::-1]

# OTHER SOLUTION
def reverse_string2(string):
    """this solution does step by step what the above func is doing
    """
    reversed_string = ""  # Initialize an empty string to store the reversed string
    for char in string:
        reversed_string = char + reversed_string  # Add each character to the front of the reversed_string
    return reversed_string


# TEST CASES
assert(reverse_string2("hello") == "olleh")
assert(reverse_string2("hello world") == "dlrow olleh")
assert(reverse_string2("brady is cool") == "looc si ydarb")
assert(reverse_string2("I Love Python") == "nohtyP evoL I")
