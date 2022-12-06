cars = ['bmw', 'audi', 'toyota', 'subaru']

# The sort() method, changes the order of the list permanently. 
cars.sort()

print(cars)

# You can also sort this list in reverse alphabetical 
# order by passing the argument reverse=True to the sort() method. 
# the order of the list is permanently changed:
cars.sort(reverse= True)

print(cars)

print("\n==========Sorting a List Temporarily with the sorted() Function===========")

cars01 = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars01)

print("\nHere is the sorted list:") 
print(sorted(cars01))

print("\nHere is the original list again:") 
print(cars01)

print("\nHere is the reserve sorted list:") 
print(sorted(cars01, reverse= True))

print("\nHere is the original list again:") 
print(cars01)

print("\n===========Printing a List in Reverse Order==========")

cars02 = ['bmw', 'audi', 'toyota', 'subaru']
print(cars02)

# Notice that reverse() doesn’t sort backward alphabetically; 
# it simply reverses the order of the list:
# The reverse() method changes the order of a list permanently
cars02.reverse()
print(cars02)

print("\n============Finding the Length of a List=============")
cars04 = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars04))

