from PIL import Image, ImageColor

name = input("Filename:\t")
effectMode = input("Effect:\t")

def applyEffect(name, effectMode):

    if __name__ == '__main__':
        img = Image.open('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/InputImages/' + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    img.close()

    def nearest(value, roundVal):
        return round(((value // roundVal) * roundVal) + (round((value % roundVal) / roundVal) * roundVal))

    def multiplyPixel(pixelTuple, m1, m2, m3):

        a = []
        for i, value in enumerate(pixelTuple):
            if value == max(pixelTuple):
                a.append(round(value * m1))
            elif value == min(pixelTuple):
                a.append(round(value * m3))
            else:
                a.append(round(value * m2))

        return tuple(a)
        
    if effectMode == "Separate":

        roundVal = list(map(int, input("Round to nearest:\t").split()))

        effectMode += str(''.join(list(map(str, roundVal))))
        
        newData = [ tuple([nearest(value, roundVal[i]) for i, value in enumerate(pixelTuple)]) for pixelTuple in data]

    elif effectMode == "Paled":

        bounds = list(map(int, input("Lower, Higher Bounds:\t").split()))
        
        effectMode += ''.join(list(map(str, bounds)))
        
        newData = [ tuple([ round(((pixelTuple[i] / 255) * (bounds[i*2 + 1] - bounds[i] + 1)) + bounds[i]) for i in range(3)]) for pixelTuple in data]

    elif effectMode == "Push":
        
        pushPlaces = int(input("Push places:\t"))

        effectMode += str(pushPlaces)

        newData = [ tuple([pixelTuple[((i + pushPlaces) % 3)] for i in range(3)]) for pixelTuple in data]

    elif effectMode == "FocusLighten":

        focusPixel = list(map(int, input("Focus Pixel:\t").split()))

        effectMode += str(focusPixel[0]) + str(focusPixel[1])

        chunkedData = [ data[i: i + width] for i in range(0, len(data), width)]

        maxDistance = max( abs(width + height - sum(focusPixel)), sum(focusPixel), abs(width - sum(focusPixel)), abs(height - sum(focusPixel)) )
        
        newData = [ tuple([ value - round((abs(i + j - focusPixel[0] - focusPixel[1]) / maxDistance) * 255) for value in chunkedData[i][j] ])  for i in range(height) for j in range(width)]
    
    elif effectMode == "FocusDarken":

        focusPixel = list(map(int, input("Focus Pixel:\t").split()))

        effectMode += str(focusPixel[0]) + str(focusPixel[1])

        chunkedData = [ data[i: i + width] for i in range(0, len(data), width)]

        maxDistance = max( abs(width + height - sum(focusPixel)), sum(focusPixel), abs(width - sum(focusPixel)), abs(height - sum(focusPixel)) )
        
        newData = [ tuple([ round((abs(i + j - focusPixel[0] - focusPixel[1]) / maxDistance) * 255) + value for value in chunkedData[i][j] ])  for i in range(height) for j in range(width)]

    elif effectMode == "LightenEdge":

        edge = input("Edge:\t")

        effectMode += edge

        chunkedData = [ data[i: i + width] for i in range(0, len(data), width)]
        
        if edge == "Top":

            gradientData = [ [ tuple([ value - round((i / height) * 255) for value in pixelTuple ]) for pixelTuple in row] for i, row in enumerate(chunkedData) ]
            
        elif edge == "Bottom":

            gradientData = [ [ tuple([ value - round(((height - i) / height) * 255) for value in pixelTuple ]) for pixelTuple in row] for i, row in enumerate(chunkedData) ]

        elif edge == "Left":

            gradientData = [ [ tuple([ value - round((i / width) * 255) for value in pixelTuple ]) for i, pixelTuple in enumerate(row)] for row in chunkedData ]

        elif edge == "Right":

            gradientData = [ [ tuple([ value - round(((width - i) / width) * 255) for value in pixelTuple ]) for i, pixelTuple in enumerate(row)] for row in chunkedData ]
        
        newData = [a for row in gradientData for a in row ]

    elif effectMode == "DarkenEdge":

        edge = input("Edge:\t")

        effectMode += edge

        chunkedData = [ data[i: i + width] for i in range(0, len(data), width)]

        if edge == "Top":

            gradientData = [ [ tuple([ round((i / height) * 255) + value for value in pixelTuple ]) for pixelTuple in row] for i, row in enumerate(chunkedData) ]

        elif edge == "Bottom":

            gradientData = [ [ tuple([ round(((height - i) / height) * 255) + value for value in pixelTuple ]) for pixelTuple in row] for i, row in enumerate(chunkedData) ]

        elif edge == "Left":

            gradientData = [ [ tuple([ round((i / width) * 255) + value for value in pixelTuple ]) for i, pixelTuple in enumerate(row)] for row in chunkedData ]

        elif edge == "Right":

            gradientData = [ [ tuple([ round(((width - i) / width) * 255) + value for value in pixelTuple ]) for i, pixelTuple in enumerate(row)] for row in chunkedData ]
        
        newData = [a for row in gradientData for a in row ]

    elif effectMode == "EnhanceColour":

        colour = input("Colour:\t")
        enhancePercent = int(input("Percent:\t"))
        
        effectMode += colour + str(enhancePercent)

        index = ["Red", "Green", "Blue"].index(colour)
        
        newData = [ tuple([ round(value * (1 + (enhancePercent / 100))) if i == index else value for i, value in enumerate(pixelTuple)]) for pixelTuple in data]

    elif effectMode == "DiminishColour":

        colour = input("Colour:\t")
        diminishPercent = int(input("Percent:\t"))
        
        effectMode += colour + str(diminishPercent)

        index = ["Red", "Green", "Blue"].index(colour)
        
        newData = [ tuple([ round(value * (1 - (diminishPercent / 100))) if i == index else value for i, value in enumerate(pixelTuple)]) for pixelTuple in data]

    elif effectMode == "MultiplyRGB":

        maxPercent, middlePercent, minPercent = list(map(float, input("Multipliers:\t").split()))

        effectMode += str(maxPercent) + str(middlePercent) + str(minPercent)

        newData = [multiplyPixel(pixelTuple, maxPercent, middlePercent, minPercent) for pixelTuple in data]
        
    new = Image.new('RGB', (width, height))
    new.putdata(newData)


    if __name__ == '__main__':
        new.save('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/GeneratedImages/' + name[: name.index('.')] + str(effectMode) + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')

    new.show()

applyEffect(name, effectMode)
