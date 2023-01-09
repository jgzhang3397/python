# You can use the replace() method to replace any word in a string with a different word. 
# Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs." 
# >>> message.replace('dog', 'cat') 
# 'I really like cats.'

# Read in each line from the file you just created, learning_python.txt, 
# and replace the word Python with the name of another language, such as C. 
# Print each modified line to the screen.

file_name = 'learning_python.txt'

with open('/Users/jingangzhang/Downloads/myWorkspace/python/pythonBasis/text_files/learning_python.txt') as file_object:
    print('\nPrint the contents once by reading in the entire file')
    lines = file_object.readlines()

for line in lines:
    replace_line = line.replace('Python', 'C')
    print(replace_line.rstrip())