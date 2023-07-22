amount = 50
print("Amount Due: 50")
while True:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        if coin > amount:
            change = coin - amount
            print("Change Owed: " + str(change))
            break
        else:
            amount = amount - int(coin)
            if amount != 0:
                print("Amount Due: " + str(amount))
    else:
        print("Amount Due: " + str(amount))
    if amount == 0:
        print("Change Owed: 0")
        break