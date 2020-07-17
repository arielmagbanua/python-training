import a3

words_list_file_name = 'wordlist1.txt'
board_file_name = 'board1.txt'

words_file = open(words_list_file_name, 'r')
board_file = open(board_file_name, 'r')

print(a3.read_words(words_file))
print(a3.read_board(board_file))


# lines = words_file.readlines()
#
# for word_index in range(len(lines)):
#     lines[word_index] = lines[word_index].rstrip('\n')

