import time
import random
import os

# create num_pads list with 24 0 items
num_pads = [' '] * 24

# accumulator of correctly guesses cells
correct_list = []

# items to guess
items = ('A', 'X', 'O')

# number of pairs
num_pairs = 3

# generate the cell indices that will hold the pairs
occupied_cells = random.sample(range(24), 2 * num_pairs)

def initialize():
    for item in items:
        # pop 2 slots for the current item
        num1 = occupied_cells.pop()
        num2 = occupied_cells.pop()

        # fill num_pad with the item's designated slots
        num_pads[num1] = str(item)
        num_pads[num2] = str(item)

def clear():
    # this works on windows only
    os.system('cls')

def print_cards():
    '''
    This prints the card pairs to guess for 2 seconds and then prints the faced down version
    '''
    clear()

    rows = int(len(num_pads) / 6)

    from_index = 0
    to_index = 0

    # print all the locations of each pair
    print('------------------------------')
    for row in range(1, rows+1):
        to_index = row * 6
        print(num_pads[from_index:to_index])
        from_index = to_index
    print('------------------------------')
    
    time.sleep(3)

    print_facedown_cards()

def print_facedown_cards():
    '''
    print blank cards which represents faced down cards.
    '''

    clear()

    # print facedown cards
    temp_list = [' '] * 24
    temp_rows = int(len(temp_list) / 6)
    from_index = 0
    to_index = 0

    print('------------------------------')
    for row in range(1, temp_rows+1):
        to_index = row * 6
        print(temp_list[from_index:to_index])
        from_index = to_index
    print('------------------------------')

def is_valid(cell_index1, cell_index2):
    '''
    Check if the two numbers:
        * Exist in the current correct list
        * Are the same number
        * Are valid numbers in the givent range

    Return Boolean value according to the result
    '''

    # same cell index is not valid
    if cell_index1 == cell_index2:
        return False

    # check if the cell already have been guessed
    # return false if any of the cell index already recorded in correct_list
    if cell_index1 in correct_list or cell_index2 in correct_list:
        return False

    # verify the number is in the range of num_pads
    if cell_index1 > (len(num_pads) - 1) or cell_index2 > (len(num_pads) - 1):
        return False
    
    return True

def check(cell_index1, cell_index2):
    cell_value1 = num_pads[cell_index1]
    cell_value2 = num_pads[cell_index2]

    # print their location

    if (cell_value1 != ' ' and cell_value2 != ' ') and (cell_value1 == cell_value2):
        correct_list.append(cell_value1)
        correct_list.append(cell_value2)
        return True
    
    return False

def game_end():
    return items * 2 == len(correct_list)

def ask_pair():
    while True:
        try:
            pair_input = input('Please enter a pair of index/number (num,num): ')
            if pair_input == 'end':
                return None, None

            # split the input
            num1, num2 = pair_input.split(',')
        
            # strip to remove excess space and convert to int
            num1 = int(num1.strip())
            num2 = int(num2.strip())

            return num1, num2
        except:
            continue

def start_game(attempts=4):
    initialize()

    while attempts > 0:
        print_cards()

        num1, num2 = ask_pair()

        if num1 and num2:
            # check if valid
            if not is_valid(num1, num2):
                print('Invalid pair!')
                continue

            if check(num1, num2):
                print('Correct!')
            else:
                print('Wrong...')

        # check if game has ended
        if game_end():
            break

        attempts -= 1

start_game()
