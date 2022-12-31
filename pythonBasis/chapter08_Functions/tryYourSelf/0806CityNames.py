# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city_name, country_name, location=''):
    """return city-country pairs"""
    return f"{city_name}, {country_name}"

print(city_country("Darmstadt", "Germany").title())


