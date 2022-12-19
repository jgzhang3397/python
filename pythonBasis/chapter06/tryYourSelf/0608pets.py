# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, 
# loop through your list and as you do, print everything you know about each pet.

cat = {
    'name': 'snowy',
    'age': 1.5,
    'name of owner': 'anna'
}

dog = {
    'name': 'hashi',
    'age': 3,
    'name of owner': 'isabella'
}

pets = [cat, dog]

for pet in pets:
    print(pet)