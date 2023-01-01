# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    """print message from messages_list"""
    for message in messages:
        print(message)

messages_list = ['I love u', 'Ich liebe dich', '我爱你']

show_messages(messages_list)
