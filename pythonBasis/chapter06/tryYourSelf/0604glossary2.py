# Now that you know how to loop through a dictionary, 
# clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls 
# with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should automatically be included 
# in the output.

glossarys = {
    'del': 'delete an element from list',
    'append()': 'add an element to list',
    'title()': 'do a title for the word',
    'lower()': 'lowercase all letters',
    'upper()': 'uppercase all letters',
    'set()': 'a set is a collection in which each item must be unique',
    'sorted()': 'use the sorted() function to get a copy of the keys in order',
    'value()': 'use the values() method to return a list of values without any keys',
}

for key, value in glossarys.items():
    print(key + "+==> " + value.title())
    
