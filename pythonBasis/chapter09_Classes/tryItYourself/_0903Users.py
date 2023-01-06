# Make a class called User. 
# Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.

class User:
    """a class about user profile"""
    
    def __init__ (self, first_name, last_name, age, location):
        """ initalization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        
    
    def describe_user(self):
        """ prints a summary of the user’s information."""
        print("\nPrint the users infomations:")
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Age: {self.age}" )
        print(f"Location: {self.location.title()}")
    
    def greet_user(self):
        """ greeting to the user"""
        print(f"{self.last_name.title()} {self.first_name.title()}, you are {self.age} years old and in {self.location.title()}. ich grüße dich!")


# user = User('snowy', 'zhang', 2, 'mainz')
# user.describe_user()
# user.greet_user()