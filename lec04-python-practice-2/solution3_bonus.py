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

my_list = []
command = ""

while command != "done":
    command = input("do you want to add, remove, or be done? ")
    if command not in ["add", "remove", "done"]:
        continue
    
    if command == "add":
        my_list.append(input("give me an item to add: "))
    elif command == "remove":
        my_list.remove(input("give me an item from the list to remove: "))
    else:
        break

    print(f"list so far: {my_list}")

print(f"FINAL LIST: {my_list}")
