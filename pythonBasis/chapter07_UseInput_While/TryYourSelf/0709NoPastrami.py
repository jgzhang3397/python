# Using the list sandwich_orders from Exercise 7-8, 
# make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['tuna sanwich','pastrami', 'tomato sanwich', 'pastrami', 'potato sanwich', 'pastrami']
print(sandwich_orders)
print("Deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_sanwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sanwich)
    
print(finished_sandwiches)
# Make sure no pastrami sandwiches end up in finished_sandwiches
while 'pastrami' in finished_sandwiches:
    print("Warning!!! pastrami occured")
