fname = input("Enter file name: ")
fh = open(fname)

words = []

for line in fh:
    line_words = line.rstrip().split()

    for word in line_words:
        if word not in words:
            words.append(word)

words.sort()
print(words)
