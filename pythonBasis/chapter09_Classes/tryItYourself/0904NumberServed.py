# Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, 
# and then change this value and print it again.

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
        self.number_served = 0
    
    def describe_restaurant(self):
        """print the infos of restaurant"""
        print(f"\nThe name of restaurant is {self.rest_name}.")
        print(f"It's a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        """indicate the restaurant is open."""
        print(f"{self.rest_name.upper()} is now open.")
    
    # Add a method called set_number_served() that lets you set the number of customers that have been served. 
    # Call this method with a new number and print the value again.
    def set_number_served(self, new_number):
        '''set the number of customers that have been served. 
            restrict the change of new_number <= 0
        '''
        if new_number > 0:
            self.number_served = new_number
            print(f"The number of customers changes to {self.number_served}")
    
    # Add a method called increment_number_served() that 
    # lets you increment the number of customers who’ve been served. 
    # Call this method with any number you like that could represent how many customers were served in, 
    # say, a day of business.
    def increment_number_served(self, increment_number):
        '''increment the number of customers who’ve been served.'''
        self.number_served += increment_number
        if increment_number > 0 or increment_number == 0:
            print(f"It increases to {self.number_served}")
        else:
            print(f"It decreases to {self.number_served}")
        
        
    
my_restaurant = Restaurant('Jins house', 'chinese')
print(f"The number of customers in {my_restaurant.rest_name.title()} is {my_restaurant.number_served}")

my_restaurant.number_served = 20
print(f"Now, it rises to {my_restaurant.number_served}")

my_restaurant.set_number_served(30)

my_restaurant.increment_number_served(2)

my_restaurant.increment_number_served(-10)



        