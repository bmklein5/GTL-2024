""" Grocery List Manager
for the exercise, you will get 3 strings from the user
and add them to a list to keep track of their groceries

follow the following structure
1)  initialize an empty list
2)  get 3 items from user and add them
3)  display the grocery list
4)  ask the user for 1 item to remove
5)  display the final list
6)  bonus (optional) allow the user to continuously
    add or remove items until the input the word 'done'
"""

# init the empty list
my_list = []

# get 3 items from user and add them to the list
# you'll want to use the .append() method
for i in range(3):
    item_to_add = input("give me an item to add: ")
    my_list.append(item_to_add)

# display the list
print(my_list)

# ask user for 1 item to remove
# you'll want to use the .remove() method
item_to_remove = input("give me an item from the list to remove: ")
my_list.remove(item_to_remove)

# display the final list
print(my_list)
