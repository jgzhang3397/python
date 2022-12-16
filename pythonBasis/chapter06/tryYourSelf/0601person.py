# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

person = {
    'first_name': 'snoowy',
    'last_name' : 'none',
    'age' : 1.5,
    'city' : 'Mainz',
}

print("my cat, she's first_name is " + person['first_name'])
print(f"her last name is {person['last_name']}")
print(f"She is {person['age']} years old")
print('She lives in ' + person['city'])