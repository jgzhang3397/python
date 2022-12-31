# Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, 
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() 
# that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, 
# add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, num_games = None):
    albums = {"Artist's name" : artist_name, "Album's title" : album_title}
    if num_games:
        albums['Number of games'] = num_games
    return albums

album01 = make_album('ps5', 'the God of War IV', num_games=1)
album02 = make_album('xbox s', 'sekiro')
album03 = make_album('xbox x', 'it takes two')

print(album01)
print(album02)
print(album03)

