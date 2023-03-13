from bank import value
def main():
    test_values()


def test_values():
    assert value('000') == (None)
    assert value('HELLO') == ('$0')
    assert value('hOLA MARCO') == ('$20')
    assert value(None) == ('$0')

if __name__ == "__main__":
    main()