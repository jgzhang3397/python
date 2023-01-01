# Using a program you wrote that has one function in it, 
# store that function in a separate file. 
# Import the function into your main program file, 
# and call the function using each of these approaches:



# from module_name import *

# import module_name as mn
import _0816Functions as func

# from module_name import function_name
from _0816Functions import subtract 

# from module_name import function_name as fn 
from _0816Functions import sum as s

# from module_name import *
from _0816Functions import *

result = func.sum(10, 20)
print(result)

result = subtract(10, 20)
print(result)

result = s("hello", "world")
print(result)

print(np.abs(-1))
