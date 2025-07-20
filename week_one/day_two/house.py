name = input("What's your name? ")

'''
if name == "Robb" or name == "Jon" or name == "Bran":
    print("Stark")
elif name == "Daenerys":
    print("Targaryen")
elif name == "Tyrion":
    print("Lannister")
elif name == "Theon":
    print("Greyjoy")
else:
    print("Who?")
'''

match name:
    case "Robb" | "Jon" | "Bran":
        print("Stark")
#    case "Jon":
#        print("Stark")
#    case "Bran":
#        print("Stark")
    case "Dany":
        print("Targaryen")
    case _: # whatever has not yet been handled
        print("Who?")


