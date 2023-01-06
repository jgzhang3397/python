# Start with your work from Exercise 9-8 (page 173). 
# Store the classes User, Privileges, and Admin in one module. 
# Create a separate file, make an Admin instance, 
# and call show_privileges() to show that everything is working correctly.

from _0908Privileges import Admin
# from _0908Privileges import Privileges

default_Admin = Admin('snowy', 'linsing', 18, 'darmstadt')
default_Admin.describe_user()
default_Admin.greet_user()

default_Admin.privileges.show_admin_privileges()