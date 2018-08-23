from PIL import Image, ImageColor
import random

name = input("Filename:\t")
patternMode = input("Filter:\t")

def applyPattern(name, patternMode):

    if __name__ == '__main__':
        img = Image.open('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/InputImages/' + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    img.close()

    if patternMode == "Chessboard":

        squareSize = int(input("Size:\t"))
        difference = int(input("Colour Difference:\t"))
        
        patternMode += str(squareSize) + str(difference)
        
        chunkedData = [data[i: i + width] for i in range(0, len(data), width)]

        isDark = True
        for i in range(0, height, squareSize):
            for j in range(0, width, squareSize):

                for k in range(squareSize):
                    for m in range(squareSize):

                        if i + k < height and j + m < width:

                            blah = []
                            
                            if isDark:
                                for n in range(3):
                                    blah.append(chunkedData[i + k][j + m][n] - difference)
                            else:
                                for n in range(3):
                                    blah.append(chunkedData[i + k][j + m][n] + difference)

                            chunkedData[i + k][j + m] = tuple(blah)

                isDark = not isDark

        newData = [a for row in chunkedData for a in row]

    elif patternMode == "RainbowStripes":

        direction = input("Direction:\t")
        stripeWidth = int(input("Width:\t"))
        
        patternMode += direction + str(stripeWidth)

        chunkedData = [data[i: i + width] for i in range(0, len(data), width)]
                
        if direction == "Vertical":

            for j in range(0, width, stripeWidth):

                values = [((random.randint(0, 1) * 2) - 1) * random.randint(1, 16), ((random.randint(0, 1) * 2) - 1) * random.randint(1, 16), ((random.randint(0, 1) * 2) - 1) * random.randint(1, 16)]
                
                for i in range(height):
                    for k in range(stripeWidth):

                        if j + k < width:

                            for n in range(3):
                                chunkedData[i][j + k] = tuple([val + values[z] for z, val in enumerate(chunkedData[i][j + k])])

        elif direction == "Horizontal":

            for j in range(0, height, stripeWidth):

                values = [((random.randint(0, 1) * 2) - 1) * random.randint(1, 16), ((random.randint(0, 1) * 2) - 1) * random.randint(1, 16), ((random.randint(0, 1) * 2) - 1) * random.randint(1, 16)]
                
                for i in range(width):
                    for k in range(stripeWidth):

                        if j + k < height:

                            for n in range(3):
                                chunkedData[j + k][i] = tuple([val + values[z] for z, val in enumerate(chunkedData[j + k][i])])
        
        newData = [a for row in chunkedData for a in row]

    elif patternMode == "ColorStripes":

        color = input("Color:\t")
        direction = input("Direction:\t")
        stripeWidth = int(input("Width:\t"))
        
        patternMode += direction + str(stripeWidth)

        colorTuple = ImageColor.getcolor(color, 'RGBA')

        chunkedData = [data[i: i + width] for i in range(0, len(data), width)]
        
        if direction == "Vertical":

            for j in range(0, width, stripeWidth * 2):

                for i in range(height):
                    for k in range(stripeWidth):

                        if j + k < width:

                            for n in range(3):
                                chunkedData[i][j + k] = colorTuple

        elif direction == "Horizontal":

            for j in range(0, height, stripeWidth * 2):

                for i in range(width):
                    for k in range(stripeWidth):

                        if j + k < height:

                            for n in range(3):
                                chunkedData[j + k][i] = colorTuple

        newData = [a for row in chunkedData for a in row]

##    elif pattern == 
        
    new = Image.new('RGB', (width, height))
    new.putdata(newData)


    if __name__ == '__main__':
        new.save('C:/Adi/Programming/AdiPython/AdiScripts/Others/Art/GeneratedImages/' + name[: name.index('.')] + str(patternMode) + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')

    new.show()

applyPattern(name, patternMode)
