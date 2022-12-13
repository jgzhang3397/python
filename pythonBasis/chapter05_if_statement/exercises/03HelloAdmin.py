"""
    Make a list of five or more usernames, including the name 'admin'. 
    Imagine you are writing code that will print a greeting to each user after they log in to a website. 
    Loop through the list, and print a greeting to each user:
"""
usernames = ['admin', 'superman', 'ironman', 'batman', 'spiderman']
for username in usernames:
    if username == 'admin' :
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
    
'''
    5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
'''
if usernames:
    for username in usernames:
        if username == 'admin' :
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")