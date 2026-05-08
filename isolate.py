from PIL import Image
import os

img = Image.open('icon.png').convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    m = max(item[0], item[1], item[2])
    if m < 15:
        newData.append((item[0], item[1], item[2], 0))
    elif m < 45:
        alpha = int((m - 15) / 30.0 * 255)
        newData.append((item[0], item[1], item[2], alpha))
    else:
        newData.append((item[0], item[1], item[2], 255))

img.putdata(newData)
img.save('icon_transparent.png', 'PNG')
print("Successfully created icon_transparent.png")
