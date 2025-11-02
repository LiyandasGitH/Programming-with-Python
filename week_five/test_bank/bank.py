
def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

'''
def main():
    greeting = input("Enter greetng here: ").strip().lower()

    if greeting.startswith("hello"):
        # startswith() checks if word starts with "hello"
        print("$0")
    elif greeting.startswith("h"):
        # startswith() checks if word starts with "h"
        print("$20")
    else:
        print("$100")

main()
'''
