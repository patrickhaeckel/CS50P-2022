monts =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
while True:
    try:
        date = input("Date: ")
        month, day, year = date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >=1 and int(day) <= 31):
            _="_"
    except EOFError:
        print(date)
        break
