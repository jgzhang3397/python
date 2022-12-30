# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, 
# and a shirt of any size with a different message.

def make_shirt(shirt_message="I love Python", shirt_size="L"):
    """"""
    print("This is a " + shirt_size.title() + " size shirt with " + shirt_message)

make_shirt()
make_shirt(shirt_size="M")

make_shirt(shirt_size="s", shirt_message="I love Cpp")