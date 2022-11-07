def main():
    fuel_frac = input("Fraction> ")
    percent = convert(fuel_frac)
    print(gauge(percent))


def convert(fraction):
    f = fraction.split("/")

    try:
        x, y = int(f[0]), int(f[1])
    except ValueError:
        raise ValueError

    try:
        frac = x / y
    except ZeroDivisionError:
        raise ZeroDivisionError

    if x > y:
        raise ValueError
    return round(frac * 100)


def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()