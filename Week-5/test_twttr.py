from twttr import shorten

def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("APPLE") == "PPL"

def test_numbers():
    assert shorten("1234") == "1234"
    assert shorten("cs50") == "cs50"

def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("what's up?") == "wht's p?"

def test_no_vowels():
    assert shorten("cry") == "cry"
