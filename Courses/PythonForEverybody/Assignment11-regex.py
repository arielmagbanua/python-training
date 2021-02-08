import re

filename = 'regex_sum_1088021.txt'
fh = open(filename)

file_content = fh.read()

numbers = re.findall('[0-9]+', file_content)

# sum up all the numbers
result = 0
for num in numbers:
    result += int(num)

print(result)
