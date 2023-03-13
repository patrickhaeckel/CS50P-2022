from twttr import shorten
def main():
    test_str()
    test_lower()
    test_upper()
    test_both()


def test_str():
    assert shorten('4') == '4'

def test_lower():
    assert shorten('twitter') == 'twtr'

def test_upper():
    assert shorten('TWITTER') == 'TWTTR'

def test_both():
    assert shorten('TwItTeR') == 'TwtTR'
main()