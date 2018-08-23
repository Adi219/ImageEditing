from PIL import Image

name = input("Filename:\t")
alphaValue = float(input("Alpha Value:\t"))

def changeBrightness(name, alphaValue):

    if __name__ == '__main__':
        img = Image.open(YOURFILEPATH + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    img.close()

    def changeAlpha(pixelTuple):
        return tuple(list(pixelTuple) + [round(alphaValue * 255)])

    new = Image.new('RGBA', (width, height))

    newData = [changeAlpha(pixelTuple) for pixelTuple in data]

    new.putdata(newData)

    if __name__ == '__main__':
        new.save(YOURFILEPATH + name[: name.index('.')] + "Alpha" + str(alphaValue) + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')

    new.show()

changeBrightness(name, alphaValue)
