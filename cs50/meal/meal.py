def main():
    time = input("What is the time> ")
    t = convert(time)

    if 7.0 <= t <= 8.0 :
        print("Breakfast time")
    elif 12.0 <= t <= 13.0:
        print("Lunch time")
    elif 18.0 <= t <= 19.0:
        print("Dinner time")


def convert(time):
    if "a" in time:
        t, min = time.strip().split(":")
        min = min.split("a")
        return 0 + float(min[0])/60 if t == "12" else float(t) + float(min[0])/60
    elif "p" in time:
        t, min = time.strip().split(":")
        min = min.split("p")
        return 12 + float(min[0])/60 if t == "12" else 12 + float(t) + float(min[0])/60
    else:
        t, min = time.strip().split(":")
        return float(t) + float(min)/60


if __name__ == "__main__":
    main()