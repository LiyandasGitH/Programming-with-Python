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

