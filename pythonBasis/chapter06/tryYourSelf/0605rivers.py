#  6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.

dic_rivers_countries = {
    'nile': 'egypt',
    'changjiang': 'china',
    'donau': 'germany',
}

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, country in dic_rivers_countries.items():
    print(river.title() + " runs though " + country.title())

# Use a loop to print the name of each river included in the dictionary.
for river in dic_rivers_countries.keys():
    print(river.upper())

# Use a loop to print the name of each country included in the dictionary.
for country in dic_rivers_countries.values():
    print(country.title())