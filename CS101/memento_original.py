from cs1graphics import *
import time
import random

canvas = Canvas(640, 580)
canvas.setTitle("Memento")

path = ""
names = ("Dohoo.jpg", "Jeongmin.jpg", "Jinyeong.jpg", "Minsuk.jpg", "Sangjae.jpg", "Sungeun.jpg")

cards = []
num_pads = []
tries = 1
correct_list = []

def initialize():
    list=[]
    x=0
    while True:
        r=random.randint(0,5)
        if r not in list: 
            list.append(r)
            x+=1
        if x==6:
            break
    
    print(list)

    # initialize cards
    for i in range(6):
        for k in range(4):
            img = Image(path+names[list[i]])
            temp_tuple = (img, names[list[i]])
            cards.append(temp_tuple)
    """
    for j in range(24):
        print(cards[j][1])
        print(" ")
    """
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

def print_cards():
    print(cards)
    print(num_pads)
    pass
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range(len(num_pads)):
        ################################################################
        if i%2 == 0:    # 3-2-2. rewrite the condition for visualization.
        ################################################################
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

def is_valid(num1, num2):
    ###########################################################################
    # 3-1-1. Check if any of two numbers exists in the current correct list,
    #        two numbers are the same,
    #        or both of the numbers are within a valid range.
    # Return Boolean value according to the result.
    ###########################################################################
    return False

def check(num1, num2):
    ###########################################################################
    # 3-1-2. At first, visualize the screen including the two cards
    #        (num1-th card and num2-th card).
    #        If two pictures of the two cards are same,
    #        put two numbers into the correct list.
    #        If not, re-visualize the original screen.
    # Return Boolean value according to the result.
    ###########################################################################
    print_cards()
    return False

initialize()
print_cards()
print("### Welcome to the Python Memento game!!! ###")