# HINTS: 
# 'continue' keyword is helpful for ignoring spaces in count_character()

def count_character(string):
    """ count the frequency of characters in a string, ignoring spaces and capitalization
    string (str)
    returns: dict
    """
    freq_dict = {}
    for char in string.lower(): # ignore capitalization
        if char == ' ': # ignore spaces
            continue
        elif char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def most_frequent_character(string):
    """ return the most frequent character in a string,
    resolve tie by returning first character with the max frequency,
    ignore capitalization, if empty string return None
    string (str)
    returns: str
    """
    if string == "":
        return None
    string = string.lower() # ignore capitalization
    freq = count_character(string)
    best_count = max(freq.values())
    for char in string:
        if freq[char] == best_count:
            return char
    return None

# write any custom tests/prints you want here


# TEST CASES
assert(count_character("hello world") == {
    'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1
})
assert(count_character("python") == {
    'p':1, 'y':1, 't':1, 'h':1, 'o':1, 'n':1 
})
assert(count_character("Majadahonda") == {
    'm':1, 'a':4, 'j':1, 'd':2, 'h':1, 'o':1, 'n':1 
})
assert(most_frequent_character("Majadahonda") == "a")
assert(most_frequent_character("") is None)
assert(most_frequent_character("hahaha") == "h")