from PIL import Image

name = input("Filename:\t")
startX, startY = list(map(int, input("Top-Left Point:\t").split()))
width, height = list(map(int, input("Width, Height:\t").split()))

def cropImage(name, startX, startY, width, height):

    if __name__ == '__main__':
        img = Image.open('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/InputImages/' + name)
    else:
        img = Image.open(name)

    origWidth, origHeight = img.size
    data = list(img.getdata())

    img.close()

    new = Image.new('RGBA', (width, height))

    acceptable = list(range(startY, startY + height))

    chunkedData = [ data[i: i + origWidth] for i in range(0, len(data), origWidth) ]
    trimmedData1 = chunkedData[startY : startY + height]
    trimmedData2 = [ chunk[startX: startX + width] for chunk in trimmedData1]

    newData = [pixelTuple for chunk in trimmedData2 for pixelTuple in chunk]
    
    new.putdata(newData)

    if __name__ == '__main__':
        new.save('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/GeneratedImages/' + name[: name.index('.')] + "Crop" + str(startX) + str(startY) + str(width) + str(height) + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')
        
    new.show()

cropImage(name, startX, startY, width, height)
