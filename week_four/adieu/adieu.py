import inflect
p = inflect.engine()

names = []

while True:

    try:
        name = input("Name: ").strip()
        names.append(name)

    except EOFError:
        break

    n = len(names)
    message = "Adieu, adieu, to"

    if n !=0:
         print(message, p.join(names))
    else:
         exit()


'''
import inflect
p = inflect.engine()

names = []

while True:

    try:
        name = input("Name: ").strip()
        names.append(name)

    except EOFError:
        break

    n = len(names)
    message = "Adieu, adieu, to"


    if n == 1:
        print(message, names[0])
    elif n == 2:
        print(message, names[0], "and", names[1])
    else:
        index = n - 1
        last_name = names[index]
        names.append(index)
        print(message, ", ".join(names) + ", and", last_name)
'''

'''
        message = message + ",".join(names[:-1])
        message(",and" + names[:-1])
        print(message, names[0], )
'''

'''
    if n == 1:
        print(message, names[0])
    elif n == 2:
        print(message, names[0], "and" names[1])
'''

























'''
p = inflect.engine()


text = ["Adieu, adieu, to"]

while True:

    try:
        n = input("Name: ")

    except EOFError:
        print()
        break

    text.append(n)

if len(text) == 3:
    new_text = p.join(text, conj=' ')

print(new_text)
'''
