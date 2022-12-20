# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

numbers_people = input("How many people are in your dinner group? ")

numbers_people = int(numbers_people)

if numbers_people > 8 :
    print("Sorry, you must wait for a table.")
else:
    print("Your table is ready!")
