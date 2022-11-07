coin_inserted, amount_due = 0, 50

while coin_inserted < 50:
    while True:
        print("Amount Due:", amount_due)
        inserted = int(input("Insert Coin: "))
        if inserted in (25,10,5):
            coin_inserted += inserted
            amount_due -= inserted
            break

print("Change Owed:", coin_inserted - 50)