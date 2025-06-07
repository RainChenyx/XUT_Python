"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class
# Use SongCollection class if you want to
import json
from song import Song
from operator import attrgetter

FILENAME = "songs.json"
MENU_STRING = "Menu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit"


def main():
    """
    This is the main function, the function is to display the menu, select to enter the corresponding function.
    """
    print("Song List 2.0")
    songs = load_songs(FILENAME)
    print(f"{len(songs)} songs loaded.")
    print(MENU_STRING)
    choice = get_choice()
    while choice != "Q":
        if choice == "D":
            display_songs(songs)
        elif choice == "A":
            add_song(songs)
        elif choice == "C":
            complete_song(songs)
        else:
            print("Invalid menu choice")
        print(MENU_STRING)
        choice = get_choice()
    save_songs(songs, FILENAME)
    print("Make some music!")


def load_songs(filename):
    """
    Load the contents of the JSON file, read and store it in the songs list as Song objects, and return the list.
    param FILENAME: The name of the file to load.
    return: The list of Song objects.
    """
    songs = []
    try:
        with open(filename, "r", encoding="utf8") as file_songs:
            records = json.load(file_songs)
            for record in records:
                title = record.get('title', "")
                artist = record.get('artist', "")
                year = int(record.get('year', 0))
                is_learned = record.get('is_learned', False)
                song = Song(title, artist, year, is_learned)
                songs.append(song)
    except IOError:
        print("Error loading song information")
    return songs


def get_choice():
    """
    Check menu function choice whether the input is one of A, C, D, and Q.
    """
    while True:
        try:
            choice = input(">>> ").upper()
            if choice == "A" or choice == "C" or choice == "D" or choice == "Q":
                return choice
            else:
                print("Invalid menu choice.")
        except ValueError:
            print("Please enter a valid choice.")


def display_songs(songs):
    """
    Display menu content.
    Displays a neatly formatted (arranged) list of all songs, including their details
    (unlearned songs with a * next to them) and the number of those songs.
    Param songs: The songs array.
    return: The songs array.
    """
    index = 0
    count_unlearn = 0
    for song in songs:
        index += 1
        print(f"{index}. ", end="")
        if song.is_learned is False:
            print("*", end=" ")
            count_unlearn += 1
        else:
            print(" ", end=" ")
        print(f"{song.title:<30} - {song.artist:<20} ({song.year:>4})")
    print(f"{len(songs) - count_unlearn} songs learned, {count_unlearn} songs still to learn.")


def add_song(songs):
    """
    Add song function, do not add duplicate song(title and artist and year cannot be the same).
    Param songs: The songs array.
    return: The songs array.
    """
    print("Enter details for a new song.")
    title = get_string("Title")
    artist = get_string("Artist")
    year = get_year()
    is_learned = False
    new_song = Song(title, artist, year, is_learned)
    songs.append(new_song)
    songs.sort(key=attrgetter("year"))
    print(f"{title} by {artist} ({year}) added to song list")
    return songs


def get_string(name1):
    """
    In the context of this program, the sub-function is used to get the Title and Artist
    (name1 = Title or name1 = Artist),  get the string, verify that the string cannot be blank, and return the string.
    Param name1: The string of Title or Artist
    return: The string name2.
    """
    while True:
        try:
            name2 = input(f"{name1}: ")  # name1 can be title or artist, depending on the argument.
            if name2.strip() == "":
                print("Input can not be blank.")
                continue
            return name2
        except ValueError:
            print(f"Please enter a valid {name1}.")


def get_year():
    """
    This function is used to check whether the year entered is a number and greater than 0, returning the year.
    return: The year.
    """
    while True:
        try:
            year = int(input("Year: "))
            if year > 0:
                return year
            else:
                print("Number must be > 0.")
        except ValueError:
            print("Please enter a valid number.")


def complete_song(songs):
    """
    This function is used when the user chooses to complete a song:
    allows the user to digitally select a song (error checking) and then change the status of the song to learned.
    Param songs: The songs array.
    return: The songs array.
    """
    count_unlearn = 0
    for song in songs:
        if not song.is_learned:
            count_unlearn += 1
    if count_unlearn == 0:
        print("No more songs to learn!")
        return songs
    while True:
        try:
            number = int(input("Enter the number of a song to mark as learned: "))
            if 1 <= number <= len(songs):
                break
            else:
                print("Please enter 1 - {}".format(len(songs)))
        except ValueError:
            print("Please enter a valid number.")
    index = 1
    for song in songs:
        if index == number:
            if not song.is_learned:
                song.is_learned = True
                print(f"{song.title} by {song.artist} learned.")
            else:
                print(f"You have already learned {song.title}.")
        index += 1
    return songs


def save_songs(songs, FILENAME):
    """
    This function is used to save all the elements in the array songs
    and write data that overwrites the original "songs.csv" file.
    param FILENAME: The name of the file to save.
    """
    song_all = []
    for song in songs:
        song_info = {"title": song.title, "artist": song.artist, "year": song.year, "is_learned": song.is_learned}
        song_all.append(song_info)
    try:
        with open(FILENAME, "w", encoding="utf8") as out_file:
            json.dump(song_all, out_file)
    except IOError:
        print("Error saving song information")


if __name__ == '__main__':
    main()
