# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical
# order.
visit_places = ['china', 'japan', 'berlin', 'london', 'america']

# Print your list in its original order. 
# Don’t worry about printing the list neatly, just print it as a raw Python list.
print(visit_places)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(visit_places))

# Show that your list is still in its original order by printing it.
print(visit_places)

# Use sorted() to print your list in reverse alphabetical order 
# without changing the order of the original list.
print(sorted(visit_places, reverse=True))

# Show that your list is still in its original order by printing it again.
print(visit_places)

# Use reverse() to change the order of your list. 
# print the list to show that its order has changed.
visit_places.reverse()
print(visit_places)

visit_places.reverse()
print(visit_places)

# Use sort() to change your list so it’s stored in alphabetical order. 
# Print the list to show that its order has been changed.
visit_places.sort()
print(visit_places)

#  Use sort() to change your list so it’s stored in reverse alphabetical order. 
#  Print the list to show that its order has changed.
visit_places.sort(reverse=True)
print(visit_places)

print(str(len(visit_places)) + ' in this list')


# Intentional Error: If you haven’t received an index error in one of your programs yet, 
# try to make one happen.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(str(len(motorcycles)) + " in the list")
print(motorcycles)
print(motorcycles[-1])

motorcycles.pop()
print(str(len(motorcycles)) + " in the list")
print(motorcycles)
print(motorcycles[-1])

del motorcycles[0]
print(str(len(motorcycles)) + " in the list")
print(motorcycles)
print(motorcycles[-1])

motorcycles.pop(0)
print(str(len(motorcycles)) + " in the list")
print(motorcycles)
 # print(motorcycles[-1]) # IndexError: list index out of range



