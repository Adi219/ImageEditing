from PIL import Image, ImageColor

name = input("Filename:\t")
colour = input("Colour of Hue:\t")
changePercent = float(input("Percentage Change:\t"))
mode = int(input("Modes:\n\t1 - Absolute\n\t2(3/4) - Relative\nMode: "))

colourTuple = ImageColor.getcolor(colour, 'RGBA')[:3]

def changeHue(name, changePercent, colourTuple, mode):

    if __name__ == '__main__':
        img = Image.open(YOURFILEPATH + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    img.close()

    changeValue = round((changePercent / 100) * 255)

    def changePixel(value, index, colourTuple, changeValue, mode, changePercent):

        targetValue = colourTuple[index]
        
        if mode == 1:

            if value <= targetValue:
                return min((value + changeValue), targetValue)
            elif value > targetValue:
                return max((value - changeValue), targetValue)

        else:

            if mode == 2 or mode == 23:
                changeValue = round((changePercent / 100) * abs(targetValue - value))
            else:
                changeValue = round((changePercent / 100) * (targetValue - value))                

            if value <= targetValue:
                return min(value + changeValue, targetValue)
            elif value > targetValue:
                return max(value - changeValue, targetValue)

    new = Image.new('RGB', (width, height))

    newData = [tuple([changePixel(value, index, colourTuple, changeValue, mode, changePercent) for index, value in enumerate(pixelTuple)]) for pixelTuple in data]

    new.putdata(newData)

    if __name__ == '__main__':
        new.save(YOURFILEPATH + name[: name.index('.')] + str(mode).replace('1', 'Absolute').replace('2', 'Relative').replace('3', 'Complete').replace('4', 'Partial') + "Hue" + colour + str(changePercent) + '.png')
    else:
        dest = input('Destination:\t')
        new.save(dest + '.png')
    
    new.show()

changeHue(name, changePercent, colourTuple, mode)
