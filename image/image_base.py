class ImageBase:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        pass

    def print(self):
        print(f"width: {self.width} height: {self.height}")
        print("data:")
        for y in range(self.height):
            for x in range(self.width):
                print(self.data[y * self.width + x], end=' ')
            print()