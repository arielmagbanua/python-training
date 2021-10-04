class WordCountMap:
    def __init__(self, words):
        self.words = words
    
    def get_map(self):
        word_dict = {}

        # loop through each word and tally the count
        for word in self.words:
            if word.isalpha():
                # the word is legit word then tally
                # the occurence in the word dictionary
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    # not yet existed therefore initialize to 1
                    word_dict[word] = 1
        
        return word_dict
