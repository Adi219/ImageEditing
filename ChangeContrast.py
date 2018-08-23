from PIL import Image

name = input("Filename:\t")
mode = int(input("Modes:\n\t1 - Increase\n\t2 - Decrease\nChoose: "))
changePercent = float(input("Percentage Change:\t"))

def changeContrast(name, mode, changePercent):

    if __name__ == '__main__':
        img = Image.open(YOURFILEPATH + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    img.close()

    changeValue = round((changePercent / 100) * 255)

    def enhancePixel1(mode, value, changePercent, pixelTuple):

        if mode == 1:
            val = 1
        elif mode == 2:
            val =  round( ((100 - changePercent) / 100) * (1 / (128 ** 2)) * ((value - 128) ** 3) ) + 128

        return val

    def enhancePixel2(mode, value, changePercent, pixelTuple):
        
        if mode == 1:

            if changePercent == 0:
                val = value
            elif changePercent == 50:
                val = ((2 * value) - (128 * (2 - 1)))
            elif changePercent == 100:
                val = ((128 * value) - (128 * (128  - 1)))
            elif changePercent < 50:
                val = (((changePercent / 50) + 1) * value) - (128 * (changePercent / 50))
            elif changePercent < 100:
                val = (((((changePercent - 50) / 50) * 128) + 1) * (value - 128)) + 128
            
        elif mode == 2:
            val = (value * (1 - (changePercent / 100))) + (128 * (changePercent / 100))

        return round(val)
    
    new = Image.new('RGB', (width, height))

    newData = [ tuple([enhancePixel2(mode, value, changePercent, pixelTuple) for value in pixelTuple]) for pixelTuple in data]
    
    new.putdata(newData)

    if __name__ == '__main__':
        new.save(YOURFILEPATH + name[: name.index('.')] + (str(mode).replace('1', 'IncreaseContrast')).replace('2', 'DecreaseContrast') + str(changePercent) + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')
        
    new.show()

changeContrast(name, mode, changePercent)
