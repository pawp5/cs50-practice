import sys
import csv
"""import os

# getting the name of the directory
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
parent = os.path.dirname(current)

# adding the parent directory to the sys.path.
sys.path.append(parent)

# now we can import the module in the parent directory."""
from handler import errors

def main():
    # Handles all possible errors
    if errors(sys.argv, 2, ext="csv") == None:
        write(read(sys.argv[1]))
    else:
        sys.exit(errors(sys.argv, 2, ext="csv"))


def read(file):
    # Read csv file and return dict
    info = []

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last, first = row["name"].split(",")
            info.append({"first": first.lstrip(), "last": last, "house": row["house"]})

    return info


def write(students):
    # Writes dict data into new csv file
    with open(sys.argv[2], "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})


if __name__ == "__main__":
    main()