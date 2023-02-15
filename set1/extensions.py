def main():
    name = input("name of file? ").casefold().replace(" ", "")
    if (".gif") in name:
        print("image/gif")
    elif ("jpg") in name:
        print("image/jpg")
    elif ("jpeg") in name:
        print("image/jpeg")
    elif ("png") in name:
        print("image/gif")
    elif ("pdf") in name:
        print("application/pdf")
    elif ("txt") in name:
        print("text/plain")
    elif ("zip") in name:
        print("application/zip")
    else:
        print("application/octet-stream")
main()

