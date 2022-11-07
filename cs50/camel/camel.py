while True:
    name = input("> ").strip()
    if name.isalpha() == True:
        break

case = ""
for char in name:
    if char.isupper():
       new = char.replace(char, "_" + char.lower())
       case += new
    else:
        case += char
print(case)