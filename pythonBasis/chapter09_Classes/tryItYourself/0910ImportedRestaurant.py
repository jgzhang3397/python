# Using your latest Restaurant class, store it in a module. 
# Make a separate file that imports Restaurant. 
# Make a Restaurant instance, 
# and call one of Restaurant’s methods to show that the import statement is working properly.

from _0901Restaurant import Restaurant

my_restaurant = Restaurant("china wok", 'chinesisch')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()