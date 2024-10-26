import random
from image.image_base import ImageBase

class BinaryImage(ImageBase):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = [255 * random.randint(0, 1) for i in range(self.size)]
    