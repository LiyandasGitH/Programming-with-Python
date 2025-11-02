import sys
from PIL import Image, ImageOps
import os



if len(sys.argv) == 3:

    extensions = [".jpg", ".jpeg", ".png"]
    extension1 = os.path.splitext(sys.argv[1])
    extension2 = os.path.splitext(sys.argv[2])
    if extension1[1] == extension2[1] and extension1[1] in extensions:

        try:
            filename = sys.argv[1]
            namefile = sys.argv[2]

            new_image = Image.open(filename)

        except FileNotFoundError:
            sys.exit("File does not exist")


        shirt = Image.open("shirt.png")
        size = shirt.size
        # (width height)
        new_image = ImageOps.fit(new_image, size)
        new_image.paste(shirt, shirt)
        new_image.save(namefile)

    elif extension1[1] != extension2[1]:
         sys.exit("Input and Output have different extensions")

    else:
         sys.exit("Wrong extension")

elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
        sys.exit("Too mamy command-line arguments")










'''
def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")




    if not filename.endswith({"jpg", "jpeg", "png"}):
        sys.exit("Not a valid file")

    if not namefile.endswith({"jpg", "jpeg", "png"}):
        sys.exit("Not a valid file")


    filename = sys.argv[1]
    namefile = sys.argv[2]

    if len(sys.argv) == 3:

        try:
            new_image = Image.open(filename)

        except FileNotFoundError:
            sys.exit("File does not exist")


        shirt = Image.open("shirt.png")
        size = shirt.size
        # width & height
        new_image = ImageOps.fit(new_image, size)
        new_image.save(namefile)



if __name__ == "__main__":
    main()
'''
