# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; 
# if they are between 3 and 12, the ticket is $10; 
# and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, 
# and then tell them the cost of their movie ticket.

prompt = "\nPlease enter your age, then i will tell you the price of your ticket:"
prompt += "\nEnter 0 to exit."
active = True

while active:
    message = input(prompt)
    
    if (int(message) < 3 and int(message) > 0):
        price = 0
        print("The price of your ticket is $" + str(price))
    elif (int(message) >= 3 and int(message) <= 12):
        price = 10
        print("The price of your ticket is $" + str(price))
    elif (int(message) > 12):
        price = 15
        print("The price of your ticket is $" + str(price))
    elif (int(message) == 0):
        active = False
    else:
        print("invalid input please enter again!")
    
        