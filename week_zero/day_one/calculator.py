#round(number[, ndigits])

#x = int(input("What's x? "))
#y = int(input("Whats's y? "))

#x = float(input("What's x? "))
#y = float(input("Whats's y? "))

#z = int(x) + int(y)
#z = round(x + y)
#z = x / y
#z = round(x / y, 2)
#print(f"{z:,}")
#print(f"{z:.2f}")
#print(x + y)
#print(int(input("What's x? ")) + int(input("Whats's y? ")))


'''DEFINING FUNCTIONS W/ RETURNS'''

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
#    return n * n
#    return n ** 2
    return pow(n, 2)


main()