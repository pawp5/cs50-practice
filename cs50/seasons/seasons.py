import re
from sys import exit
import datetime

import inflect

p = inflect.engine()


def main():
    birthday = input("DOB> ").strip()
    print(p.number_to_words(minutes(format(birthday)), andword="").capitalize() + " minutes")


def format(date):
    if match := re.match(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", date):
        try:
            return datetime.date(int(match[1]), int(match[2]), int(match[3]))
        except ValueError:
            exit("Invalid date")
    else:
        exit("Invalid date")


def minutes(birthday):
    today = datetime.date.today()
    #print(today - birthday)
    return abs(today - birthday).days * 1440


if __name__ == "__main__":
    main()