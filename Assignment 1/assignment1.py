"""
This program is a simple song list that allows a user to track songs
that they wish to learn and songs they have completed learning.
The program reads and writes a list of songs in a file. Each song has:
title, artist, year, whether it is learned Users can choose to display the list of songs.
The song list should be sorted by year then by title (use operator.itemgetter) for sorting.
Users can add new songs and mark (set) songs as learned.
They cannot change songs from learned to unlearned.
"""

from operator import itemgetter

FILENAME = "songs.csv"
MENU_STRING = "Menu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit"


def main():
    """
    This is the main function, the function is to display the menu, select to enter the corresponding function.
    """
    print("Song List 1.0")
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
    Load the contents of the file, read and store it in the songs array, and return songs.
    param FILENAME: The name of the file to load.
    return: The songs array.
    """
    songs = []
    try:
        file_songs = open(filename, "r")
        for line in file_songs:
            information = line.strip().split(",")
            songs.append(information)
        file_songs.close()
        songs.sort(key=itemgetter(2))
    except IOError:
        print("Error saving song information")
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
        if song[3] == "u":
            print("*", end=" ")
            count_unlearn += 1
        else:
            print(" ", end=" ")
        print(f"{song[0]:<30} - {song[1]:<20} ({song[2]:<4})")
    print(f"{len(songs) - count_unlearn} songs learned, {count_unlearn} songs still to learn.")


def add_song(songs):
    """
    Add song function, do not add duplicate song(title and artist and year cannot be the same).
    Param songs: The songs array.
    return: The songs array.
    """
    print("Enter details for a new song.")
    new_song = []
    title = get_string("Title")
    new_song.append(title)
    artist = get_string("Artist")
    new_song.append(artist)
    year = get_year()
    new_song.append(year)
    for song in songs:
        if are_songs_same(song, new_song):
            print("The song is already in it, please do not add it again.")
            return songs
    situation = "u"
    new_song.append(situation)
    songs.append(new_song)
    songs.sort(key=itemgetter(2))
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
            year = input("Year: ")
            if int(year) > 0:
                return year
            else:
                print("Number must be > 0.")
        except ValueError:
            print("Please enter a valid number.")


def are_songs_same(song, new_song):
    """
    This function checks if the song has the same title and artist and year as entered by the user.
    Param song: The song array.
    Param new_song: The new song array.
    return: True if the song has the same title and artist and year as entered by the user.
    """
    if (song[0].lower().strip() == new_song[0].lower().strip()
            and song[1].lower().strip() == new_song[1].lower().strip()
            and song[2].lower().strip() == new_song[2].lower().strip()):
        return True
    else:
        return False


def complete_song(songs):
    """
    This function is used when the user chooses to complete a song:
    allows the user to digitally select a song (error checking) and then change the status of the song to learned.
    Param songs: The songs array.
    return: The songs array.
    """
    count_unlearn = 0
    for song in songs:
        if song[3] == "u":
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
            if song[3] == "u":
                song[3] = "l"
                print(f"{song[0]} by {song[1]} learned.")
            else:
                print(f"You have already learned {song[0]}.")
        index += 1
    return songs


def save_songs(songs, FILENAME):
    """
    This function is used to save all the elements in the array songs
    and write data that overwrites the original "songs.csv" file.
    param FILENAME: The name of the file to save.
    """
    try:
        songs_file = open(FILENAME, "w")
        for song in songs:
            songs_file.write(song[0] + "," + song[1] + "," + song[2] + "," + song[3] + "\n")
        songs_file.close()
    except IOError:
        print("Error saving song information")


if __name__ == '__main__':
    main()

"""
Here are good patterns that you must follow.

Menu:
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>

Error checking:
<priming read - get some input>
while <input is bad>
    display error message
    <same as the priming read again - get some input>
do next thing now that you know the input is valid

Exception-based error checking (for valid numbers):
(example)
is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)
"""
