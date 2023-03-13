word = input("say hello ").replace(" ", "").casefold()
if word.startswith("hello"):
    print("$0")
elif word.startswith("h"):
    print("$20")
else:
    print("$100")