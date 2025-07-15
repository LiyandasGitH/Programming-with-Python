#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# Ask user for their name
#name = input("What's your name? ").strip().title()

# Remove whitespace from str & capitalise user's name
#name = name.strip().title()

# Capitalise user's name
#name = name.capitalize()

# Capitalise first letter
#name = name.title()

# Split user's name into first & last name
#first, last = name.split(" ")

# Say hello to user
#print("hello, ")
#print("hello, " + name)
#print("hello, ", name)
#print("hello,", name)
#print("hello, ", end="")
#print("hello,", name, sep="no")
#print('hello, "friend"')
#print('hello, \"friend\"')
#print(name)
#print(f"hello, {name}")
#print(f"hello, {first}")

'''DEFINING FUNCTIONS'''

#def hello(to="world"):
#    print("hello,", to)

def main():

#hello()
    name = input("What's your name? ")
    hello(name)
#(name)

def hello(to="world"):
    print("hello,", to)

main()



def main():
    print("hello, world!")
    print("This is a test file.")

main()
