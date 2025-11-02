def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):

    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False


    for i in range(len(s)):
        if s[i].isdigit():

            if s[i] == "0":
                return False

            if not s[i:].isdigit():
                return False

            break

    return True

if __name__ == "__main__":
    main()





'''

def is_valid(s):
    # ACII 'A' 65 - 'Z' 90
    letters = [chr(i) for i in range (65, 91)]
    numbers = [str(i) for i in range(10)]

    # plate must be more than 2 & less than 6
    if len(s) < 2 or len(s) > 6:
        return False

    # plate char should come from lists in letters & numbers
    for char in s:
        if char not in letters and char not in numbers:
            return False


    # index 0 or 1 should start with letter
    if s[0] not in letters or s[1] not in letters:
        return False

    # make sure '0' doesn't appear at the start of plate(s)
    number_started = False
    for char in s:
        if char in numbers:
            if not number_started:
                number_started = True
                if char == "0":
                    return False

        elif number_started:
            return False

    else:
        return True

main()


'''
