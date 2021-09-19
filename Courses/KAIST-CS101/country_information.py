import re

path = 'D:\\Training\\python-training\\CS101\\'

country_names = []
country_coordinates = []

# read the file
countries_file = open(path + 'average-latitude-longitude-countries.csv')
list_countries_data = countries_file.readlines()

# loop through each of the records
# then store them at their respective list of tuples
for i in range(1, len(list_countries_data)):
    # get the data at the current index and strip it
    # this will strip the string with \t \n characters
    data = list_countries_data[i].strip()

    # split the string using , to transform the data to a list
    # split it using regular expression to deal with countries that has comma
    data = re.split(',((?=")|(?=\d)|(?=-))', data)

    # remove empty string from the list
    # strip the " at both ends of each string
    data = [s.strip('"') for s in data if s!='']

    temp = []
    for s in data:
        if s!='':
            temp.appen(s.strip('"'))
    
    data = temp



    # create the country (code, name) tuple and append it
    country_name = (data[0], data[1])
    country_names.append(country_name)
    
    # create the country (code, (lat, long)) tuple and append it
    country_coordinate = (data[0], (float(data[2]), float(data[3])))
    country_coordinates.append(country_coordinate)

# print the list that conttains the needed tuples
print(country_names)
print(country_coordinates)

# convert the (code, name) tuple to dictionary for easier access of names
# use dictionary comprehension to accomplish this
countries_dict = {code: country_name for (code, country_name) in country_names}

# print the names of all country whose location lies in the south of the equator
for code, coordinates in country_coordinates:
    # unpack coordinates
    lat, lng = coordinates

    # print country names south of the equator
    if 0 >= lat >= -90:
        print(countries_dict[code])

# ask for country code input and print the full name of that country
country_code = input('Enter country code: ')
print(countries_dict[country_code])
