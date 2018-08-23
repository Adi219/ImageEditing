from PIL import Image

name = input("Filename:\t")
mode = int(input("Modes:\n\t1 - Brighten\n\t2 - Darken\nChoose: "))
changePercent = float(input("Percentage Change:\t"))

def changeBrightness(name, mode, changePercent):

    if __name__ == '__main__':
        img = Image.open('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/InputImages/' + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    img.close()

    changeValue = round((changePercent / 100) * 255)

    def changePixel(mode, value, changeValue):

        if mode == 1:
            return min((value + changeValue), 255)
        elif mode == 2:
            return max((value - changeValue), 0)


    new = Image.new('RGB', (width, height))

    newData = [tuple([changePixel(mode, value, changeValue) for value in pixelTuple]) for pixelTuple in data]

    new.putdata(newData)

    if __name__ == '__main__':
        new.save('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/GeneratedImages/' + name[: name.index('.')] + (str(mode).replace('1', 'Brighten')).replace('2', 'Darken') + str(changePercent) + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')
        
    new.show()

changeBrightness(name, mode, changePercent)
