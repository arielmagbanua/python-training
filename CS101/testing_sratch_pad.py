# from PIL import Image
# from math import *

# img = Image.open("D:\\Training\\python-training\\CS101\\test.png")
# width, height = img.size
# m = -0.5
# xshift = abs(m) * width
# new_width = width + int(round(xshift))
# img = img.transform((new_width, height), Image.AFFINE, (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)

# img.show()

# test_list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# sorted_list = sorted(test_list, key=lambda k: k['name'])

# print(sorted_list)

awts = ['hotel_name']

print(awts == ['hotel_name'])