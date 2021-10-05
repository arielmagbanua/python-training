from file_word_reader import FileWordReader
from word_count_map import WordCountMap

class WordCounter:
    def __init__(self, file_name):
        self.reader = FileWordReader(file_name)
        
        # get the words
        self.words = self.reader.get_words()

        wcm = WordCountMap(self.words)
        self.word_map = wcm.get_map()

    def display(self):
        # variable for total distinct words
        number_distinct_words = 0
        # variable for total of words read
        total_word_count = 0

        for word, count in self.word_map.items():
            # print each word and count
            print(str(count) + '    ' + word)

            # increment counter for each distinct word
            number_distinct_words += 1

            # sum up all word counts
            total_word_count += count

        print('-----------------------------------')
        print(str(number_distinct_words) + '    Number of distinct words')
        print(str(total_word_count) + '    Total words read')


