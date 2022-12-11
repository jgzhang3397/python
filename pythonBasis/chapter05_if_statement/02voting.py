'''
You can have as many lines of code as you want in the block following the if statement. 
'''
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
    
# if - else statements
age = 17
if age >= 18:
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
    
# The if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:  
    print("Your admission cost is $40.")
    
# Using Multiple elif Blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:  
    price = 20
print("You admission cost : $" + str(price))

'''
Omitting the else Block

The else block is a catchall statement. 
It matches any condition that wasn’t matched by a specific if or elif test, 
and that can sometimes include invalid or even malicious data.
'''
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65: 
    price = 20
print(f"Your admission cost is ${price}.")