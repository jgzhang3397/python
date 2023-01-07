# Make a list or tuple containing a series of 10 numbers and five letters. 
# Randomly select four numbers or letters from the list 
# and print a message saying that any ticket matching these four numbers or letters wins a prize.

from random import choice
my_list = [1, 2, 3, 4, 5, 66, 77, 65, 59, 63, 'e', 'l', 's', 'r', '&']

my_ticket = []

num = 4

while num >=1:
    pick_up = choice(my_list)
    my_ticket.append(pick_up)
    num -= 1

print(my_ticket)
print("any ticket matching these four numbers or letters wins a prize")
