from random import randint


def main():
    level = get_level()

    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        solution = sum([x,y])

        tries = 0
        while tries < 3:
            tries += 1
            try:
                reply = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            else:
                if solution == reply:
                    score += 1
                    break
                else:
                    print("EEE")
        if solution != reply:
            print(f"{x} + {y} = {solution}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0 < level < 4:
                return level


def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError

    if level == 3:
        x = randint(100, 999)
        y = randint(100, 999)
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    else:
        x = randint(0, 9)
        y = randint(0, 9)
    return x, y


if __name__ == "__main__":
    main()