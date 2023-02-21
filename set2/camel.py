def main():
       v = input("name of variable ").split()
       for i in v:
              print(i)
              if i.isupper():
                     print("_" + i)

main()

