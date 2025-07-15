def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")

# both "guess" are able to work because they are in different functions
main()
