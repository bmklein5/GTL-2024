"""
for this exercise we will be taking a string and converting
its letters in a frequency dictionary

for example, if starting string is "hello", the freq dict will
be {'h':1, 'e':1, 'l':2, 'o':1}
"""

# create an empty dict
freq = {}

# feel free to change this to 
# whatever string you want
word = "mississippi"

# loop thru the string (for loop), for each char
# add 1 to the dict if it exists or create a new
# entry

for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(f"for the word, {word}, the freq dict is {freq}")
