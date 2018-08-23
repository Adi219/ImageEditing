from PIL import Image, ImageColor

name = input("Filename:\t")

location = list(map(int, input("Target Pixel:\t").split())) 

replacementColour = input("Replacement Colour:\t")
replaceTuple = ImageColor.getcolor(replacementColour, 'RGB')

def replaceColour(name, location, replaceTuple):

    if __name__ == '__main__':
        img = Image.open(YOURFILEPATH + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    targetTuple = data[ ((location[1] - 1) * width) + location[0] ]   
    
    img.close()

    RGB = targetTuple.index(max(targetTuple))
    
    def isRGBClose(givenColour, RGB):
        return givenColour.index(max(givenColour)) == RGB

    def isClose(givenTuple, targetTuple):
        return (targetTuple[0] - givenTuple[0]) ** 2 + (targetTuple[1] - givenTuple[1]) ** 2 + (targetTuple[2] - givenTuple[2]) ** 2 <= (255 ** 2)

    def alterPixel(pixel, RGB, replaceRGB):
        a = list(pixel)
        a[RGB], a[replaceRGB] = a[replaceRGB], a[RGB]
        return tuple(a)

    def isRGBClose2(givenTuple, targetTuple):

        if abs(max(givenTuple) - givenTuple[targetTuple.index(max(targetTuple))]) <= 8:
            return True

        
        givenMaxIndices = [a for a in range(3) if givenTuple[a] == max(givenTuple)]
        targetMaxIndices = [a for a in range(3) if targetTuple[a] == max(targetTuple)]

        for index in givenMaxIndices:
            if index in targetMaxIndices:
                return True
        

        return False
        
        
    replaceRGB = replaceTuple.index(max(replaceTuple))
#    newData = [alterPixel(data[i], RGB, replaceRGB) if isRGBClose(data[i], RGB) else data[i] for i in range(len(data))]

    newData = [alterPixel(data[i], RGB, replaceRGB) if isRGBClose2(data[i], targetTuple) else data[i] for i in range(len(data))]
    

    new = Image.new('RGB', (width, height))
    new.putdata(newData)
    
    if __name__ == '__main__':
        new.save(YOURFILEPATH + name[: name.index('.')] + str(location[0]) + str(location[1]) + replacementColour + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')
        
    new.show()

replaceColour(name, location, replaceTuple)
