name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

hour_counts = {}

for line in handle:
    if line.startswith('From '):
        words = line.strip().split()
        hour = words[5].split(':')[0]
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

sorted_hour_counts = sorted([(h, c) for h, c in hour_counts.items()])
for hour, count in sorted_hour_counts:
    print('{} {}'.format(hour, count))
