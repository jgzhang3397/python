# Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city_name, city_country="China"):
    """_summary_

    Parameters
    ----------
    city_name : _type_
        _description_
    city_country : str, optional
        _description_, by default "China"
    """
    print(city_name.title() + " is in " + city_country.title())

describe_city("Beijing")
describe_city(city_name="Shanghai")

describe_city(city_country="germany", city_name="beilin")
describe_city(city_name="darmstadt", city_country="germany")