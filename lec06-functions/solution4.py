def capitalize_words(sentence):
    """capitlize the first letter of each word in the given string
    """
    new_sentence = ""
    for i in range(len(sentence)):
        if i == 0 or sentence[i-1] == " ": # check if letter is at start of word
            new_sentence += sentence[i].upper() # add capitalized letter
        else:
            new_sentence += sentence[i] # add letter as is
    return new_sentence


# TEST CASES
assert(capitalize_words("i love python") == "I Love Python")
assert(capitalize_words("the boy went to spain") == "The Boy Went To Spain")
assert(capitalize_words("hello") == "Hello")
assert(capitalize_words("country music is so awesome") == "Country Music Is So Awesome")
