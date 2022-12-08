# For example, consider how you might make a list of the first 10 square numbers 
# (that is, the square of each integer from 1 through 10).

# In Python, two asterisks (**) represent exponents. 

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

## Simple Statistics with a List of Numbers
# For example, you can easily find the minimum, maximum, and sum of a list of numbers:

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

## List Comprehensions
# The approach described earlier for generating the list squares 
# consisted of using three or four lines of code. 
# A list comprehension allows you to generate this same list in just one line of code.
squares = [value ** 2 for value in range(1, 11)]
print(squares)