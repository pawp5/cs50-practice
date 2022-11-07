def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    twttr = ""
    for char in word:
        if char in "aeiouAEIOU":
            pass
        else:
            twttr += char
    return twttr


if __name__ == "__main__":
    main()