from PIL import Image, ImageDraw, ImageFont

ASCII_CHARS = [' ', '.', '*', ':', 'o', '&', '8', '#', '@']

def resize(img, new_width):
    ratio = new_width / img.width
    new_height = int(img.height * ratio)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return img

def convert_image_to_ascii(img, columns):
    characters_per_pixel = 255 / (len(ASCII_CHARS) - 1)
    img = img.convert("L")
    img = resize(img, columns)
    ascii_image = []
    for i in range(img.height):
        row = []
        for j in range(img.width):
            intensity = img.getpixel((j, i))
            char = ASCII_CHARS[int(intensity / characters_per_pixel)]
            row.append(char)
        ascii_image.append(row)
    return ascii_image

def convert_ascii_to_image(ascii_image, width, height, font_size):
    font = ImageFont.truetype("arial.ttf", font_size)
    image = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    for i, row in enumerate(ascii_image):
        for j, char in enumerate(row):
            draw.text((j * font_size, i * font_size), char, font=font, fill=(255, 255, 255))
    return image

def save_image(image, path):
    image.save(path, "PNG")

img = Image.open("human.jpg")
ascii_image = convert_image_to_ascii(img, 100)
image_width = len(ascii_image[0]) * 20
image_height = len(ascii_image) * 20
image = convert_ascii_to_image(ascii_image, image_width, image_height, 20)
save_image(image, "ascii_art.png")
