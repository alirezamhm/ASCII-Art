from PIL import Image
im = Image.open('sample.jpg')
im.thumbnail((500, 500), Image.ANTIALIAS)

width, heigth = im.size
data = list(im.getdata())
pixels = [data[i:i+width] for i in range(0, len(data), width)]
for row in range(len(pixels)):
    for col in range(len(pixels[row])):
        pixels[row][col] = sum(pixels[row][col]) // 3

characters = list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$") # ascii characters sorted by brightness
ratio = 255/len(characters)
for row in range(len(pixels)):
    for col in range(len(pixels[row])):
        brightness = pixels[row][col]
        pixels[row][col] = characters[int(brightness//ratio)]

def print_image(pixels: list):
    for row in range(len(pixels)):
        for col in range(len(pixels[row])):
            print(pixels[row][col], end='')
        print()
    print()

print_image(pixels)
