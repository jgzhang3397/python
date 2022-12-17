# Use the code in favorite_languages.py (page 97)
# Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that are not.

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
}

# Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take the poll.
friends = ['ashiq', 'sarah', 'phil']

for name in friends:
    if name in favorite_languages.keys():
        print("thanke you " + name.title() + ", but you have already taken the poll.")
    else:
        print(name.title() + ", please take the poll")
    