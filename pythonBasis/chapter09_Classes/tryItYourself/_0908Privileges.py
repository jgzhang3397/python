# Write a separate Privileges class. 
# The class should have one attribute, privileges, 
# that stores a list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.


class Privileges():
    '''a separate Privileges class.'''
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        '''lists the administrator’s set of privileges. '''
        for privilege in self.privileges:
            print(f"The Admin {privilege}.")

# class Admin(User):
#     def __init__(self, first_name, last_name, age, location):
#         super().__init__(first_name, last_name, age, location)
#         self.privileges = Privileges()

# your_Admin = Admin('luna', 'marko', '8', 'kassel')

# your_Admin.describe_user()

# your_Admin.privileges.show_admin_privileges()