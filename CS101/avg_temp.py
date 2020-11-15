from math import ceil

path = 'D:\\Training\\python-training\\CS101\\'

tpmon_file = open(path + 'tpmon.txt')

# read all lines and store it to a list
monthly_temperatures = tpmon_file.readlines()

# clean up each item and make sure all items are string
monthly_temperatures = [temps.strip() for temps in monthly_temperatures if temps != '\n']

year = 1723

tpmon_csv_file = open(path + 'tpmon.csv', 'w+')
tpmon_csv_file.truncate(0)

for i in range(1, len(monthly_temperatures)):
    # convert the temeratures string to list
    temps_list = monthly_temperatures[i].split()
    # convert each temperature to float
    temps_list = [float(temp) for temp in temps_list]

    winter_avg = (temps_list[0] + temps_list[1]) / 2
    winter_avg = ceil(winter_avg * 10) / 10
    summer_avg = (temps_list[6] + temps_list[7]) / 2
    summer_avg = ceil(summer_avg * 10) / 10

    print('{}: {}/{}'.format(year, winter_avg, summer_avg))  

    # convert each of the item in temp_list as string
    temps_list = [str(temp) for temp in temps_list]
    year_row = '{},{}\n'.format(year, ','.join(temps_list))
    tpmon_csv_file.write(year_row)

    year += 1

tpmon_csv_file.close()

tpmon_csv_new = open(path + 'tpmon.csv')
lines = tpmon_csv_new.readlines()
tpmon_csv_new.close()

header = 'Year,Jan.,Feb.,Mar.,Apr.,Jun.,Jul.,Aug.,Oct.,Nov.,Dec.\n'

tpmon_csv_new = open(path + 'tpmon.csv', 'w+')
tpmon_csv_new.write(header)

for line in lines:
    tpmon_csv_new.write(line)

tpmon_csv_new.close()