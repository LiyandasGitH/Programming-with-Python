
def main():
    coke_price = 50
    amount_due = coke_price

    while amount_due > 0:
            print(f"Amount Due: {amount_due}")
            coin = int(input("Insert Coin: "))
            #if insert is not in list
            if coin in [25, 10, 5]:
                  amount_due -= coin

    if amount_due < 0:
      # abs() somehow minuses?
      print(f"Change Owed: {abs(amount_due)}")

    else:
        print("Change Owed: 0")

main()

'''

            else:
                  print(input("Insert Coin: "))

            if inserted_price < coke_price:
                  print(f"Amount Due: {coke_price - inserted_price}")

            elif inserted_price > coke_price:
                  print(f"Change Owed: {inserted_price - coke_price}")
            else:
                break

main()

coke price = 50

def main():
    price = int(input("Insert Coin: "))
    remainder(price)


def remainder(price):
    # if price is not 50/25/10/5, try to return input?
    if price != [50, 25, 10, 5]:
        print(input("Insert Coin: "))
    elif price == 25:
        return "Change Owed: 25"
    print(input("Insert Coin: "))
    elif price == 10:
        return "Change Owed: 40"
    print(input("Insert Coin: "))

main()
def remainder(price):
    if price == 50:
        print("Change Owed: 0")
    elif price == 25:
        return "Change Owed: 25"
    elif price == 10:
        return
'''
