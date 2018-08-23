from PIL import Image, ImageColor

name = input("Filename:\t")

location = list(map(int, input("Target Pixel:\t").split())) 

replacementColour = input("Replacement Colour:\t")
replaceTuple = ImageColor.getcolor(replacementColour, 'RGB')

def replaceColour(name, location, replaceTuple):

    if __name__ == '__main__':
        img = Image.open('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/InputImages/' + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    targetTuple = data[ ((location[1] - 1) * width) + location[0] ]   
    
    img.close()

    RGB = targetTuple.index(max(targetTuple))
    
    #def isRGBClose(givenColour, RGB):
     #   return givenColour.index(max(givenColour)) == RGB

    def isRGBClose(givenColour, RGB, targetTuple):
        #return (givenColour.index(max(givenColour)) == RGB) and (abs(max(givenColour) - max(targetTuple))) <= 64 and ( (((targetTuple[0] - givenColour[0]) ** 2 + (targetTuple[1] - givenColour[1]) ** 2 + (targetTuple[2] - givenColour[2]) ** 2) - (targetTuple[RGB] - givenColour[RGB]) ** 2) <= (64 ** 2))
        return (givenColour.index(max(givenColour)) == RGB) and (abs(max(givenColour) - max(targetTuple))) <= 64 and abs(sum(givenColour) - sum(targetTuple)) <= 64        
    def isClose(givenTuple, targetTuple):
        return (targetTuple[0] - givenTuple[0]) ** 2 + (targetTuple[1] - givenTuple[1]) ** 2 + (targetTuple[2] - givenTuple[2]) ** 2 <= (64 ** 2)


    #def alterPixel(pixel, RGB, replaceRGB):
     #   a = list(pixel)
      #  a[RGB], a[replaceRGB] = a[replaceRGB], a[RGB]
       # return tuple(a)

    def alterPixel(pixel, targetTuple, RGB, replaceRGB):
        a = list(targetTuple)
        a[replaceRGB] = pixel[RGB]
        return tuple(a)
    
    replaceRGB = replaceTuple.index(max(replaceTuple))
#    newData = [alterPixel(data[i], RGB, replaceRGB) if isRGBClose(data[i], RGB) else data[i] for i in range(len(data))]
    newData = [alterPixel(data[i], targetTuple, RGB, replaceRGB) if isRGBClose(data[i], RGB, targetTuple) else data[i] for i in range(len(data))]
#    newData = [alterPixel(data[i], RGB, replaceRGB) if isClose(data[i], targetTuple) else data[i] for i in range(len(data))]
    

    new = Image.new('RGB', (width, height))
    new.putdata(newData)
    
    if __name__ == '__main__':
        new.save('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/GeneratedImages/' + name[: name.index('.')] + str(location[0]) + str(location[1]) + replacementColour + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')
        
    new.show()

replaceColour(name, location, replaceTuple)
