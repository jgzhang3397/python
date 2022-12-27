# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

dream_vacations = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    vacation_place = input("If you could visit one place in the world, where would you go? ")
    
    # Store in the dictionary.
    dream_vacations[name] = vacation_place
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False
    
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, vacation_place in dream_vacations.items():
    print(name.title() + " would like in " + vacation_place.title() + " have a vacation.")