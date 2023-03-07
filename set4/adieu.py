# implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with commas and one and, as in the below:
dict = {}
while True:
    try:
        name = input("Names here ")
    except EOFError:
        for i in dict:
            print(dict[name])

