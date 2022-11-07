import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+$)", ip.strip())

    count = 1
    if matches:
        for _ in range(4):
            if 0 <= int(matches[count]) <= 255:
                count += 1
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()