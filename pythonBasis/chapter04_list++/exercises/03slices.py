# Using one of the programs you wrote in this chapter, 
# add several lines to the end of the program that do the following:

# Print the message The first three items in the list are:. 
# Then use a slice to print the first three items from that program’s list.
list = ['starlord', 'ironman', 'superman', 'betman', 'snowy']
print("The first three items in the list are:")
for hero in list[:3]:
    print(hero.title())


# Print the message Three items from the middle of the list are:. 
# Use a slice to print three items from the middle of the list.
print("\nThree items from the middle of the list are:")
for hero in list[1:4]:
    print(hero.title())
    
# Print the message The last three items in the list are:. 
# Use a slice to print the last three items in the list.
print("\n The last three items in the list are:.")
for hero in list[-3:]:
    print(hero.title())

list02 = list[:]
list.append('panda')
list02.append('eagle')

for hero in list:
    print(hero)
print("\n====")
for hero02 in list02:
    print(hero02)
