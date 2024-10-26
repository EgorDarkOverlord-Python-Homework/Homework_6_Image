import random
from image.image_base import ImageBase

class ColorImage(ImageBase):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = [[random.randint(0, 255) for i in range(self.size)]
                     for i in range(3)]
    
    def print(self):
        print(f"width: {self.width} height: {self.height}")
        print("data:")
        for c in range(3):
            for y in range(self.height):
                for x in range(self.width):
                    print(self.data[c][y * self.width + x], end=' ')
                print()
            print()