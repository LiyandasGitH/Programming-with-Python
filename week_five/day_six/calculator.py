
def main():
    x = input("What is x? ")
    print("x squared is", square(x))

def square(n):
    return n * n


# ensure that when importing from another file/library,
# make sure main does not call itself
# call main only conditionally
if __name__ == "__main__":
    main()
