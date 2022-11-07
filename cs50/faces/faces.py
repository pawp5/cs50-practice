def main():
    text = input("")
    print(convert(text))

def convert(item):
    item = item.replace(":)","\U0001F642")
    item = item.replace(":(", "\U0001F641")
    return item


main()