from PIL import Image

def process_image():
    img = Image.open('icon.png').convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        r, g, b, a = item
        # Calculate saturation / color difference
        diff = max(r, g, b) - min(r, g, b)
        
        # If it's pure white, black, or gray, it has very low difference
        # We also want to fade the edges smoothly
        if diff < 15:
            newData.append((r, g, b, 0))
        elif diff < 55:
            # Smooth alpha transition
            alpha = int((diff - 15) / 40.0 * 255)
            # Make the underlying color pure red to avoid white/black fringes showing up
            newData.append((r, g, b, alpha))
        else:
            newData.append((r, g, b, 255))

    img.putdata(newData)
    img.save('icon_transparent.png', 'PNG')
    print("Successfully created new icon_transparent.png with corners removed")

if __name__ == '__main__':
    process_image()
