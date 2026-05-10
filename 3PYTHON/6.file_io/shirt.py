from PIL import Image
from PIL import ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        _, secondArg, thirdArg = sys.argv
        _, ext_file1 = os.path.splitext(secondArg)
        _, ext_file2 = os.path.splitext(thirdArg)

        if ext_file1 != ".jpg" and ext_file1 != ".jpeg" and ext_file1 != ".png":
            sys.exit("Invalid input")
        elif ext_file2 != ".jpg" and ext_file2 != ".jpeg" and ext_file2 != ".png":
            sys.exit("Invalid input2")
        elif ext_file1 != ext_file2:
            sys.exit("Input and output have different extensions")

        with Image.open(secondArg) as img:
            print(img.size)
            img2 = ImageOps.fit(img, (100, 100))
            img2.save(thirdArg)

    except ValueError as e:
        pass
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
