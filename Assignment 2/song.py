"""
This project is used to create the song class.
"""


# TODO: Create your Song class in this file


class Song:
    """
    Represent a Song object.
    :title (str): The title of the song.
    :artist (str): The artist of the song.
    :year (int): The year the song was released.
    :is_learned (bool): indicates the learned status of a song.
    """
    songs = []

    def __init__(self, title="", artist="", year=0, is_learned=False):
        """
        Initialise a Song instance
        :title (str, optional): The title of the song, which defaults to an empty string.
        :artist (str, optional): Artist name, default is an empty string.
        :year (int, optional): year of release. The default value is 0.
        :is_learned (bool, optional): indicates learning status. The default value is False.
        """
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned  # This is the first way to set songs as learned or unlearned by way of a file
        self.songs.append(self)

    def __str__(self):
        """
        Return a string representation of a Song object.
        :return: String representation of the song in the format "Title by Artist (Year)(Learning status)".
        """
        return f"Song: {self.title} by {self.artist} ({self.year}) [Learned: {self.is_learned}]"

    def press_song_button(self, app):
        """
        Press the corresponding song button to change the song learning status and background color
        :app: The name of the file using the kivy method
        """
        if self.is_learned:
            self.is_learned = False  # This is the second way to set the song as learned or unlearned by way of button.
            app.status_text = f"You need to learn{self.title}"
        else:
            self.is_learned = True  # This is the second way to set the song as learned or unlearned by way of button.
            app.status_text = f"You have learned {self.title}"
        app.create_song_buttons()
