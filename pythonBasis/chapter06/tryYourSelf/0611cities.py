# Make a dictionary called cities. 
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

cities = {
    'berlin': {
        'country': 'germany',
        'population': 200,
        'fact': 'the famous city in Germany.'
    },
    'shanghai': {
        'country': 'china',
        'population': 5000,
        'fact': 'one of famous cities in China'
    },
    'paris': {
        'country': 'franch',
        'population': 250,
        'fact': 'one of romantic cities of world'
    }
}

for city, city_info in cities.items():
    print(city.title()+": ")
    print("Locate in "+ city_info['country'].title())
    print("Has " + str(city_info['population'])+ " millions people.")
    print("It's " + city_info['fact'] +"\n")