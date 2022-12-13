'''
    Do the following to create a program that simulates how websites 
    ensure that everyone has a unique username.
'''
'''
    * Make a list of five or more usernames called current_users.
'''
current_users = ['Superman', 'Ironman', 'Spiderman', 'Batman', 'Black widow']

'''
    * Make another list of five usernames called new_users. Make sure one
    or two of the new usernames are also in the current_users list
'''
new_users = ['batMan', 'ironMan', 'huLk', 'thOr', 'captain america']

'''
    Loop through the new_users list to see if each new username has already been used. 
    If it has, print a message that the person will need to enter a new username. 
    If a username has not been used, print a message saying that the username is available.
'''
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user}, you need a new username.")
    else:
        print(f"{new_user}, The username is available.")

'''
    Make sure your comparison is case insensitive. 
    If 'John' has been used, 
    'JOHN' should not be accepted. 
    (To do this, you’ll need to make a copy of current_users containing the lowercase versions of 
    all existing users.)
'''
print("=================================")
copy_current_users = []

for current_user in current_users:
    copy_current_users.append(current_user.lower())
    
for new_user in new_users:
        if new_user.lower() in copy_current_users:
            print(f"{new_user}, you need a new username.")
        else:
            print(f"{new_user}, The username is available.")

