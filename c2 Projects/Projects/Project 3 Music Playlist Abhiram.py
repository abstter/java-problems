"""
Project 3: Music Playlist Creator
Student Code: Base Project and Enhancements
Python Level 3
"""
# Abhiram Avasarala D14
# 11/17/23
import random

# Song library is a dictionary of dictionaries.
# Keys are song titles and values are dictionaries with each song's details.
song_library = {
    "Moon Cheese": {
        "Artist": "Galactic Mice",
        "Album": "Space Rats",
        "Year": "2023",
        "Genre": "Electronic",
        "Duration": 300
    },
    "Dance of the Marshmallows": {
        "Artist": "Sugar Symphony",
        "Album": "Candy Orchestra",
        "Year": "2022",
        "Genre": "Classical",
        "Duration": 270
    },
    "The Lonely Broccoli": {
        "Artist": "Veggie Vibes",
        "Album": "Kitchen Jams",
        "Year": "2021",
        "Genre": "Pop",
        "Duration": 210
    },
    "The Mysterious Sock": {
        "Artist": "Laundry Legends",
        "Album": "Washing Tunes",
        "Year": "2024",
        "Genre": "Rock",
        "Duration": 240
    },
    "Under the Bed": {
        "Artist": "Monster Melodies",
        "Album": "Nightmare Notes",
        "Year": "2023",
        "Genre": "Alternative",
        "Duration": 180
    },
    "Pajama Party on Pluto": {
        "Artist": "Starry Siblings",
        "Album": "Planetary Playtime",
        "Year": "2024",
        "Genre": "Dance",
        "Duration": 330
    }
}

# Playlists dictionary will hold all playlists.
# Each playlist will be a list of strings (song titles).
playlists = {}


def print_song_library():
    """ Display the entire song library as a table. """
    
    print("\nSong Library:")
    print("=" * 101)  # Line separator
    
    # Print column headings with field widths (left-justified by default):
    print(f"   {'Title':27} {'Artist':18} {'Album':20} {'Year':6}",
          f"{'Genre':13} Duration")
    print("=" * 101)  # Line separator
    
    # Loop over the songs to print them. First enumerate the songs so that
    # we can display song numbers for easy user selection:
    for i, song_title in enumerate(song_library.keys(), 1):
        # First get the dictionary containing that song's details:
        song_details = song_library[song_title]
        
        # Now, get the song's details from that dictionary:
        artist, album = song_details["Artist"], song_details["Album"]
        year, genre = song_details["Year"], song_details["Genre"]
        duration = song_details["Duration"]  # whole number of seconds
        
        # Calculate minutes and seconds using integer division and remainder:
        minutes, seconds = duration // 60, duration % 60
        
        # Output that song's details using their columns' field widths:
        print(f"{i:<2} {song_title:27} {artist:18} {album:20}",
              f"{year:6} {genre:13} {minutes:2}:{seconds:02}")


def print_playlists():
    """ Display all playlists with song titles, artists, and durations. """
    
    print("\nPlaylists:")
    
    # Loop over the playlists to print them. First enumerate the playlists
    # so that we can display playlist numbers for easy user selection:
    for i, playlist_name in enumerate(playlists, 1):
        print(f"\n{i}. {playlist_name}:")
        print("-"*60)  # Line separator
        
        # Print column headings for the playlist with field widths:
        print(f"   {'Title':27} {'Artist':18} Duration")
        print("-"*60)
        
        # Call print_playlist() to print the current playlist:
        print_playlist(playlist_name)


def print_playlist(playlist_name):
    # Loop over the songs to print them. First enumerate the songs so that
    # we can display song numbers for easy user selection:
    for i, song_title in enumerate(playlists[playlist_name], 1):
        # First get the dictionary containing that song's details:
        song_details = song_library[song_title]
        
        # Now, get the song's details from that dictionary:
        artist, album = song_details["Artist"], song_details["Album"]
        year, genre = song_details["Year"], song_details["Genre"]
        duration = song_details["Duration"]  # whole number of seconds
        
        # Calculate minutes and seconds using integer division and remainder:
        minutes, seconds = duration // 60, duration % 60
        
        # Output that song's details using their columns' field widths:
        print(f"{i:<2} {song_title:27} {artist:18} {minutes:2}:{seconds:02}")

