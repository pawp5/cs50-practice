import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours := re.search(r"(\d+)(?:\:(\d+))? (\w+) to (\d+)(?:\:(\d+))? (\w+)", s.strip()):
        details = [hours[i] for i in range(7)]
        h = validate(details)
    else:
        raise ValueError

    return f"{h[0]}:{h[1]} to {h[2]}:{h[3]}"


def validate(stuff):
    spread = []
    i = 1
    while i < 5:
        if int(stuff[i]) not in range(1,13):
            raise ValueError
        else:
            if stuff[i+2] == "AM":
                if stuff[i] == "12":
                    spread.append("00")
                else:
                    spread.append(stuff[i].zfill(2))
            elif stuff[i+2] == "PM":
                if stuff[i] == "12":
                    spread.append("12")
                else:
                    spread.append(str(int(stuff[i])+12))
            else:
                raise ValueError

        if stuff[i+1] == None:
            spread.append("00")
        elif int(stuff[i+1]) in range(60):
            spread.append(stuff[i+1])
        else:
            raise ValueError

        i += 3

    return spread


if __name__ == "__main__":
    main()