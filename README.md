# img_to_asciiart
img to ascii art

The given code converts an image to ASCII art and saves it as a PNG image. The code imports the Image, ImageDraw, and ImageFont modules from the Python Imaging Library (PIL). The ASCII_CHARS variable is a list of characters that will be used to represent the image intensity levels.

The resize function takes an image and a new width as inputs and returns the image resized to the specified width, preserving the aspect ratio.

The convert_image_to_ascii function takes an image and the number of columns as inputs and returns a two-dimensional list of ASCII characters representing the image. The function first converts the image to grayscale and resizes it to the specified number of columns. Then, for each pixel in the image, the function calculates the intensity level and maps it to an ASCII character from the ASCII_CHARS list.

The convert_ascii_to_image function takes a two-dimensional list of ASCII characters, the width and height of the image, and the font size as inputs and returns an image representation of the ASCII art. The function creates a new black image and uses the ImageDraw module to draw white ASCII characters on the image.

The save_image function takes an image and a file path as inputs and saves the image as a PNG image in the specified file path.

Finally, the code opens an image named "human.jpg", converts it to ASCII art using the convert_image_to_ascii function, and saves the result as a PNG image named "ascii_art.png"

![ascii](https://user-images.githubusercontent.com/108156491/215910579-123147aa-2ad7-43a6-941f-0a9767e15204.png)