def create_playlist():
    global playlists, print_playlist
    print("Playlists: ")
    print("\n")
    # This is the input statement for the new playlist
    name = input("Enter the name of the new playlist: ")
    # Check if name is in playlist or not
    if name in playlists:
        print("This playlist already exists.")
    else:
        playlists[name] = []
        # F string to print out the name
        print(f"Playlist {name} created!")
def add_song_to_playlist():
    """Prompt user to add a song to a chosen playlist"""
    
    print_playlists()
    playlist_num = int(input("\nChoose a playlist number: "))
    
    # Convert the playlist keys view object to a list and then retrieve the
    # playlist name in the list using the user-selected playlist number:
    playlist_names = list(playlists.keys())
    playlist_name = playlist_names[playlist_num - 1]
    
    print_song_library()
    song_num = int(input("\nChoose a song number to add: "))
    
    # Get the song title by converting the song library keys view object to a
    # list and then finding the string at the chosen song number:
    song_titles = list(song_library.keys())
    song_title = song_titles[song_num - 1]
    
    # Get the playlist from the dictionary of playlists and add the song to it:
    playlist = playlists[playlist_name]
    playlist.append(song_title)
    
    print(f"Song '{song_title}' added to playlist '{playlist_name}'!")


def remove_song_from_playlist():
    print_playlists()
    # This input statement chooses a playlist num to remove
    playlist_num = int(input("\nChoose a playlist number to remove: "))
    # Convert the playlist keys view object to a list and then retrieve the
    # playlist name in the list using the user-selected playlist number:
    playlist_names = list(playlists.keys())
    playlist_name = playlist_names[playlist_num - 1]
    song_num = int(input("\nChoose a song number to remove: "))
    if playlists[playlist_name] == []:
        print("Playlist is empty. Retry.")
    else:
        # Get the playlist from the dictionary of playlists and remove the song to it:
        playlist = playlists[playlist_name]
        playlist.pop(song_num-1)
        
        # print statement to remove playlist
        print(f"Song '{song_num}' removed from playlist '{playlist_name}'!")
        


def search_songs():
    """ OPTIONAL ENHANCEMENT:
        Search for songs by any of their details.
        
        > Prompt the user for a search term and search each song detail
          (including the song title) to see if it contains the search term
          as a substring (e.g., 'dance' is found as part of a song title
          and as a genre).
          
        > Display every matched song along with all its song details.  
    """
    print("\n *** OPTIONAL ENHANCEMENT: Song Search ***\n")
    print("This is currently just a stub.")
    

def main():
    """ Present the main menu of choices in a loop, prompting the user to
        select the next playlist operation. """
    
    print("\nWelcome to the Music Playlist Creator!")
    print("Please choose one of the following options at a time.")
    
    while True:
        print("\nMain Menu:")
        print("----------------------------")
        print("1. Display Song Library")
        print("2. Display Playlists")
        print("3. Create Playlist")
        print("4. Add Song to Playlist")
        print("5. Remove Song from Playlist")
        print("6. Shuffle Playlist")
        print("7. Search Songs")
        print("8. Quit")
        print("----------------------------")
        choice = input("Choose an option (1-8): ")
        if choice == "1":
            print_song_library()
        elif choice == "2":
            print_playlists()
        elif choice == "3":
            create_playlist()
        elif choice == "4":
            add_song_to_playlist()
        elif choice == "5":
            remove_song_from_playlist()
        elif choice == "6":
            shuffle_playlist()
        elif choice == "7":
            search_songs()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
