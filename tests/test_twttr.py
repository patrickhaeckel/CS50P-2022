from twttr import shorten
def test_numb():
    assert shorten (4) == 4

def test_str():
    assert shorten ("4") == "4"