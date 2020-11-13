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

import re
from math import *

data = '"AG","Antigua and Barbuda",17.05,-61.8'
data = re.split(',((?=")|(?=\d)|(?=-))', data)

# remove empty string from the list
# strip the " at both ends of each string
data = [s.strip('"') for s in data if s!='']

# print(data)

test_tuples = [('A', (1,2)), ('B', (1,2)), ('C', (1,2))]

dicts = {key: value for (key, value) in test_tuples}

my_list = ['one','two','three', 4, 5]

segment1 = my_list[0:2]
print(segment1)
segment2 = my_list[2:4]
print(segment2)

print(round(15.35, 1))

decimal_count = 1
print(ceil(15.352312 * 10) / 10)
print(ceil(1.352312 * 10) / 10)

print(ceil(153.5))