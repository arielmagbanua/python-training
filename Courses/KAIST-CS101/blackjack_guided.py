from random import *
from cs1graphics import *

# img_path = './images/'
img_path = 'D:\\Training\\python-training\\CS101\\images\\'

suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



bj_board = Canvas(600, 400, 'dark green', 'Black Jack 101')


"""
Define the Card class
"""
class Card:
    def __init__(self, suit, face, value, state):
        self.suit = suit
        self.face = face
        self.value = value
        self.state = state

    # This is called automatically everytime we set a value to an attribute
    def __setattr__(self, name, value):
        # change or assing the correct image base on state
        if name == 'state':
            if value:
                # this means card is not hidden or the card is face up
                path = ('%s%s_%s.png' % (img_path ,self.suit, self.face))
                self.image = Image(path)
            else:
                # this means card is hidden or the card is face down
                path = ('%sBack.png' % (img_path))
                self.image = Image(path)

        object.__setattr__(self, name, value)



def create_deck(number = 1):
    """
    Create a list("deck") of all 52 cards, shuffle them and return the list.
    The list 'deck' have to include Card objects
    A Card is represented by a object with four attributes: the face, the suit, value, state, and the image object
    First, Have to define class 'Card'
    """
    # prepare the deck
    deck = []

    # create the 52 cards for the deck
    for suit in suit_names:
        for i in range(len(face_names)):
            card = Card(suit, face_names[i], value[i], True)
            deck.append(card)
    
    # shuffle and return the deck
    shuffle(deck)
    return deck



def hand_value(hand):
    """
    hand is a list including card objects
    Compute the value of the cards in the list "hand"
    """

    # hand_value = sum([card.value for card in hand])
    # return hand_value
    hand_value = 0
    for card in hand:
        hand_value += card.value

    return hand_value



def card_string(card):
    """
    Parameter "card" is a Card object
    Return a nice string to represent a card
    (sucn as "a King of Spades" or "an Ace of Diamonds")
    """

    face = card.face
    determiner = 'a'

    if face == '8' or face == 'Ace':
        determiner = 'an'

    return '%s %s of %s' % (determiner, card.face, card.suit)



def ask_yesno(prompt):
    """
    Display the text prompt and let's the user enter a string.
    If the user enters "y", the function returns "True",
    and if the user enters "n", the function returns "False".
    If the user enters anything else, the function prints "I beg your pardon!", and asks again,
	repreting this until the user has entered a correct string.
    """

    user_input = ''

    while user_input != 'y' and user_input != 'n':
        user_input = input(prompt)

        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('I beg your pardon!')



def draw_card(dealer, player):
    """
    This funuction add the cards of dealer and player to canvas, bj_board.
    If the state of each Card object is false, then you have to show the hidden card image(Back.png).
	The dealer's first card is hidden state.
    The parameter dealer and player are List objects including Card Objects.

    The start position of dealer's card is (100,100).
    The start position of player's card is (100,300).

    You can use the following methods for positioning images and text:
    Image() Object, Text() Object, moveTo() method, setDepth() method.

    You should use help function -
    help('cs1graphics.Image') -> about Image(), moveTo(), setDepth()
    help('cs1graphics.Text') -> about Text(),moveTo(), setDepth()
    """
    bj_board.clear()

    # start position of dealer's cards
    x0, y0 = 35, 0

    # start position of player's cards
    x1, y1 = 35, 200

    # the dimension of each cards
    i_w = 72
    i_h = 100

    # this is the amount per loop where we move x coordinate of printing
    slide_amount = 20

    depth = 100
    # dealer = dealer[::-1]
    for card in dealer:
        card_image = card.image
        card_image.moveTo(x0 + i_w, y0 + i_h)
        card_image.setDepth(depth)
        bj_board.add(card_image)

        x0 += slide_amount
        depth -= 5

    # get the total hand value of dealer
    dealer_hand_value = hand_value(dealer)
    text_str = "The dealer's Total: %d" % (dealer_hand_value)
    text_layer = Layer()
    text = Text(text_str, 14, Point(400, 100))
    text.setFontColor(Color('greenyellow'))
    text_layer.add(text)
    bj_board.add(text_layer)

    depth = 100
    # player = player[::-1]
    for card in player:
        card_image = card.image
        card_image.moveTo(x1 + i_w, y1 + i_h)
        card_image.setDepth(depth)
        bj_board.add(card_image)

        x1 += slide_amount
        depth -= 5

    # get the total hand value of player
    player_hand_value = hand_value(player)
    text_str = "Your Total: %d" % (player_hand_value)
    text_layer = Layer()
    text = Text(text_str, 14, Point(431, 300))
    text.setFontColor(Color('greenyellow'))
    text_layer.add(text)
    bj_board.add(text_layer)

def main():
    deck = []

    while True:
        # prompt for starting a new game and create a deck
        print ("Welcome to Black Jack 101!\n")
        if len(deck) < 12:
            deck = create_deck()

        # create two hands of dealer and player
        dealer = []
        player = []

        # initial two dealings
        card = deck.pop()
        print ("You are dealt " + card_string(card))
        player.append(card)

        card = deck.pop()
        print ("Dealer is dealt a hidden card")
        card.state=False
        dealer.append(card)

        card = deck.pop()
        print ("You are dealt " + card_string(card))
        player.append(card)

        card = deck.pop()
        print ("Dealer is dealt " + card_string(card))
        dealer.append(card)

        print ("Your total is", hand_value(player))
        draw_card(dealer, player)

        # player's turn to draw cards
        while hand_value(player) < 21 and ask_yesno("Would you like another card? (y/n) "):
            # draw a card for the player
            card = deck.pop()
            print ("You are dealt " + card_string(card))
            player.append(card)
            print ("Your total is", hand_value(player))

        draw_card(dealer, player)

        # if the player's score is over 21, the player loses immediately.
        if hand_value(player) > 21:
            print ("You went over 21! You lost.")
            dealer[0].state = True
            draw_card(dealer, player)
        else:
            # draw cards for the dealer while the dealer's score is less than 17
            print ("\nThe dealer's hidden card was " + card_string(dealer[0]))
            while hand_value(dealer) < 17:
                card = deck.pop()
                print ("Dealer is dealt " + card_string(card))
                dealer.append(card)
                print ("The dealer's total is", hand_value(dealer))

            dealer[0].state = True
            draw_card(dealer, player)

            # summary
            player_total = hand_value(player)
            dealer_total = hand_value(dealer)
            print ("\nYour total is", player_total)
            print ("The dealer's total is", dealer_total)

            if dealer_total > 21:
                print ("The dealer went over 21! You win!")
            else:
                if player_total > dealer_total:
                    print ("You win!")
                elif player_total < dealer_total:
                    print ("You lost!")
                else:
                    print ("You have a tie!")

            if not ask_yesno("\nPlay another round? (y/n) "):
                bj_board.close()
                break

main()

