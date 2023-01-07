# You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. 
# Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice

sum_ticket = [1, 45, 5, 'q', 'e']

win_ticket = [1, 45, 5, 'q']
my_ticket = []

def pull_ticket(number = 4):
    '''a loop keeps pulling tickets to win'''
    while number:
        pickup = choice(sum_ticket)
        sum_ticket.remove(pickup)
        my_ticket.append(pickup)
        number -= 1
        
# calculate how many times 
count = 0
while True:
    if my_ticket == win_ticket:
        print(f"You need {count} times to win")
        break
    else:
        count += 1
        # clear my_ticket
        my_ticket = []
        # recover sum_ticket
        sum_ticket = [1, 45, 5, 'q', 'e']
        pull_ticket()
        
        


