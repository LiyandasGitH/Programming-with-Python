'''
# Ask user for greetings
greeting = input("Aren't you gonna greet? ").lower().strip()

print("HELLO, WORLD!")
'''
'''
def greet(input):
    if "HELLO, WORLD!" in input:
        return "hello, world!"
    else:
        return "Are you gonna greet?"

greeting = greet("HELLO. WORLD!")
print(greeting)
'''

# Ask user for input
user_input = input("Please enter text here: ")

# Return input in lowercase
print(user_input.lower())
