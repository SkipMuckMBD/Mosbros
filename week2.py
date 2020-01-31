import sys
import os
from PIL import Image
import time



def printImageInfo(imagePath):
    img = Image.open(imagePath)
    px = img.load()

    width, height = img.size

    print(width, height)

    # img.show()

    start_time = time.time()
    for x in range(0, width-1):
        for y in range(0, height-1):
            print(px[x, y])


    print("--- %s seconds ---" % (time.time() - start_time))

    img.save('test.jpeg')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <image> <tiles directory>\r'.format(sys.argv[0]))
    else:
        printImageInfo(sys.argv[1])
