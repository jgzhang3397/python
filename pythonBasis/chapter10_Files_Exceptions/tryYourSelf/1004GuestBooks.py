# Write a while loop that prompts users for their name. 
# When they enter their name, print a greeting to the screen and 
# add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    print("Please give the names of guest (enter q to quit): ")
    loopcount = 1
    while True:
        names = input("#Nr" +  str(loopcount) + ": ")
        if names == 'q' or names == 'Q' or names == 'quit':
            break
        else:
            file_object.write(names.title() + ".\n")
            print("Welcome, " + names.title() + ".\n")
            loopcount += 1