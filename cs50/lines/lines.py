import sys


def main():
    # error checker
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        # read file by line
        lines = read(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(counter(lines))


def read(file_name):
    code = []

    with open(file_name) as file:
        for line in file:
            code.append(line.strip())
    return code


def counter(file_list):
    count = 0

    for line in file_list:
        if len(line) < 1:
            pass
        elif line[0] == "#":
            pass
        else:
            count += 1

    return count


if __name__ == "__main__":
    main()