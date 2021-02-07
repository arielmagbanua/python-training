name = input("Enter file:")
if len(name) <1:
    name = "mbox-short.txt"

handle = open(name)

email_counts = {}

for line in handle:
    if line.startswith('From '):
        words = line.strip().split()
        email = words[1]

        email_counts[email] = email_counts.get(email, 0) + 1

biggest_count_email = None
biggest_count = 0

# determine what email has largest count
for email, count in email_counts.items():
    if biggest_count < count:
        biggest_count = count
        biggest_count_email = email

print('{} {}'.format(biggest_count_email, biggest_count))
