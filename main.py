import random
from image.binary_image import BinaryImage
from image.monochrome_image import MonochromeImage
from image.processor import Processor
from image.color_image import ColorImage

p = Processor()

print('MonocromeToMonochome\n')

m1 = MonochromeImage(3, 2)
m1.print()
print()

m2 = p.MonocromeToMonochome(m1)
m2.print()
print()

print()


print('BinaryToBinary\n')

b1 = BinaryImage(4, 4)
b1.print()
print()

b2 = p.BinaryToBinary(b1)
b2.print()
print()

print()


print('ColorToMonochome\n')

c = ColorImage(3, 3)
c.print()
print()

m = p.ColorToMonochome(c)
m.print()
print()

print()


print('MonochomeToColor\n')

m = MonochromeImage(3, 2)
m.print()
print()

c = p.MonochomeToColor(m, {i : (random.randint(0,i) , random.randint(0,i), random.randint(0,i)) for i in range(256)})
c.print()
print()

print()


print('MonochromeToBinary\n')

m = MonochromeImage(3, 2)
m.print()
print()

b = p.MonochromeToBinary(m)
b.print()
print()


print('BinaryToMonochrome\n')

b = BinaryImage(4, 4)
b.print()
print()

m = p.BinaryToMonochrome(b)
m.print()
print()


print('ColorToBinary\n')

c = ColorImage(3, 3)
c.print()
print()

b = p.ColorToBinary(c)
b.print()
print()


print('BinaryToColor\n')

b = BinaryImage(4, 4)
b.print()
print()

c = p.BinaryToColor(b, {i : (random.randint(0,i) , random.randint(0,i), random.randint(0,i)) for i in range(256)})
c.print()
print()