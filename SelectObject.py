from PIL import Image

name = input("Filename:\t")
origX, origY = list(map(int, input("Starting Pixel:\t").split()))
tolerance = int(input("Tolerance:\t"))

def selectObject(name, origX, origY, tolerance):

    if __name__ == '__main__':
        img = Image.open('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/InputImages/' + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    img.close()

    def discover(found, captured, data, width, height, tolerance, targetColour):

        discovered = []
        
        checkPixels = []
        referPixel = {}
        for location in found:

            x, y = location

            possiblePixels = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
            blackList = []

            if x == 1:
                blackList += [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1]]
            elif x == width:
                blackList += [[x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]

            if y == 1:
                blackList += [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1]]
            elif y == height:
                blackList += [[x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]

            checkList = [tuple(pixel) for pixel in possiblePixels if pixel not in blackList and pixel not in checkPixels]
            for pixel in checkList:
                referPixel[pixel] = location
                checkPixels.append(pixel)

            
        for pixel in checkPixels:

            actualColour = data[ ((pixel[1] - 1) * width) + pixel[0] ]

            if abs(targetColour[0] - actualColour[0]) ** 2 + abs(targetColour[1] - actualColour[1]) ** 2 + abs(targetColour[2] - actualColour[2]) ** 2 <= (tolerance ** 2):

                if pixel not in captured and pixel not in discovered:
                    discovered.append(pixel)

        return discovered
            
            
    targetColour = data[ (origY * width) + origX ]

    captured = [(origX, origY)]
    found = [(origX, origY)]
    stop = False
    prev = 0
    while not stop:

        found = discover(found, captured, data, width, height, tolerance, targetColour)
        print(len(found))
        if len(found) == 0:
            stop = True
        else:
            captured += found
            prev = len(found)
    
    
    new = Image.new('RGB', (width, height), "white")
    newData = list(new.getdata())
    for location in captured:
        x, y = location
        newData[ ((y - 1) * width) + x] = data[ ((y - 1) * width) + x]
    
    new.putdata(newData)

    if __name__ == '__main__':
        new.save('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/GeneratedImages/' + name[: name.index('.')] + "Select" + str(tolerance) + str(origX) + str(origY) + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')
        
    new.show()

selectObject(name, origX, origY, tolerance)
