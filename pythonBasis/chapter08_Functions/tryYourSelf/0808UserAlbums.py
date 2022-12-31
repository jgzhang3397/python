# Start with your program from Exercise 8-7. Write a while loop that allows
# users to enter an album’s artist and title. Once you have that information, 
# call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, num_games = None):
    albums = {"Artist's name" : artist_name, "Album's title" : album_title}
    if num_games:
        albums['Number of games'] = num_games
    return albums

while True:
    print("\nPlease enter an album's artust and title:")
    print("(enter 'q' to exit)")
    artist_name = input("Artist's name: ")
    if artist_name == 'q' or album_title == 'q':
        break
    
    album_title = input("Album's title: ")
    if artist_name == 'q' or album_title == 'q':
        break
    my_album = make_album(artist_name=artist_name, album_title=album_title)
    print(my_album)