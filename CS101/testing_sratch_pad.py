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

# import re
# from math import *

# data = '"AG","Antigua and Barbuda",17.05,-61.8'
# data = re.split(',((?=")|(?=\d)|(?=-))', data)

# # remove empty string from the list
# # strip the " at both ends of each string
# data = [s.strip('"') for s in data if s!='']

# print(data)

# test_tuples = [('A', (1,2)), ('B', (1,2)), ('C', (1,2))]

# dicts = {key: value for (key, value) in test_tuples}

# my_list = ['one','two','three', 4, 5]

# segment1 = my_list[0:2]
# print(segment1)
# segment2 = my_list[2:4]
# print(segment2)



# decimal_count = 1
# print(ceil(15.352312 * 10) / 10)
# print(ceil(1.352312 * 10) / 10)

# print(ceil(153.5))

# normal = '"CA","Canada",60,-95'

# complex_data = '"CD","Congo, The Democratic Republic of the",0,25'

# mylist = complex_data.split(',')
# print(mylist)

# country_dict = [('BY', 'Belarus'), ('CA', 'Canada')]


# country_dict = {
#     'BY': 'Belarus',
#     'CA': 'Canada'
# }

# print(country_dict['CA'])

# countries_dict['ZW']

# num = '14.0'

# test = float(num)

# print(test)

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.something = 'something'
        self.something1 = 'something1'
        self.something2 = 'something2'

    def say_name(self):
        print(self.name)

    def eat(self):
        print('I am eating')
    
    def walk(self):
        print('Walking!')

    def __str__(self):
        # print('str test')
        return self.name

ariel = Person('Ariel', 7.0, 80.0)

ysa = Person('Ysa', 6.0, 56.0)

print(ariel.something1)


