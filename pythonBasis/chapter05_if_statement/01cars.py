'''
    The following code loops through a list of car names and looks for the value 'bmw'. 
    Whenever the value is 'bmw', it’s printed in uppercase instead of title case:
'''
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
"""
    Checking for Inequality:
        When you want to determine whether two values are not equal, 
        you can combine an exclamation point and an equal sign (!=). 
"""
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

'''
    Checking Whether a Value Is Not in a List
    
    Other times, it’s important to know if a value does not appear in a list. 
    You can use the keyword not in this situation.
'''
banned_users = ['andrew', 'carolina', 'david']
user = 'mai'

if user not in banned_users:
    print(user + ", you can post a response if you wish.")
    
    