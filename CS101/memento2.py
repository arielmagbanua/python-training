from cs1graphics import *
import time
from random import shuffle

canvas = Canvas(640, 580)
canvas.setTitle("Memento")

path = "D:\\Training\\python-training\\CS101\\images\\"
names = ("Dohoo.jpg", "Jeongmin.jpg", "Jinyeong.jpg", 
         "Minsuk.jpg", "Sangjae.jpg", "Sungeun.jpg")

cards = []
num_pads = []
tries = 1

class Card:
    def __init__(self, value):
        self.value = value

        if type(value) == int:
            number_layer = Layer()
            rect = Rectangle(90, 120, Point(0, 0))
            text = Text(str(value), 18, Point(0, 0))
            number_layer.add(rect)
            number_layer.add(text)
            self.image = number_layer
        else:
            self.image = Image(path + value)

        self.guessed = False


def initialize():
    # initialize cards
    for i in range(len(names)):
        for k in range(4):
            # images won't load in windows 10 replace it with text
            card = Card(names[i])
            cards.append(card)

    for i in range(24):
        card = Card(i)
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
    for i in range(len(cards)):
        ################################################################
        # if i%2 == 0:    # 3-2-2. rewrite the condition for visualization.
        ################################################################
        cards[i].image.moveTo(i_w + w, i_h + h)
        canvas.add(cards[i].image)

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
        if cards[i].guessed:
            cards[i].image.moveTo(i_w + w, i_h + h)
            canvas.add(cards[i].image)
        else:
            num_pads[i].image.moveTo(i_w + w, i_h + h)
            canvas.add(num_pads[i].image)

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
            cards[i].image.moveTo(i_w + w, i_h + h)
            canvas.add(cards[i].image)
        elif cards[i].guessed:
            cards[i].image.moveTo(i_w + w, i_h + h)
            canvas.add(cards[i].image)
        else:
            num_pads[i].image.moveTo(i_w + w, i_h+h)
            canvas.add(num_pads[i].image)

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
    card1 = cards[num1]
    card2 = cards[num2]
    if card1.guessed or card2.guessed:
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

    card_value1 = cards[num1].value
    card_value2 = cards[num2].value

    if card_value1 == card_value2:
        cards[num1].guessed = True
        cards[num2].guessed = True
        ret_val = True

    # re-visualize the original screen
    print_cards_with_guessed()

    return ret_val

initialize()
print_cards()
print("### Welcome to the Python Memento game!!! ###")

guessed_count = 0

###############################################################################
while guessed_count < (len(names) * 4): # 3-2-3. Rewrite the condition for termination
###############################################################################

    ###########################################################################
    # 3-2-4. Print the number of tries and the corrected pairs
    print(str(tries) + "th try. You got " + str(guessed_count//2) + " pairs.")
    ###########################################################################
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if not is_valid(num1, num2):
        continue

    if check(num1, num2):
        print("Correct!")
        guessed_count += 1
    else:
        print("Wrong!")
    
    ###########################################################################
    # 3-2-5. Update number of tries (global variable, tries)
    ###########################################################################
    tries += 1
