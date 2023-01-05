# An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
# or Exercise 9-5 (page 167). 
# Add an attribute, privileges,
# that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of privileges. 
# Create an instance of Admin, and call your method.

from _0903Users import User

class Admin(User):
    '''a class called Admin that inherits from the User class '''
    
    def __init__(self, first_name, last_name, age, location):
        '''initialization'''
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        '''lists the administrator’s set of privileges. '''
        for privilege in self.privileges:
            print(f"The Admin {privilege}.")

myAdmin = Admin('Snowy', 'Linsing', 20, 'Mainz')
myAdmin.describe_user()
myAdmin.show_privileges()
        