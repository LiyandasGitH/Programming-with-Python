'''
def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_text = ""

    for i in range(len(word)):
        if word[i].lower() not in vowels:
            new_text += word[i]

        return new_text


if __name__ == "__main__":
    main()
'''


def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowels:
            result += char

    return result


if __name__ == "__main__":
    main()



