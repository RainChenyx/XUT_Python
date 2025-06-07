"""(Incomplete) Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert default_song.is_learned is False
    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    # TODO: Write tests to show this initialisation works
    print(initial_song)
    # TODO: Add more tests, as appropriate, for each method
    test1_song = Song("There for you", "Troye Sivan,Martin Garrix", 2016, False)
    print(test1_song)
    test2_song = Song("Cruel Summer", "Taylor Swift", 2019, True)
    print(test2_song)
    test3_song = Song("Find you", "G.E.M.", 2022, False)
    print(test3_song)


run_tests()
