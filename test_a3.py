import a3

words_list_file_name = 'wordlist1.txt'
board_file_name = 'board1.txt'

words_file = open(words_list_file_name, 'r')
board_file = open(board_file_name, 'r')

# print(a3.read_words(words_file))
# print(a3.read_board(board_file))

# lines = words_file.readlines()
#
# for word_index in range(len(lines)):
#     lines[word_index] = lines[word_index].rstrip('\n')

# print(a3.make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0))
# print(a3.make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1))
# print(a3.make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2))
# print(a3.make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 3))
# print(a3.make_str_from_column([['A', 'N', 'T'], ['X', 'S', 'O', 'B']], 3))


# print(a3.board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO'))
# print(a3.board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NS'))
# print(a3.board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'AX'))
# print(a3.board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TB'))

# ['A', 'N', 'T', 'T']
# ['X', 'S', 'O', 'B']
# ['B', 'S', 'I', 'T']
three_row_board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['B', 'S', 'I', 'T']]
print(a3.board_contains_word_in_column(three_row_board, 'TB'))
print(a3.board_contains_word_in_column(three_row_board, 'XB'))

