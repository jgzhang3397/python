# Start with the program you wrote for Exercise 6-1 (page 99). 
# Make two new dictionaries representing different people, 
# and store all three dictionaries in a list called people.
# Loop through your list of people. 
# As you loop through the list, print everything you know about each person.

person01 = {
    'name': 'superman',
    'age': 800,
    'height': 1.90,
    'location': 'new york',
}

person02 = {
    'name': 'batman',
    'age': 30,
    'height': 1.88,
    'location': 'gotham city',
}

person03 = {
    'name': 'ironman',
    'age': 42,
    'height': 1.75,
    'location': 'paris'
}

superheros = [person01, person02, person03]

for superhero in superheros:
    print(superhero['name'].title() + ", "+str(superhero['age']) 
          + " years old and height is " + str(superhero['height']) 
          + " m. now in " + superhero['location'].title())