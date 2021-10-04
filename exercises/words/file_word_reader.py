from pathlib import Path

class FileWordReader:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def get_words(self):
        all_words = []

        # open the file specified assuming at the same directory
        file_path = Path(__file__).with_name(self.file_name)
        with file_path.open('r') as file:
            # read the line
            lines = file.readlines()
            
            # loop through each line
            for line in lines:
                # strip newlines and split into words
                words = line.lower().strip().split(' ')

                all_words += words

                # # loop through each word and tally the count
                # for word in words:
                #     # make lower case and add to list
                #     words.append(word)
    
        return all_words

