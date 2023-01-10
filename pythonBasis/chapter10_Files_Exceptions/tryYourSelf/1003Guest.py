# Write a program that prompts the user for their name. 
# When they respond, 
# write their name to a file called guest.txt.

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    message = input("Please enter your name: ")
    file_object.write(message)
    file_object.write(" you are so cute!!")