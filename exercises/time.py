from pathlib import Path
import sys
import math 

# get the argument inputs of the command string
timezones_file = sys.argv[1]
current_time_sydney = sys.argv[2]

# get the current hours equivalent of sydnet
input_time_sydney = current_time_sydney.split(':')
input_hour_sydney = float(input_time_sydney[0]) + float(float(input_time_sydney[1]) / 60)

# open the file specified
p = Path(__file__).with_name(timezones_file)
with p.open('r') as f:
    # read the line
    line = f.readlines()

    timezones = []
    sydney_timezone = ()

    for i in range(0, len(line)):
        # extract the country and timezone then store it as a tuple
        country_timezone = line[i].split()
        country = ' '.join(country_timezone[:len(country_timezone) - 1])
        timezone = float(country_timezone[len(country_timezone) - 1])
        timezones.append((country, timezone))

        # get the sydney timezone from the file
        if country.lower() == "sydney":
            sydney_timezone = (country, timezone)
    
    for i in range(0, len(timezones)):
        current_tz = timezones[i]

        # the current country that we are looping
        current_country = current_tz[0]
        # the timezone of the country that we are looping
        current_timezone = current_tz[1]

        # calculate the timezone difference
        tz_diff = sydney_timezone[1] - current_timezone

        # calculate hours difference between current input sydney hours
        # and the timezone hours difference between sydney and current country
        hours_diff = input_hour_sydney - tz_diff

        # transform hours difference to hours and minutes and that's the
        # equivalent time in the current country
        hours_diff = math.modf(hours_diff)
        hours = int(hours_diff[1])
        minutes = abs(int(hours_diff[0] * 60))

        # print the equivalent time for the current country
        if (hours < 0):
            # more than 12 hours difference
            hours = hours + 23
            print(current_country + ' {:02}'.format(hours) + ":" + '{:02}'.format(minutes) + ' -1')
        else: 
            print(current_country + ' {:02}'.format(hours) + ":" + '{:02}'.format(minutes))
