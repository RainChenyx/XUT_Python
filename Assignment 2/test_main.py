from main import SongListApp


def run_tests():
    """Tests for main.py 's add_check method."""
    print("Testing main,py 's add_check method...")
    app = SongListApp()

    # Test normal case
    print("Test normal:")
    result = app.add_check("Song Title", "Artist Name", "2023")
    assert result == ("Song Title", "Artist Name", "2023")
    print("Normal test passed.")

    # Test year 0
    print("Test year 0:")
    result = app.add_check("Song Title", "Artist Name", "0")
    assert app.status_text == "Year must be > 0"
    assert result is None
    print("Year 0 test passed.")

    # Test cases where the year is not numerical
    print("Test non-numerical year:")
    result = app.add_check("Song Title", "Artist Name", "abc")
    assert app.status_text == "Please enter a valid number"
    assert result is None
    print("Non-numerical year test passed.")

    # Test for empty fields
    print("Test empty fields:")
    result = app.add_check("", "Artist Name", "2023")
    assert app.status_text == "All fields must be completed"
    assert result is None
    print("Empty fields test passed.")

    print("All tests for add_check method completed.")


run_tests()
