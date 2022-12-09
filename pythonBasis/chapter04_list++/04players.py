###Working with Part of a List

##Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# you would start the slice at index 1 and end at index 4:
print(players[1:4])

# If you omit the first index in a slice, 
# Python automatically starts your slice at the beginning of the list:
print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list.
print(players[2:])

# f we want to output the last three players on the roster, we can use the slice players[-3:]:
print(players[-3:])

## Looping Through a Slice
print("\nLooping Through a Slice")
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
## Copying a List
print("\nCopying a List")
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]
# friend_foods = my_foods # Instead of storing a copy of my_foods in friend_foods, 
                          # we set friend_foods equal to my_foods. 


my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


