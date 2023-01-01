# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

def order_sandwiches(*sandwiches):
    """print a summary of the sanwiches that's being ordered"""
    print("\nThe followed Sandwiches habe been ordered:")
    for sandwich in sandwiches:
        print(f"- {sandwich.title()}")

order_sandwiches("chicken sandwich", "fish sandwich", 'egg sandwich')
order_sandwiches("seafood sandwich")
order_sandwiches("grilled chicken sandwich", "grilled cheese sandwich")