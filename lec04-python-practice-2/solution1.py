"""
for this exercise we will be creating a game which follows
the following structure:
1) computer: picks random number between 1 and 100 (maybe start with 10)
2) user: guesses a number
3) computer: tells user if their guess was high or low
4) repeats steps 2 and 3 until number is guessed
"""

# import random
import random
# pick a random number
num = random.randint(0,100)

while True:
    # get the guess from the user
    guess = int(input("guess a number: "))

    # logic for checking how to respond 
    # should be a simple if, elif, else
    if guess < num:
        print("too low")
    elif guess > num:
        print("too high")
    else:
        break

print("congrats, you win!")
