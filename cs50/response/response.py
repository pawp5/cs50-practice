from validator_collection import checkers


def main():
    if is_valid(input("Email: ")):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if checkers.is_email(s):
        return True


if __name__ == "__main__":
    main()