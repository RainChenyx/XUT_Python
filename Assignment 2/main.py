"""
This program is a simple song list that allows users to track songs
The songs they wish to learn and the songs they have finished learning.
The program reads and writes a list of songs in a file. Every song has:
Users can choose to display a list of songs.
The song list can be sorted by year, title, author name.
Users can add new songs and mark (set) learned songs.
Create both a console program and a Graphical User Interface (GUI) program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from songcollection import SongCollection
from song import Song
from kivy.uix.button import Button


class SongListApp(App):
    """
    Create a SongListApp class
    """
    status_text = StringProperty()
    total_text = StringProperty()
    sort_by = StringProperty()
    SORT_KEYS = ["Artist", "Title", "Year"]

    def __init__(self, **kwargs):
        """
        Constructor - set up the model data.
        """
        super().__init__(**kwargs)
        self.song_collection = SongCollection()
        self.song_collection.load_songs("songs.json")

    def build(self):
        """
        Build the Kivy GUI.
        """
        self.title = "Song List 2.0"
        self.root = Builder.load_file('app.kv')
        self.create_song_buttons()
        self.song_collection.sort("year")  # Sort songs by year when they are first loaded
        self.root.ids.spinner.text = "Year"  # Change the text of the spinner button to Year at the beginning
        self.root.bind(on_key_down=self.handle_key_down)  # When the tab key is pressed, the handle key down will run.
        return self.root

    def on_stop(self):
        """
        Save the song file when the application stops
        """
        self.song_collection.save_songs("songs.json")  # The song data is automatically saved when the process ends

    def create_song_buttons(self):
        """This function is used to create buttons for each song"""
        # first remove existing buttons
        self.root.ids.songs_box.clear_widgets()
        self.total_text = f"Time to work hard"
        for song in self.song_collection.songs:  # Create each song button as well as color and text content
            if song.is_learned is False:
                song_button = Button(text=f"{song.title} by {song.artist}({song.year})")
            else:
                song_button = Button(text=f"{song.title} by {song.artist}({song.year})(learned)")
            song_button.bind(on_press=lambda instance, s=song: s.press_song_button(self))  # Bind events that is taken.
            self.root.ids.songs_box.add_widget(song_button)
            if song.is_learned:
                song_button.background_color = (1, 1, 0, 1)  # Set the song button color
            else:
                song_button.background_color = (0, 1, 1, 1)  # Set the song button color
        number_learned = self.song_collection.get_number_learn()
        number_unlearned = self.song_collection.get_number_unlearn()
        self.total_text = f"To learn: {number_unlearned}    Learned: {number_learned}"

    def press_sort(self, text):
        """
        Handle pressing sort button; sort and display songs.
        """
        self.sort_by = text
        self.sort(self.sort_by)
        self.create_song_buttons()

    def sort(self, text):
        """
        Sort song collection based on selection.
        """
        # convert on-screen text to attribute for sorting
        key = text.lower()
        self.song_collection.sort(key)
        self.create_song_buttons()

    def handle_key_down(self, keycode):
        """
        Pressing the Tab key should move between the text fields
        """
        if keycode[1] == 'tab':  # To determine whether the pressed key is Tab
            current_focus = self.root.focus
            if current_focus == self.root.ids.added_title:
                self.root.ids.added_artist.focus = True
            elif current_focus == self.root.ids.added_artist:
                self.root.ids.added_year.focus = True
            elif current_focus == self.root.ids.added_year:
                self.root.ids.added_title.focus = True
            return True
        return False

    def press_add(self, add_title, add_artist, add_year):
        """
        Press the Add Song button to add the title, artist, year of their song and save it to the songs.json file.
        :add_title (str): Song title entered by the user.
        :add_artist (str): The artist name entered by the user.
        :add_year (str): The year of the song's release entered by the user (as a string).
        """
        checked_values = self.add_check(add_title, add_artist, add_year)  # Verify that the song format is correct
        if checked_values:
            added_title, added_artist, added_year = checked_values
            song = Song(added_title, added_artist, int(added_year))
            self.song_collection.add_song(song)
            self.song_collection.sort("year")
            self.handle_clear()
            self.create_song_buttons()
            self.song_collection.save_songs("songs.json")  # Add songs and buttons and save to file

    def add_check(self, title, artist, year):
        """
        The input title, artist, title is checked, and an error message is displayed in status_text
        :title (str): The title of the song.
        :artist (str): Name of the artist.
        :year (str): The year the song was released (as a string).
        :return: value of title, artist, year or None
        """
        if title != "" and artist != "" and year != "":
            try:
                if int(year) > 0:  # Check that the year is entered correctly
                    return title, artist, year
                elif int(year) <= 0:
                    self.status_text = "Year must be > 0"
                    return None
                else:
                    self.status_text = "Please enter a valid number"
                    return None
            except ValueError:
                self.status_text = "Please enter a valid number"
                return None
        else:
            if title == "" or artist == "" or year == "":
                self.status_text = "All fields must be completed"
                return None

    def handle_clear(self):
        """
        Clear the status_text.
        """
        self.root.ids.added_title.text = ""
        self.root.ids.added_artist.text = ""
        self.root.ids.added_year.text = ""
        self.status_text = ""


if __name__ == '__main__':
    SongListApp().run()

# Tests (All methods in classes are tested appropriately) in the file (test_main.py)

"""
Function with error checking pattern

function do_task(input)
    if input has error 1
        display error message 1
        return
    if input has error 2
        display error message 2
        return
    do task (knowing we don't have any of the above errors)
"""
