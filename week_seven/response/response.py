from validator_collection import checkers

def main():
    print(validate(input("What's your email address? ")))


def validate(email):
    try:

        if checkers.is_email(email):
            return "Valid"
        else:
            return "Invalid"

    except:
        return "Invalid"



if __name__ == "__main__":
    main()



'''
def validate(email):

        if checkers.is_email(email):
            return "Valid"
        else:
            return "Invalid"

        return "Invalid"



if __name__ == "__main__":
    main()
'''




