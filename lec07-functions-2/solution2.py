def reverse_string(string):
    """ reverse the order of characters in a string, leave capitalization the same
    string (str) - string to be reversed
    returns str
    """
    return string[::-1]

def is_palindrome(string):
    """ determine whether a string is a palindrome, should ignore any capitalization
    string (str) - string to be checked
    returns bool (True or False)
    """
    string = string.lower()
    return reverse_string(string) == string

# write any custom tests/prints you want here

# TEST CASES
assert(reverse_string("hello world") == "dlrow olleh")
assert(reverse_string("brady is cool") == "looc si ydarb")
assert(reverse_string("I Love Python") == "nohtyP evoL I")
assert(is_palindrome("Kayak"))
assert(is_palindrome("Racecar"))
assert(is_palindrome("Able was I ere I saw Elba"))
assert(not is_palindrome("This is a random sentence"))
assert(not is_palindrome("Just a bunch of random words"))
