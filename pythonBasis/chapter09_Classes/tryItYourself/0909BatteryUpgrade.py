# Use the final version of electric_car.py from this section. 
# Add a method to the Battery class called upgrade_battery(). 
# This method should check the battery size and set the capacity to 100 if it isn’t already. 
# Make an electric car with a default battery size, call get_range() once, 
# and then call get_range() a second time after upgrading the battery. 
# You should see an increase in the car’s range.


from electric_car import ElectricCar


myCar = ElectricCar('Tesla', 'Model 3', 2023)
print(myCar.get_descriptive_name())

myCar.battery.describe_battery()
myCar.battery.get_range()

myCar.battery.upgrade_battery()
myCar.battery.get_range()



    