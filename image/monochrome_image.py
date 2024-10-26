import random
from image.image_base import ImageBase

class MonochromeImage(ImageBase):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = [random.randint(0, 255) for i in range(self.size)]
            