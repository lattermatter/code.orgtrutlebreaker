from PIL import Image

name = input("image full name: ")

def shrink(y):
    return y*320/450

im = Image.open(f'turtledestrouer/{name}') # Can be many different formats.
width, height = im.size

while True:
    centering = input("1 for left, 2 for center, 3 for right: ")
    if centering == '2':
        im1 = im.crop((int(width/2 - shrink(height)/2), 0, int(width/2 + shrink(height)/2), height))
        break
    elif centering == "3":
        im1 = im.crop((int(width*2/3), 0, width, height))
        break
    elif centering == "1":
        im1 = im.crop((0, 0, int(width*1/3), height))
        break
    else:
        im1 = im.crop((int(width/2 - shrink(height)/2), 0, int(width/2 + shrink(height)/2), height))
        break

new_image = im1.resize((320, 450))
pix = new_image.load()

image_dict = {}
for y in range(0, 450):
    for x in range(0, 320):
        pixRGB = pix[x, y]
        coord = (x, y)
        image_dict[coord] = pixRGB

key = image_dict.keys()
with open('turtledestrouer/image1text.txt', 'w') as f:
    f.write("""function MoveFunction(x, y) {
  penUp();
  moveTo(x,y);
  penDown();
}

function Dot(r, g, b) {
  penRGB(r, g, b);
  dot(0.5);
}
    """)
    for element in key:
        f.write(f"MoveFunction{element};")
        f.write('\n')
        f.write(f"Dot{image_dict[element]};")
        f.write('\n')
