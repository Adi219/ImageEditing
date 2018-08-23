from PIL import Image, ImageColor

name = input("Filename:\t")
filterMode = input("Filter:\t")

def applyFilter(name, filterMode):

    if __name__ == '__main__':
        img = Image.open(YOURFILEPATH + name)
    else:
        img = Image.open(name)

    width, height = img.size
    data = list(img.getdata())

    img.close()

    def greyScale(pixelTuple):
        return tuple([round(sum(pixelTuple) / 3)] * 3)

    def pixelate(array):

        averageList = []
        for i in range(3):
             averageList.append(round(sum([j[i] for j in array]) / len(array)))
        return tuple(averageList)

    def blur(square):

        averageList = []
        for i in range(3):
            averageList.append( round(sum([b[i] for a in square for b in a]) / (len(square) ** 2)) )
        return tuple(averageList)

    
    if filterMode == "Greyscale":
        newData = [greyScale(pixelTuple) for pixelTuple in data]

    elif filterMode == "Pixelate":

        smallestSize = int(input("Size of smallest pixel:\t"))

        filterMode += str(smallestSize)

        chunkedData = [ data[i: i + width] for i in range(0, len(data), width) ]
        
        heightChoppedOff = chunkedData[height - (height % smallestSize) : ]
        trimmedData = chunkedData[ : height - (height % smallestSize)]

        widthChoppedOff = [row[ len(row) - (len(row) % smallestSize) : ] for row in trimmedData]
        trimmedData = [row[ : len(row) - (len(row) % smallestSize)]  for row in trimmedData ]

        for i in range(0, len(trimmedData), smallestSize):
            for j in range(0, len(trimmedData[0]), smallestSize):
                temp = [ trimmedData[i + a][j + b] for a in range(smallestSize) for b in range(smallestSize) ]
                averageTuple = pixelate(temp)
                
                for a in range(smallestSize):
                    for b in range(smallestSize):
                        trimmedData[i + a][j + b] = averageTuple


        widenedData = [row + widthChoppedOff[i] for i, row in enumerate(trimmedData)]
        heightenedData = widenedData + heightChoppedOff
        
        newData = [pixelTuple for row in heightenedData for pixelTuple in row]

        ## ADD CODE TO PIXELATE EDGES

    elif filterMode == "Blur":

        resolution = int(input("Resolution of blur:\t"))

        filterMode += str(resolution)

        chunkedData = [ data[i: i + width] for i in range(0, len(data), width)]

        newData = [ [(0, 0, 0) for j in range(width)] for i in range(height) ]

        for i in range(height - resolution + 1):
            for j in range(width - resolution + 1):
                square = []
                for k in range(resolution):
                    square.append(chunkedData[i + k][j: j + resolution])

                average = blur(square)
                
                for k in range(1):#resolution):
                    for m in range(1):#resolution):
                        newData[i + k][j + m] = average

        newData = [b for a in newData for b in a]

    elif filterMode == "Televise":

        import math, random

        lower, higher = list(map(int, input("Lower and Higher Bounds:\t").split()))

        filterMode += str(lower) + str(higher)
        
        newData = [ tuple([round(value * (random.randint(lower, higher) / 10)) for value in pixelTuple]) for pixelTuple in data]


    new = Image.new('RGB', (width, height))
    new.putdata(newData)


    if __name__ == '__main__':
        new.save(YOURFILEPATH + name[: name.index('.')] + str(filterMode) + '.png')
    else:
        dest = input("Destination:\t")
        new.save(dest + '.png')

    new.show()

applyFilter(name, filterMode)
