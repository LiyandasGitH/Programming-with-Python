def main():
    with open("alice.txt", "r") as f:
        #contents = f.reader()
        contents = f.readlines()

    chapter1 = contents[52:272]
    with open("chapter1.txt", "w") as f:
        f.writelines("Chapter I.")


    print(contents[0])




main()
