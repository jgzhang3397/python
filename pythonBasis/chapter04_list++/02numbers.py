### Making Numerical Lists

##  Using the range() Function

# range() function makes it easy to generate a series of numbers
# The range() function causes Python to start counting at the first value you give it, 
# and it stops when it reaches the second value you provide. 
# Because it stops at that second value, 
# the output never contains the end value, which would have been 5 in this case.
for value in range(1, 6):
    print(value)


## Using range() to Make a List of Numbers

# If you want to make a list of numbers, 
# you can convert the results of range() directly into a list using the list() function.
numbers = list(range(1, 6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a given range.
numbers01 = list(range(1, 10, 2))
print(numbers01)
