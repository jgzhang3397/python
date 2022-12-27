# Write different versions of either Exercise 7-4 or Exercise 7-5 
# that do each of the following at least once:

# Use a conditional test in the while statement to stop the loop. 
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "Our cinema charges different fares according to different ages. Please enter your age:"
prompt += "\n(To exit, press the 'q' key or enter quit.) "


active = True
while active:
    message = input(prompt)
    
    if message == "quit" or message == 'q':
        break
    elif int(message) < 3:
        print("You are free.")
    elif 3 <= int(message) <= 12:
        print("You charge $10.") 
    elif 12 < int(message) < 100:
        print("You charge $15.")
    else:
        active = False