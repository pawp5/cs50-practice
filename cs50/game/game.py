from random import randint

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level > 0:
            break

rand_num = randint(1, level)
print(rand_num)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > 0:
            if guess < rand_num:
                print("Too small!")
            elif guess > rand_num:
                print("Too large!")
            else:
                print("Just right!")
                break
