from numb3rs import validate
def main():
    print(test_casefold())


def test_validate():
    assert validate('HELLO') == (0)
    assert validate('hola') == (20)
    assert validate('111') == (100)
    assert validate('$100') == (100)