import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        attempt = 0

        while attempt < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == result:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
            # catch EOFError so program doesn't crash before it finishes
            except (ValueError, EOFError):
                print("EEE")
                attempt += 1

        if attempt == 3:
            print(f"{x} + {y} = {result}")

    print(score)


def get_level():
    while True:
        try:

            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            return level

        except ValueError:
            continue


def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

'''
    # returns None by default, number cannot be 1, 2 & 3 at same time
    if level == 1 and level == 2 and level == 3:
        return random.randint(0, 9)
    else:
        return
'''

if __name__ == "__main__":
    main()
