from word_count.core import tokenize

def test_tokenize():
    line = "Hello, World!"
    assert tokenize(line) == ["hello", "world"]
