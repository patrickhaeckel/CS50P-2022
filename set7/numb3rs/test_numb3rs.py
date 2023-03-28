from numb3rs import validate
def main():
    print(test_validate(ip))


def test_validate(ip):
    assert validate('255.') == (0)
    assert validate('hola') == (20)
    assert validate('111') == (100)
    assert validate('$100') == (100)