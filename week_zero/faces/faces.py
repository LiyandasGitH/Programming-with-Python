'''
text = ":)"


def convert(text):

    Replace emoticons w/ emoji.
    :) - 🙂 & :( - 🙁
    if text == ":)":
        return "🙂"
    elif text == ":(":
        return "🙁"
    else:
        return "Unrecognised text"

def main():
    global text
    user_input = input("Enter text here: ")

main()
'''

def convert(text):
    # Use replace() 
    return text.replace(":)", "🙂").replace(":(", "🙁")
    # Replaces emoticons w/ emoji

def main():
    user_input = input()
    print(convert(user_input))

main()
