import re

name = input("What is your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    # counting starts at 1 not 0
    # := - assign value from left to right & ask a boolean question (true/false)
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


'''
name = input("What is your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    # counting starts at 1 not 0
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
'''

'''
name = input("What is your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name =  f"{first} {last}"
print(f"hello, {name}")
'''

'''
name = input("What is your name? ").strip()
if "," in name:
    last, first = name.split(", ?")
    name = f"{first} {last}"
print(f"hello, {name}")
'''

