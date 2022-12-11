# Testing Multiple Conditions

'''
    However, sometimes it’s important to check all of the conditions of interest. 
    In this case, you should use a series of simple if statements with no elif or else blocks.
'''
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

'''
In summary, if you want only one block of code to run, use an if-elif-else chain. 
If more than one block of code needs to run, use a series of independent if statements.
'''