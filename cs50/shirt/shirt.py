import sys
from PIL import Image, ImageOps


def main():

    # command-line error checker
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    try:
        # read file
        file_name = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        input, ext1 = sys.argv[1].split(".")
        output, ext2 = sys.argv[2].split(".")
        if ext1.lower() not in ["png", "jpg", "jpeg"]:
            sys.exit("Invalid input")
        if ext1 != ext2:
            sys.exit("Input and output have different extensions")

    overlay()


def overlay():
    input, output = sys.argv[1], sys.argv[2]

    shirt = Image.open("shirt.png")
    size = shirt.size

    im = Image.open(input)
    photo = ImageOps.fit(im, size)


    photo.paste(shirt, shirt)
    photo.save(output)


if __name__ == "__main__":
    main()