

def main():
    x = get_int("What is x? ")
    print(f"x is {x}")

def get_int(prompt):
# use loop to ask what is x until its an int
    while True:
        try:
            return int(input(prompt))
#            x = int(input("What is x? "))
        except ValueError:
            pass
#            print("x is not an interger")
#        else:
#            break
#            return x
# break out of loop
main()
