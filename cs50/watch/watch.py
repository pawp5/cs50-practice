import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)"', s.strip(), re.IGNORECASE):
        return "https://youtu.be/" + url[1]


if __name__ == "__main__":
    main()