#  Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py, 
# and modify the file to use the imported functions.


# due to a circular import sum() don't run
import _0815PrintingFunctions as pf

def print_models(msg):
    print(msg)

num = pf.sum(10, 20)
print(num)    