'''
Welcome to the Music Playlist Creator!
Please choose one of the following options at a time.

Main Menu:
----------------------------
1. Display Song Library
2. Display Playlists
3. Create Playlist
4. Add Song to Playlist
5. Remove Song from Playlist
6. Shuffle Playlist
7. Search Songs
8. Quit
----------------------------
Choose an option (1-8): 3
Playlists: 


Enter the name of the new playlist: dog
Playlist dog created!

Main Menu:
----------------------------
1. Display Song Library
2. Display Playlists
3. Create Playlist
4. Add Song to Playlist
5. Remove Song from Playlist
6. Shuffle Playlist
7. Search Songs
8. Quit
----------------------------
Choose an option (1-8): 4

Playlists:

1. dog:
------------------------------------------------------------
   Title                       Artist             Duration
------------------------------------------------------------

Choose a playlist number: 1

Song Library:
=====================================================================================================
   Title                       Artist             Album                Year   Genre         Duration
=====================================================================================================
1  Moon Cheese                 Galactic Mice      Space Rats           2023   Electronic     5:00
2  Dance of the Marshmallows   Sugar Symphony     Candy Orchestra      2022   Classical      4:30
3  The Lonely Broccoli         Veggie Vibes       Kitchen Jams         2021   Pop            3:30
4  The Mysterious Sock         Laundry Legends    Washing Tunes        2024   Rock           4:00
5  Under the Bed               Monster Melodies   Nightmare Notes      2023   Alternative    3:00
6  Pajama Party on Pluto       Starry Siblings    Planetary Playtime   2024   Dance          5:30

Choose a song number to add: 1
Song 'Moon Cheese' added to playlist 'dog'!

Main Menu:
----------------------------
1. Display Song Library
2. Display Playlists
3. Create Playlist
4. Add Song to Playlist
5. Remove Song from Playlist
6. Shuffle Playlist
7. Search Songs
8. Quit
----------------------------
Choose an option (1-8): 4

Playlists:

1. dog:
------------------------------------------------------------
   Title                       Artist             Duration
------------------------------------------------------------
1  Moon Cheese                 Galactic Mice       5:00

Choose a playlist number: 1

Song Library:
=====================================================================================================
   Title                       Artist             Album                Year   Genre         Duration
=====================================================================================================
1  Moon Cheese                 Galactic Mice      Space Rats           2023   Electronic     5:00
2  Dance of the Marshmallows   Sugar Symphony     Candy Orchestra      2022   Classical      4:30
3  The Lonely Broccoli         Veggie Vibes       Kitchen Jams         2021   Pop            3:30
4  The Mysterious Sock         Laundry Legends    Washing Tunes        2024   Rock           4:00
5  Under the Bed               Monster Melodies   Nightmare Notes      2023   Alternative    3:00
6  Pajama Party on Pluto       Starry Siblings    Planetary Playtime   2024   Dance          5:30

Choose a song number to add: 6
Song 'Pajama Party on Pluto' added to playlist 'dog'!

Main Menu:
----------------------------
1. Display Song Library
2. Display Playlists
3. Create Playlist
4. Add Song to Playlist
5. Remove Song from Playlist
6. Shuffle Playlist
7. Search Songs
8. Quit
----------------------------
Choose an option (1-8): 2

Playlists:

1. dog:
------------------------------------------------------------
   Title                       Artist             Duration
------------------------------------------------------------
1  Moon Cheese                 Galactic Mice       5:00
2  Pajama Party on Pluto       Starry Siblings     5:30

Main Menu:
----------------------------
1. Display Song Library
2. Display Playlists
3. Create Playlist
4. Add Song to Playlist
5. Remove Song from Playlist
6. Shuffle Playlist
7. Search Songs
8. Quit
----------------------------
Choose an option (1-8): 1

Song Library:
=====================================================================================================
   Title                       Artist             Album                Year   Genre         Duration
=====================================================================================================
1  Moon Cheese                 Galactic Mice      Space Rats           2023   Electronic     5:00
2  Dance of the Marshmallows   Sugar Symphony     Candy Orchestra      2022   Classical      4:30
3  The Lonely Broccoli         Veggie Vibes       Kitchen Jams         2021   Pop            3:30
4  The Mysterious Sock         Laundry Legends    Washing Tunes        2024   Rock           4:00
5  Under the Bed               Monster Melodies   Nightmare Notes      2023   Alternative    3:00
6  Pajama Party on Pluto       Starry Siblings    Planetary Playtime   2024   Dance          5:30

Main Menu:
----------------------------
1. Display Song Library
2. Display Playlists
3. Create Playlist
4. Add Song to Playlist
5. Remove Song from Playlist
6. Shuffle Playlist
7. Search Songs
8. Quit
----------------------------
Choose an option (1-8): 5

Playlists:

1. dog:
------------------------------------------------------------
   Title                       Artist             Duration
------------------------------------------------------------
1  Moon Cheese                 Galactic Mice       5:00
2  Pajama Party on Pluto       Starry Siblings     5:30

Choose a playlist number to remove: 1

Choose a song number to remove: 2
Song '2' removed from playlist 'dog'!
'''