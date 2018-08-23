from PIL import Image

name1 = input("Filename:\t")
name2 = input("Filename:\t")
coordinates = tuple(map(int, input("Top Left Corner:\t").split()))

def pasteImage(name1, name2, coordinates):

    if __name__ == '__main__':
        img1 = Image.open(YOURFILEPATH + name1)
        img2 = Image.open(YOURFILEPATH2 + name2)
    else:
        img1 = Image.open(name1)
        img2 = Image.open(name2)

    img3 = Image.new("RGB", img1.size)    

    img3.paste(img1, (0, 0))
    img3.paste(img2, coordinates)

    if __name__ == '__main__':
        img3.save(YOURFILEPATH + name1[: name1.index('.')] + "Paste" + name2[: name2.index('.')] + str(coordinates[0]) + str(coordinates[1]) + '.png')
    else:
        dest = input("Destination:\t")
        img3.save(dest + '.png')

    img3.show()

pasteImage(name1, name2, coordinates)
