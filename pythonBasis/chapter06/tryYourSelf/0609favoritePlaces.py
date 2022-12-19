# Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, 
# and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, 
# ask some friends to name a few of their favorite places. 
# Loop through the dictionary, 
# and print each person’s name and their favorite places.

favorite_places = {
    'anna': ['tokyo', 'paris'],
    'ashiq': ['mainz', 'berlin', 'hannover'],
    'kaleb': ['darmstadt']
}

for name, places in favorite_places.items():
    print(name.title() + ", what's your favorite places?")
    if len(places) > 1:
        print("My favorite places are: ")
        for place in places:
            print(place.title())
    else:
        print("My favorite place is: ")
        for place in places:
            print(place.title())
    print("\n")  