#! /usr/bin/python3

from PIL import Image
import os

image = Image.open("Pokemon.jpg")

# maxHeight, maxWidth = image.
cropWidth, cropHeight = (250, 250)
cropBounds = (0, 0, cropWidth, cropHeight)

horizontalNumber = 16
verticalNumber = 10

backgroundColor = (250, 250, 250)

path = "exported/"
spriteFolder = "pokemon/"

if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(path + spriteFolder):
    os.mkdir(path + spriteFolder)
counter = 1

for left in range(0, cropWidth * horizontalNumber, cropWidth):
    for upper in range(0, cropHeight * verticalNumber, cropHeight):
        cropBounds = (left, upper, left+cropWidth, upper+cropHeight)
        resized = image.crop(cropBounds)
        resized = resized.convert("RGBA")

        data = resized.getdata()
        # print(data)
        temp = list()
        for r,g,b,a in data:
            # print(r,g,b,a)
            if r >= backgroundColor[0] and g >= backgroundColor[1] and b >= backgroundColor[2]:
                temp.append((r,g,b,0))
                continue
            temp.append((r,g,b,a))
        resized.putdata(temp)
        resized.save(path + spriteFolder +str(counter)+".png", "PNG")
        counter = counter + 1
image.close()