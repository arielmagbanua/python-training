from cs1graphics import *
import time
from random import shuffle

canvas = Canvas(640, 580)
canvas.setTitle("Memento")

path = "./images/"
names = ("ariel.jpg", "howard.jpg", "leonard.jpg", 
         "rajesh.jpg", "sheldon.jpg", "yuri.jpg")

cards = []
num_pads = []
tries = 1
correct_list = []

def initialize():
    # initialize cards with empty tuples
    cards[:] = [('','')] * 12

    # initialize cards
    for i in range(6):
        for k in range(2):
            # images won't load in windows 10 replace it with text
            # img = Image(path+names[i])
            # temp_tuple = (img, names[i])
            # cards.append(temp_tuple)
            card = Layer()
            text = Text(str(names[i]), 12, Point(0, 0))
            temp_tuple = (text, names[i])
            cards.append(temp_tuple)

    for i in range(24):
        card = Layer()
        rect = Rectangle(90, 120, Point(0, 0))
        text = Text(str(i), 18, Point(0, 0))
        card.add(rect)
        card.add(text)
        num_pads.append(card)

    ################################################################
    # 3-2-1. shuffle the card list
    ################################################################
    shuffle(cards)

def print_cards():
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range(len(num_pads)):
        ################################################################
        # if i%2 == 0:    # 3-2-2. rewrite the condition for visualization.
        ################################################################
        if cards[i][0] != '':
            cards[i][0].moveTo(i_w + w, i_h+h)
            canvas.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h+h)
            canvas.add(num_pads[i])

        w += 100
        if w % 600 == 0:
            w = 0
            h += 130

    time.sleep(5)
    print_cards_with_guessed()

def print_cards_with_guessed():
    '''
    Print the guessed cards along with the normal num_pad cards
    '''
    canvas.clear()

    w = 0
    h = 0
    i_w = 70
    i_h = 90

    for i in range(len(num_pads)):
        if i in correct_list:
            cards[i][0].moveTo(i_w + w, i_h+h)
            canvas.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h+h)
            canvas.add(num_pads[i])

        w += 100
        if w % 600 == 0:
            w = 0
            h += 130

    time.sleep(1)

def print_cards_with_selected(num1, num2):
    '''
    Print all num_cards with the currently selected cards
    '''

    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90

    for i in range(len(num_pads)):
        if i == num1 or i == num2:
            if cards[i][0] != '': 
                cards[i][0].moveTo(i_w + w, i_h+h)
                canvas.add(cards[i][0])
            else:
                num_pads[i].moveTo(i_w + w, i_h+h)
                canvas.add(num_pads[i])
        else:
            num_pads[i].moveTo(i_w + w, i_h+h)
            canvas.add(num_pads[i])

        w += 100
        if w % 600 == 0:
            w = 0
            h += 130

    time.sleep(1)

def is_valid(num1, num2):
    ###########################################################################
    # 3-1-1. Check if any of two numbers exists in the current correct list,
    #        two numbers are the same,
    #        or both of the numbers are within a valid range.
    # Return Boolean value according to the result.
    ###########################################################################

    # same index number is not valid
    if num1 == num2:
        return False
    
    # verify the index number is in the range of num_pads
    if num1 > (len(num_pads) - 1) or num2 > (len(num_pads) - 1):
        return False

    # check if the index number already have been guessed
    # return false if any of the index number is already recorded in correct_list
    if num1 in correct_list or num2 in correct_list:
        return False

    return True

def check(num1, num2):
    ###########################################################################
    # 3-1-2. At first, visualize the screen including the two cards
    #        (num1-th card and num2-th card).
    #        If two pictures of the two cards are same,
    #        put two numbers into the correct list.
    #        If not, re-visualize the original screen.
    # Return Boolean value according to the result.
    ###########################################################################
    # print_cards()
    ret_val = False

    # visualize the board with the currently selected cards
    print_cards_with_selected(num1, num2)

    card_value1 = cards[num1][1]
    card_value2 = cards[num2][1]

    # only check if both values are not empty
    if card_value1 != '' and card_value2 != '':
       if card_value1 == card_value2:
            # nice both card has the same value therefore it is a pair
            # add them to the correct list
            correct_list.append(num1)
            correct_list.append(num2)
            ret_val = True

    # re-visualize the original screen
    print_cards_with_guessed()

    return ret_val

initialize()
print_cards()
print("### Welcome to the Python Memento game!!! ###")

###############################################################################
while len(correct_list) < (len(names) * 2): # 3-2-3. Rewrite the condition for termination
###############################################################################

    ###########################################################################
    # 3-2-4. Print the number of tries and the corrected pairs
    print(str(tries) + "th try. You got " + str(len(correct_list)//2) + " pairs.")
    ###########################################################################
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if not is_valid(num1, num2):
        continue

    if check(num1, num2):
        print("Correct!")
    else:
        print("Wrong!")
    ###########################################################################
    # 3-2-5. Update number of tries (global variable, tries)
    ###########################################################################
    tries += 1
