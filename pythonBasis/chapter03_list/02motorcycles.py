motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles[0] = 'ducati'

print(motorcycles)

motorcycles.append('honda') # The append() method at adds 'honda' to the end of the list 
# without affecting any of the other elements in the list

print(motorcycles)

print('\n=================================')

motorcycles01 = []
motorcycles01.append('honda')
motorcycles01.append('yamaha')
motorcycles01.append('suzuki')
print(motorcycles01)

print('\nInserting Elements into a List')
motorcycles01.insert(0, 'ducati')
print(motorcycles01)

print('\nRemoving an Item Using the del Statement')
del motorcycles01[0]
print(motorcycles01)
del motorcycles01[1]
print(motorcycles01)

print('\nPopping Items from any Position in a List')
motorcycles02 = ['honda', 'yamaha', 'suzuki']
print(motorcycles02)
popped_motorcycle = motorcycles02.pop()
print(motorcycles02)
print(popped_motorcycle)

print('\nPopping Items from any Position in a List')
motorcycles03 = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles03.pop(0)
print('The first motorcycle i owned was a ' + first_owned.title())

# If you’re unsure whether to use the del statement or the pop() method, 
# here’s a simple way to decide: when you want to delete an item from a list 
# and not use that item in any way, use the del statement; 
# if you want to use an item as you remove it, use the pop() method.

print('\nRemoving an Item by Value')
motorcycles04 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles04)
motorcycles04.remove('ducati')
print(motorcycles04)

motorcycles04.append('ducati')
print(motorcycles04)
too_expensive = 'ducati'
motorcycles04.remove('ducati')
print(motorcycles04)
print(too_expensive + ' is too expensive for me.')
