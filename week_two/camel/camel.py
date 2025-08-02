
#case.replace("N", "_n")

def main():
    camel = input("camelCase: ")
    snake = camel

    for letter in camel:
        if letter.isupper():
            # replace() uppercase w/ "_" & lowercase at the same time
            snake = snake.replace(letter, "_" + letter.lower())


    print("snake_case:", snake)

if __name__ == "__main__":
    main()







