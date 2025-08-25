

def main():
    groceries = {}

    try:
        while True:
            item = input().strip().lower()
            if item:
                groceries[item] = groceries.get(item, 0) + 1

    except EOFError:
        print()


#def groceries(item):
    for item in sorted(groceries):
        count = groceries[item]
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()


