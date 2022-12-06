# Looping Through an Entire List

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)


# Doing More Work Within a for Loop

for magician in magicians:
    print(magician.title() + ", that a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")