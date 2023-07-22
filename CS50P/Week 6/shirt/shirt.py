import sys
import os.path
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    valid_extensions = [".png", ".jpg", ".jpeg"]
    path_one = os.path.splitext(sys.argv[1])
    if path_one[1] not in valid_extensions:
        sys.exit("Invalid Input")
    path_two = os.path.splitext(sys.argv[2])
    if path_two[1] not in valid_extensions:
        sys.exit("Invalid Output")
    if path_one[1] != path_two[1]:
        sys.exit("Input and Output have different extensions")
    try:
        input_image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    size = shirt.size
    input_image = ImageOps.fit(input_image, size)
    input_image.paste(shirt, shirt)
    input_image.save(sys.argv[2])
