# Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

def show_messages(messages):
    """print message from messages_list"""
    for message in messages:
        print(message)

def send_messages(messages, printed_messages):
    
    while messages:
        current_messages = messages.pop()
        print(current_messages)
        printed_messages.append(current_messages)

messages_list = ['I love u', 'Ich liebe dich', '我爱你']
printed_messages = []

show_messages(messages_list)

send_messages(messages_list, printed_messages)

print(messages_list)
print(printed_messages)
