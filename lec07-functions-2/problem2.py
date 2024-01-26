def reverse_string(string):
    """ reverse the order of characters in a string
    string (str) - string to be reversed
    returns str
    """
    # delete 'pass' and write your code here
    pass

def is_palindrome(string):
    """ determine whether a string is a palindrome, should ignore any capitalization
    string (str) - string to be checked
    returns bool (True or False)
    """
    # delete 'pass' and write your code here
    pass

# write any custom tests/prints you want here

# TEST CASES
assert(reverse_string("hello world") == "dlrow olleh")
assert(reverse_string("brady is cool") == "looc si ydarb")
assert(reverse_string("I Love Python") == "nohtyP evoL I")
assert(is_palindrome("kayak"))
assert(is_palindrome("racecar"))
assert(is_palindrome("Able was I ere I saw Elba"))
assert(not is_palindrome("this is a random sentence"))
assert(not is_palindrome("just a bunch of random words"))
