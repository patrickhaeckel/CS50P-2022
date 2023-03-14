def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    if s[-1].isalpha() == True:
        return False
    s = []

    for i in s:
        lista = {"."}
        if i[s] in lista:
            return False
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            elif s[i+1].isalpha() == True:
                return False

            else:
                break


    return True
main()

