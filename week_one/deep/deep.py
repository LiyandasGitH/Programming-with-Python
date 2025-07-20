'''
def main():
    question = input("What is the Great Question of Life, the Universe, and Everthing? ")
    response(question)

def response(answer):
    if answer == "42":
        print("Yes")
    elif answer == "Forty Two":
        print("Yes")
    elif answer == "forty-two":
        print("Yes")
    else:
        print("No")

main()
'''



# shorter and more effcient
def main():
    question = input("What is the Great Question of Life, the Universe, and Everthing? ")
    print(check_answer(question))

def check_answer(response):
    if response == "42" or response == "Forty Two" or response == "forty-two":
        return "Yes"
    else:
        return "No"

main()

