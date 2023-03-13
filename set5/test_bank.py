from bank import value
def main():
    test_values()


def test_casefold():

    assert value('HELLO') == ('$0')
    assert value('hola') == ('$20')
    assert value('000') == ('$100')


if __name__ == "__main__":
    main()