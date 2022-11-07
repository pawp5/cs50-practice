while True:
    fuel = input("Fraction> ")
    l_fuel = fuel.split("/")

    try:
        frac = 100 * int(l_fuel[0]) / int(l_fuel[1])
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if frac <= 100:
            if 99 <= frac < 101:
                print("F")
            elif 0 <= frac <= 1:
                print("E")
            else:
                print(str(round(frac)) + "%")
            break