import sys


def main():

    if len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


    filename = sys.argv[1]

    if not filename.endswith("py"):
        sys.exit("Not a python file")

    try:
        with open(filename) as file:
            nlines = 0
            for line in file:
                if line.lstrip() != "" and not line.lstrip().startswith("#"):
                    nlines += 1
        print(nlines)
    except FileNotFoundError:
        sys.exit("File not found")

def count_lines(filename):
    count = 0
    in_docstring = False

    with open(filename) as file:
        for line in file:
            if not line.lstrip().startswith(("'''", '"""')):
                if line.lstrip().count("'''") == 2 or line.lstrip('"""') == 2:
                    continue
                in_docstring = not in_docstring
                continue

            if in_docstring:
                continue

            count += 1

    return count

if __name__ == "__main__":
    main()



'''
    with open(sys.argv[1]) as file:
        nlines = 0
        for line in file:
            if not line.lstrip().startswith("#") and line.lstrip() != " ":
                nlines += 1
    print(cal_len(nlines))


def cal_len():
    while True:
        try:

            if len(sys.argv) == 2:
                if sys.argv[1][-2:] == "py":
                    return main
                elif sys.argv[1][-2:] != "py":
                    sys.exit("Not a python file")


            else:
                raise FileNotFoundError

        except FileNotFoundError:
            sys.exit("File not found")



if __name__ == "__main__":
    main()
'''


'''
# test.py
if len(sys.argv) == 2:
    if sys.argv[1][-2:] == "py":
        try:
            with open(sys.argv[1]) as file:
                nlines = 0
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip() != " ":
                        nlines += 1
            print(nlines)
        except FileNotFoundError:
            sys.exit("File not found")
    elif sys.argv[1][-2:] != "py":
        sys.exit("Not a python file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    raise FileNotFoundError

'''


'''
def main():
    with open("lines.py", "r") as file:
'''


