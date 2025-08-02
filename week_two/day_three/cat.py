'''
i = 3
while i != 0:
    print("meow")
    i = i - 1

# start counting at zero
i = 0
while i < 3:
    print("meow")
#    i = i + 1
    i += 1
'''
'''
for i in [0, 1, 2]:
    print("meow")

for _ in range(3): # _ variable if you're not gonna use it again
    print("meow")
'''

#print("meow\n" * 3, end="")
'''
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

def main():
    num = get_number()
    meow(num)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for i in range(n):
        print("meow")

main()
