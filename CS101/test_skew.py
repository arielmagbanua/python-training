from PIL import Image
from math import *

img = Image.open("D:\\Training\\python-training\\CS101\\test.png")
width, height = img.size
m = -0.5
xshift = abs(m) * width
new_width = width + int(round(xshift))
img = img.transform((new_width, height), Image.AFFINE, (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)

# img.show()


angle_radians = radians(53)

opp = tan(angle_radians) * 7

print(opp)