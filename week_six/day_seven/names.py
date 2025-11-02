
'''
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
'''


# create list to gather data
names = []

# iterate through over file, reading each line, stripping off \n & adding names to list
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
'''
# sort all names in memory and print them in order
for name in sorted(names):
    print(f"hello, {name}")
'''

# sort in counter alphabetical order
for name in sorted(names, reverse=True):
    print(f"hello, {name}")



'''
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
        # rstrip to strip from end of line all the white space
'''

'''
# "r" = read
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)
'''

'''
name = input("What is your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''

'''
name = input("What is your name? ")

# "w" = write
# "a" = append
file = open("names.txt", "a") # open a file named "names.txt"
file.write(f"{name}\n") # write names and separate w/ new line
file.close()
# equivalent to file, save
'''

'''
names = []

for _ in range(3):
        names.append(input("What is your name? "))

for name in sorted(names):
    print(f"hello, {name}")
'''

'''
for _ in range(3):
    name = input("What is your name? ")
    names.append(name)
'''

'''
name = input("What is your name? ")
    print(f"hello, {name}")
'''
