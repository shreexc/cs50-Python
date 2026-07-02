from um import count


def test_one():
    assert count("um") == 1


def test_multiple():
    assert count("um, um, um") == 3


def test_case_insensitive():
    assert count("Um, UM, uM") == 3


def test_no_match_in_word():
    assert count("umbrella yummy vacuum") == 0


def test_no_um():
    assert count("Hello, world!") == 0
