groceries = {}

while True:
    try:
        item = input("").upper()
    except EOFError:
        print()
        break
    else:
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

key_list = [i for i in groceries]
key_list.sort()

for i in key_list:
    print(groceries[i], i)