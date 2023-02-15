def main():
    name = input("name of file? ").casefold().replace(" ", "")
    if name.endswith(".gif"):
        print("image/gif")
    elif name.endswith(".jpeg"):
        print("image/jpeg")
    elif name.endswith(".jpg"):
        print("image/jpeg")
    elif name.endswith(".png"):
        print("image/png")
    elif name.endswith(".pdf"):
        print("application/pdf")
    elif name.endswith(".txt"):
        print("text/plain")
    elif name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
main()

