import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ").strip().capitalize()
    except EOFError:
        print()
        break
    else:
        names.append(name)

print("Adieu, adieu, to", p.join(names))