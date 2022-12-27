## Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

prompt = "\nWhat do you want to add in your pizza,"
prompt += "\nenter 'quit' to exit:"

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print("I will add " + message + " to your pizza")