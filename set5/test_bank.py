from bank import value
def main():
    test_values()


def test_values():
    assert value('HELLO') == (None)
    assert value('HELLO') == ('$0')
    assert value('hOLA MARCO') == ('$20')

if __name__ == "__main__":
    main()