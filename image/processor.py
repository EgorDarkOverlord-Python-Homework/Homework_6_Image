import math
import copy
import numpy as np
from image.image_base import ImageBase
from image.binary_image import BinaryImage
from image.monochrome_image import MonochromeImage
from image.color_image import ColorImage

class Processor:

    def MonocromeToMonochome(self, image):
        res = MonochromeImage(image.width, image.height)
        hist = {i:len(list(filter(lambda x : x == i, image.data))) / image.size 
                for i in range(0,256)}
        
        av1 = np.array([key*value for key, value in hist.items()]).sum()
        std1 = math.sqrt(np.array([ value * (key - av1)**2 for key, value in hist.items()]).sum())

        av2 = np.array(image.data).mean()
        std2 = np.array(image.data).std()
        res.data = std1 * (np.array(image.data) - av2) / std2 + av1
        res.data = list(map(lambda x : int(x), res.data))

        return res
    
    def BinaryToBinary(self, image):
        return copy.deepcopy(image)
    
    def ColorToMonochome(self, image):
        res = MonochromeImage(image.width, image.height)
        res.data = [(image.data[0][i] + image.data[1][i] + image.data[2][i]) // 3
                    for i in range(image.size)]
        return res
    
    def MonochomeToColor(self, image, pallete):
        res = ColorImage(image.width, image.height)
        res.data = [[pallete[image.data[i]][j] for i in range(image.size)]
                     for j in range(3)]
        return res
    
    def MonochromeToBinary(self, image, x = 128):
        res = BinaryImage(image.width, image.height)
        res.data = list(map(lambda i: 255 if i > x else 0 , image.data))
        return res

    def BinaryToMonochrome(self, image):
        res = MonochromeImage(image.width, image.height)
        
        whites = []
        for i in range(image.size):
            if image.data[i] == 255:
                whites.append((i % image.width, i // image.width))

        for i in range(image.size):
            if image.data[i] == 255:
                res.data[i] = 255
            else:
                x, y = i % image.width, i // image.width
                maxr = image.width ** 2 + image.height ** 2
                r = maxr
                for w in whites:
                    r1 = (x - w[0]) ** 2 + (y - w[1]) ** 2
                    if (r1 < r):
                        r = r1
                r = (math.sqrt(maxr) - math.sqrt(r)) / math.sqrt(maxr) * 255
                res.data[i] == int(r)
        
        return res
    
    def ColorToBinary(self, image, x = 128):
        return self.MonochromeToBinary(self.ColorToMonochome(image), x)
    
    def BinaryToColor(self, image, pallete):
        return self.MonochomeToColor(self.BinaryToMonochrome(image), pallete)

