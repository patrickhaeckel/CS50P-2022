def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False

    if s[-1].isalpha() == True:
        return False

    s = []
    for i in s:
        if s[i] in [".", ",", " "]:
            return False
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            elif s[i+1].isalpha() == True:
                return False

            else:
                break
        else:
            return True


    return True
main()

