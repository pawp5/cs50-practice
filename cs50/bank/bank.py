greetings = input("Hey, what's up?").lower().strip()

if greetings.startswith("hello"):
    print("$0")
elif greetings.startswith("h"):
    print("$20")
else:
    print("$100")