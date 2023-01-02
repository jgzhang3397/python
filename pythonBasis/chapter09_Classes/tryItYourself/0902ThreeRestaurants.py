# Start with your class from Exercise 9-1. 
# Create three different instances from the class, 
# and call describe_restaurant() for each instance.

from _0901Restaurant import Restaurant as rest 

restaurant01 = rest('palmen grill', 'turkey')
restaurant01.describe_restaurant()

restaurant02 = rest('cafe chaos', 'germany')
restaurant02.describe_restaurant()

restaurant03 = rest('das krü', 'vietnam')
restaurant03.describe_restaurant()