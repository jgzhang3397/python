# Make a class Die with one attribute called sides, 
# which has a default value of 6. 
# Write a method called roll_die() that prints a random number 
# between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint
class Die:
    ''' a simple class Die'''
    def __init__(self, sides = 6, roll_times = 1):
        self.sides = sides
        self.roll_times = roll_times
        
    
    def roll_die(self):
        while self.roll_times >= 1:
            random_num = randint(1, self.sides)
            print(random_num)
            self.roll_times -= 1
            
print("Make a 6-sided die and roll it 10 times.")
my_die = Die(6, 10)
my_die.roll_die()
print("\nMake a 10-sided die, roll each die 10 times.")
my_die = Die(10, 10)
my_die.roll_die()
