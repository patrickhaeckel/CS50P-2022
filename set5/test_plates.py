from plates import is_valid
def main():
    test_lenght()
    test_beginningalpha()
    test_lenght()
    test_numplacement()
    test_zeroplacement()
    test_alphanumeric()

def test_beginningalpha():
    assert is_valid('cs50') == True

def test_lenght():
    assert is_valid('w') == False
    assert is_valid('wwwwwww') == False

def test_numplacement():
    assert is_valid('C205') == False
    assert is_valid('cs50p') == False

def test_zeroplacement():
    assert is_valid('CS05') == False

def test_alphanumeric():
    assert is_valid('CS.50') == False

if __name__ == "__main__":
    main()



