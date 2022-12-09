### Tuples
# Lists work well for storing collections of items 
# that can change throughout the life of a program. 

# Python refers to values that cannot change as immutable, 
# and an immutable list is called a tuple.

# When compared with lists, tuples are simple data structures.
# Use them when you want to store a set of values that 
# should not be changed throughout the life of a program.

## Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

## Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)

## Writing over a Tuple
print("Original dimensions:") 
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions: 
    print(dimension)