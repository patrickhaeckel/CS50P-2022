import value from bank
def main():


def test_values():
    assert value('000') == ('000')
    assert value('HELLO') == ('$0')
    assert value('hi') == ('$20')
    assert value() ==