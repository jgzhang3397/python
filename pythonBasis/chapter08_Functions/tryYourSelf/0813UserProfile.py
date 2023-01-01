# Start with a copy of user_profile.py from page 149. 
# Build a profile of yourself by calling build_profile(), 
# using your first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **infos):
    infos['first_name'] = first
    infos['last_name'] = last
    return infos
 
user_profile = build_profile('snowy', 'katze', 
                                loaction = 'Darmstadt',
                                age = 24,
                                weight = str(78.8)+"kg")

print(user_profile)

