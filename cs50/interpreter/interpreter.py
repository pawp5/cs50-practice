exp = input(">")
list_exp = exp.split(" ")

x = float(list_exp[0])
z = float(list_exp[-1])

if list_exp[1] == "+":
    print(x + z)
elif list_exp[1] == "-":
    print(x - z)
elif list_exp[1] == "*":
    print(x * z)
elif list_exp[1] == "/" and z != 0:
    print(x / z)
