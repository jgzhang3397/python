'''
    Write a series of conditional tests. Print a statement describing each
    test and your prediction for the results of each test. 
    Your code should look something like this:
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
'''
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

'''
    5-2. More Conditional Tests: You don’t have to limit the number of tests you create to ten. 
    If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
    Have at least one True and one False result for each of the following:
'''

'''
    Tests for equality and inequality with strings:
'''
name1 = 'audi'
name2 = 'auDi'
print(name1 == name2) # false

'''
    Tests using the lower() method
'''
print(name1.upper() == name2.upper()) # true

'''
    Numerical tests involving equality and inequality, 
    greater than and less than, greater than or equal to, and less than or equal to
'''

num1 = 10
num2 = 20
print(num1 > num2) # false
print(num1 < num2) # true
print(num1 > num2 or num1 == num2) # false
print(num1 < num2 or num1 == num2) # true

'''
    Tests using the and keyword and the or keyword
'''
print(100 == 120 or 100 == 100) # true
print(100 == 90 and 100 == 30) # false

# Test whether an item is in a list
list = ['superman', 'ironman']
print('superman' in list) # true

# Test whether an item is not in a list
print('spiderman' in list) # false