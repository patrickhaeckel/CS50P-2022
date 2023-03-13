from bank import value
def main():
    test_casefold()


def test_casefold():

    assert value('HELLO') == ('$0')
    assert value('hola') == ('$20')
    assert value('111') == ('$100')


if __name__ == "__main__":
    main()