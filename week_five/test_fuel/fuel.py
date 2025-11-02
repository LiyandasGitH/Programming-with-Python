# find a way to catch for negative numbers in convert
# i keep failing the check50 test

def main():
    num = input("Fraction: ")
    percentage = convert(num)
    print(gauge(percentage))


def convert(num):
    while True:

        try:

            index = num.find("/") # find index of "/" [1]
            x = int(num[:index]) # find index of numerator [0:1]
            y = int(num[index+1:]) # find index of denominator [2:]
            fraction = x / y

            if x < 0 or y < 0:
                raise ValueError

            if y == 0:
                raise ZeroDivisionError


            if x > y:
                num = input("Fraction: ")
                continue

            else:
                percentage = int(fraction * 100)
                return percentage


        except (ValueError, ZeroDivisionError):
            raise



def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"



if __name__ == "__main__":
    main()


'''
def main():
    num = input("Fraction: ")
    convert(num)


def convert(fraction):
    while True:

        fraction = input("Fraction: ")


        try:
            x, y = map(int, fraction.split("/"))

            if y == 0:
                return ZeroDivisionError

            if x > y:
                raise ValueError

            if x < 0 or y < 0:
                raise ValueError


        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    percentage = round(x / y * 100)

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"





if __name__ == "__main__":
    main()
'''



'''
# fractions have numerators & denominators

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x = int(numerator)
            y = int(denominator)
            # "map()" converts all numbers into ints
            # use split() to clean extra spaces
            x, y = map(int, fraction.split("/"))

            if y == 0:
                return ZeroDivisionError
            if x > y:
                raise ValueError
            if x < 0 or y < 0:
                raise ValueError

            percentage = round(x / y * 100)

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def gauge(percentage):


            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return "f{percentage}%"
            break



if __name__ == "__main__":
    main()
'''


