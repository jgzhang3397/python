# Store the User class in one module, 
# and store the Privileges and Admin classes in a separate module. 
# In a separate file, create an Admin instance and call show_privileges() 
# to show that everything is still working correctly.

from _0907Admin import Admin

default_admin = Admin('snowy', 'linsing', 20, 'kassel')

default_admin.privileges.show_privileges()