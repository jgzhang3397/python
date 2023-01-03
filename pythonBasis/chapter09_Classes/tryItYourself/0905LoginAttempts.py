# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() 
# that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.


# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, 
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
class User:
    """a class about user profile"""
    
    def __init__ (self, first_name, last_name, age, location, login_attempts = 0):
        """ initalization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts
    
    def increment_login_attempts(self):
        '''increments the value of login_attempts  '''
        self.full_name = f"{self.first_name.title()} {self.last_name.title()}"
        
        self.login_attempts += 1
        print(f"{self.full_name} has try to login for {self.login_attempts} times. ")
    
    def reset_login_attempts(self):
        '''resets the values of login_attempts to 0'''
        self.login_attempts = 0
        print(f"The value of login attempts have been reset to {self.login_attempts}")
        
    
    def describe_user(self):
        """ prints a summary of the user’s information."""
        print("\nPrint the users infomations:")
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Age: {self.age}" )
        print(f"Location: {self.location.title()}")
    
    def greet_user(self):
        """ greeting to the user"""
        print(f"{self.first_name.title()} {self.last_name.title()}, you are {self.age} years old and in {self.location}. ich grüße dich!")


user = User('snowy', 'zhang', 2, 'mainz')
user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()
