
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    while True:

        try:
            item = input("Item: ").title()
            if price(item):
                break
        except EOFError:
            print()
            break

def price(item):
    if item in menu:
        print(f"Total: ${menu[item]:.2f}")
        return True
    else:
        return False

main()

