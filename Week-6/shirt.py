import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    valid_extensions = {".jpg", ".jpeg", ".png"}

    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        photo = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    photo = ImageOps.fit(photo, shirt.size)

    photo.paste(shirt, shirt)

    photo.save(output_path)


if __name__ == "__main__":
    main()
