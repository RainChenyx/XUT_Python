"""Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection


def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert song_collection.songs == []

    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.json')
    print(song_collection)
    assert len(song_collection.songs) > 0

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)

    # Test sorting songs
    print("Test sorting - year:")
    song_collection.sort("year")
    print(song_collection)
    # TODO: Add more sorting tests
    print("Test sorting - artist:")
    song_collection.sort("artist")
    print(song_collection)

    print("Test sorting - title:")
    song_collection.sort("title")
    print(song_collection)

    print("Test sorting - is_learned:")
    song_collection.sort("is_learned")
    print(song_collection)
    # TODO: Test saving songs (check file manually to see results)
    song_collection.save_songs('songs.json')
    # TODO: Add more tests, as appropriate, for each method
    '''this is test 1'''
    print("Test1 SongCollection:")
    test1_song_collection = SongCollection()
    print("Test1 loading songs:")
    test1_song_collection.load_songs('songs.json')
    print(test1_song_collection)
    print("Test1 adding new song:")
    test1_song_collection.add_song(Song("There for you", "Troye Sivan,Martin Garrix", 2016, False))
    test1_song_collection.add_song(Song("Cruel Summer", "Taylor Swift", 2019, True))
    print(test1_song_collection)
    print("Test1 sorting - artist:")
    test1_song_collection.sort("artist")
    print(test1_song_collection)
    song_collection.save_songs('songs_test1.json')

    '''this is test 2'''
    print("Test2 SongCollection:")
    test2_song_collection = SongCollection()
    print("Test2 loading songs:")
    test2_song_collection.load_songs('songs.json')
    print(test2_song_collection)
    print("Test2 adding new song:")
    test2_song_collection.add_song(Song("Find you", "G.E.M.", 2022, False))
    print(test2_song_collection)
    print("Test2 sorting - is_learned:")
    test2_song_collection.sort("is_learned")
    print(test2_song_collection)
    song_collection.save_songs('songs_test2.json')


run_tests()
