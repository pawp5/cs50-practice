month = [
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
    date = input("Date> ").capitalize().strip()

    try:
        mon, day, year = date.split("/")
    except ValueError:
        pass
    else:
        try:
            day, mon = int(day), int(mon)
        except ValueError:
            pass
        else:
            if int(mon) <= 12 and int(day) <= 31:
                print(f"{year}-{str(mon).zfill(2)}-{str(day).zfill(2)}")
                break

    try:
        mon, day, year = date.split(" ")
    except ValueError:
        pass
    else:
        if "," in day:
            day = day.removesuffix(",")
            try:
                day = int(day)
            except ValueError:
                pass
            else:
                if mon in month and int(day) <= 31:
                    num_mon = str(month.index(mon)+1)
                    print(f"{year}-{num_mon.zfill(2)}-{str(day).zfill(2)}")
                    break