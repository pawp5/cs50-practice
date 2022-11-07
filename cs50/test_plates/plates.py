def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) < 7:
        if s.isalpha():
            return True
        # Checks if s is only alphanumeric ie NO PUNCTUATOINS
        if s.isalnum() and s[0:2].isalpha():
            if num_order(s):
                return True
    return False


def num_order(s):
    # List of all numbers in s
    int_list = []
    for i in s:
        if i.isdigit():
            int_list.append(i)

    # Confirms that first numbers is not zero
    if int_list[0] != "0":
        # Checks if the s number sequence matches the list
        p = s.find(int_list[0])   # index of first number in s
        num_str = "".join(int_list)   # str of numbers in s in order

        if num_str == s[p:]:
            return True


if __name__ == "__main__":
    main()