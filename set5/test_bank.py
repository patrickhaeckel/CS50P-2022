from bank import value
def main():
    test_values()


def test_values():
    assert value('000') == ('None')
    assert value('HELLO') == ('$0')
    assert value('hola') == ('$20')

if __name__ == "__main__":
    main()