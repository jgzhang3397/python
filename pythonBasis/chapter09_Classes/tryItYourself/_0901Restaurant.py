# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.

# Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.

class Restaurant:
    """a class about restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """_summary_

        Parameters
        ----------
        restaurant_name : _type_
            _description_
        cuisine_type : _type_
            _description_
        """
        self.rest_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """print the infos of restaurant"""
        print(f"\nThe name of restaurant is {self.rest_name}.")
        print(f"It's a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        """indicate the restaurant is open."""
        print(f"{self.rest_name.upper()} is now open.")

my_restaurant = Restaurant("Jin's house", 'chinese')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
    