# Write a function called make_shirt() that accepts a size and 
# the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

def make_shirt(shirt_size):
    """print a sentence summarizing the size of the shirt and the message printed on it."""
    print("\nThe size of shirt is " + shirt_size.title())
    print("Nike==>Just do it:)")

# using positional arguments
make_shirt("m")

# using key arguments
make_shirt(shirt_size="l")