from numb3rs import validate
def main():
    print(test_validate(ip))


def test_validate(ip):
    assert validate('255.1.1.1') == (True)
    assert validate('256.1.1.1') == (False)
    assert validate('255.256.1.1') == (False)
    assert validate('255.1.1.256') == (False)




if __name__ == "__main__":
    main()