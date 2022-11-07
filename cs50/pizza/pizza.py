import sys
import csv
from tabulate import tabulate


def main():
    if errors(sys.argv) == None:
        print(tabulate(read(), headers="firstrow", tablefmt="grid"))
    else:
        sys.exit(errors(sys.argv))


def read():
    lines = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)

    return lines


def errors(file, ext):
    # command-line error checker
    if len(file) > 2:
        return "Too many arguments"
    elif len(file) < 2:
        return "Too few arguments"


    try:
        # read file by line
        lines = file[1]
    except FileNotFoundError:
        return "File does not exist"
    else:
        text = file[1].split(".")
        if text[-1] != ext.lower():
            return f"Not a {ext.upper()} file"


if __name__ == "__main__":
    main()