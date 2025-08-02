WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to the Spelling Bee!")
    # word, points = key, value
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")



#    print("Your letters are: A I P C R H G")

main()

'''
    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")


        # TODO: Check if guess in dictionary
        if guess == "GRAPHIC":
            WORDS.clear() # clear(), removes all letters available
            print("You've won!")
        if guess in WORDS.keys():
#           WORDS.pop(guess)
# pop() gives value of key then remove same key
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")

    print("That's the game!")
'''
