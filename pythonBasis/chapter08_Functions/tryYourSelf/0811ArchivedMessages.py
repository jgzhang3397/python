# Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, 
# print both of your lists to show that the original list has retained its messages.


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

# copy the original list
send_messages(messages_list[:], printed_messages)

print(messages_list)
print(printed_messages)
