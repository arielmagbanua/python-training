from math import ceil

path = 'D:\\Training\\python-training\\CS101\\'

tpmon_file = open(path + 'tpmon.txt')
# read all lines and store it in a list
monthly_temperatures = tpmon_file.readlines()

# clean up each item and make sure all items are string
monthly_temperatures = [temps.strip() for temps in monthly_temperatures if temps != '\n']

# get the starting and ending year
title_list = monthly_temperatures[0].split(',')
start_end_years = tuple(int(year) for year in title_list[1].strip().split('-'))

# organize the monthly temperatures in year -> temperature list dictionary
year = start_end_years[0]
years_temperatures = {}

# loop each temperatures list and assign it to the correct year
for i in range(1, len(monthly_temperatures)):
    # convert the temeratures string to list
    temps_list = monthly_temperatures[i].split()
    # convert each temperature to integer
    temps_list = [float(temp) for temp in temps_list]
    # add the year as key and the list as value in the dictionary
    years_temperatures[year] = temps_list
    year+=1

tpmon_csv_file = open(path + 'tpmon.csv', 'w+')
# remove the content in case file is not empty
tpmon_csv_file.truncate(0)

# print the temperature averages of winter and summer per year
for year, month_temperatures in years_temperatures.items():
    # january - february average
    winter_avg = (month_temperatures[0] + month_temperatures[1]) / 2
    winter_avg = ceil(winter_avg * 10) / 10
    # july - august average
    summer_avg = (month_temperatures[6] + month_temperatures[7]) / 2
    summer_avg = ceil(summer_avg * 10) / 10
    
    # print year: winter_avg/summer_avg
    print('{}: {}/{}'.format(year, winter_avg, summer_avg))

    # convert each float temps to string
    month_temperatures = [str(temp) for temp in month_temperatures]
    # write year and temperatures as csv
    year_row = '{},{}\n'.format(year, ','.join(month_temperatures))
    tpmon_csv_file.write(year_row)

# close the file
tpmon_csv_file.close()
