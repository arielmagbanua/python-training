# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

aggregate = 0
counter = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    aggregate += float(line[19:])
    counter += 1

avg = aggregate / counter

print('Average spam confidence: {}'.format(avg))
