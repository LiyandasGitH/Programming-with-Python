# fractions have numerators & denominators

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            # "map()" converts all numbers into ints
            # use split() to clean extra spaces
            num, denom = map(int, fraction.split("/"))

            if denom == 0:
                return ZeroDivisionError
            if num > denom:
                raise ValueError

            percentage = round(num / denom * 100)


            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()



'''
#percentage = numerator / denominator * 100

def main():
    fraction = input("Fraction: ")

     try:
        percentage = numerator / denominator * 100

        match fraction:
            case x / y:
                print(f"{percentage}%")

    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    main()
'''


'''
    # use loop to ask what is fraction
    while True:
        try:

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
'''
