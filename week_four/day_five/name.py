import sys



if len(sys.argv) < 2:
    sys.exit("Too fews arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)



'''
if len(sys.argv) < 2:
    sys.exit("Too fews arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
'''


'''
# check for the things we're worried about
# use conditionals

if len(sys.argv) < 2:
    print("Too fews arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
'''


'''
try:
    print("hello, my name is", sys.argv[1])

except IndexError:
    print("Too fews arguments")
'''


'''
print("hello, my name is", sys.argv[1])
'''
