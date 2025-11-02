import re

email = input("What is your email? ").strip()



if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    # \w - built-in word char (alphanumetric & underscore symbol)
    # (\w+\.)? - optional for 0/1 repetition "?" for group inside brackets "()"
    print("Valid")
else:
    print("Invalid")


# (r"^[a-zA-Z0-9_ ]+@[a-zA-Z0-9_ ]+\.edu$", email) - alphabets with spaces
# (r"^(\w|\s)+@[a-zA-Z0-9_]+\.edu$", email) - alphaets with spaces
# (r"^\w+@\w+\.(com|gov|net|net|edu)$", email) - can have different

'''
# "r" - raw string
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    # [] - set of chars allowed
    print("Valid")
else:
    print("Invalid")
'''


'''
# "r" - raw string
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    # [^@] - any char except an "@"
    # ^ - start
    # & - end
    # \ - "escape key" so email can end in ".edu"
    print("Valid")
else:
    print("Invalid")
'''




'''
# "r" - raw string
if re.search(r"^.+@.+\.edu$", email):
    # ^ - start
    # & - end
    # \ - "escape key" so email can end in ".edu"
    print("Valid")
else:
    print("Invalid")
'''


'''
username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
'''



'''
if "@" in email and "." in email:
    print("Valid")

else:
    print("Invalid")
'''
