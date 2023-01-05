# An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the 
# Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). 
# Either version of the class will work; just pick the one you like better. 

# Add an attribute called flavors that stores a list of ice cream flavors. Write a method that
# displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

from _0901Restaurant import Restaurant

class IceCreamStand(Restaurant):
    ''' son class inherits present class Restaurant'''
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream_flavors = ['banana', 'chocolate', 'vanilla']
    
    def display_flavors(self):
        '''display these flavors'''
        for flavor in self.ice_cream_flavors:
            print(f"The flavor is {flavor}.")
            
# create an instance
my_IceCreamStand = IceCreamStand('The cold of summer', 'chinese')

# call the method
my_IceCreamStand.describe_restaurant()
my_IceCreamStand.display_flavors()        

