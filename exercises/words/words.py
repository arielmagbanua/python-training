from pathlib import Path

# create the word - count mapping / dictionary
word_dict = {}

# open the file specified assuming at the same directory
file_path = Path(__file__).with_name('kennedy.txt')
with file_path.open('r') as file:
    # read the line
    lines = file.readlines()

    # loop through each line
    for line in lines:
        # strip newlines and split into words
        words = line.strip().split(' ')
        
        # loop through each word and tally the count
        for word in words:
            # make it as lowercase
            word = word.lower()

            if word.isalpha():
                # the word is legit word then tally
                # the occurence in the word dictionary
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    # not yet existed therefore initialize to 1
                    word_dict[word] = 1

# variable for total distinct words
number_distinct_words = 0
# variable for total of words read
total_word_count = 0
for word, count in word_dict.items():
    # print each word and count
    print(str(count) + '    ' + word)

    # increment counter for each distinct word
    number_distinct_words += 1

    # sum up all word counts
    total_word_count += count

print('-----------------------------------')
print(str(number_distinct_words) + '    Number of distinct words')
print(str(total_word_count) + '    Total words read')
