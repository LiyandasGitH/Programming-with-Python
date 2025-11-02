import random


def main():

    level = get_integer()

    # random num between 1 & level
    randint = random.randint(1,level)

    # guess random num. match guess w/ randint
    guess_integer(randint)

def get_integer():
    while True:

        try:
            n = int(input("Level: "))
            if n < 0:
                continue
            return n

        except ValueError:
            continue

def guess_integer(x):
    while True:

        try:
            guess = int(input("Guess: "))
            if guess < 0:
                continue
            elif guess < x:
                print("Too small")
            elif guess > x:
                print("Too large")
            elif guess == x:
                print("Just right!")
                break

        except EOFError:
            continue


if __name__ == "__main__":
    main()




