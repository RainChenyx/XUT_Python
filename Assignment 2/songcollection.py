"""..."""
import json
from operator import attrgetter
from song import Song

STATUS_UNLEARNED = 'u'
STATUS_LEARNED = 'l'


class SongCollection:
    """
    SongCollection class for Song list.
    songs (list): A list of stored Song objects.
    """

    def __init__(self):
        """Constructor - create empty song list."""
        self.songs = []

    def __str__(self):
        """
        Return song list displayed as a string.
        return: A string form that contains a list of string representations of all songs.
        """
        return str([str(song) for song in self.songs])

    def sort(self, first_sort_key="artist"):
        """
        Sort the song list by key parameter then title.
        :first_sort_key (str, optional): Primary sorting key including "artist", "title", "year", default is "artist".
        """
        self.songs.sort(key=attrgetter(first_sort_key, "title"))

    def load_songs(self, filename):
        """
        Load JSON file and store songs as list of Song objects.
        :filename (str): The name of the JSON file to be loaded.
        """
        try:
            with open(filename, "r", encoding="utf8") as in_file:
                records = json.load(in_file)
                for record in records:
                    artist = record['artist']
                    title = record['title']
                    year = record['year']
                    is_learned = record['is_learned']
                    song = Song(title, artist, year, is_learned)
                    self.songs.append(song)
        except IOError:
            print("Error loading song information")

    def get_number_learn(self):
        """
        Gets the number of songs learned
        return: Number of songs learned.
        """
        number = 0
        for song in self.songs:
            if song.is_learned:
                number += 1
        return number

    def get_number_unlearn(self):
        """
        Gets the number of unlearned songs
        return: Number of songs unlearn.
        """
        number = 0
        for song in self.songs:
            if not song.is_learned:
                number += 1
        return number

    def add_song(self, song):
        """
        Add new songs
        :song: new song.
        """
        self.songs.append(song)

    def save_songs(self, filename):
        """
        Save added and existing music written to a json file
        :filename (str) : The name of the JSON file to save.
        """
        song_all = []
        for song in self.songs:
            song_info = {"title": song.title, "artist": song.artist, "year": song.year, "is_learned": song.is_learned}
            song_all.append(song_info)
        with open(filename, "w", encoding="utf8") as out_file:
            json.dump(song_all, out_file)
