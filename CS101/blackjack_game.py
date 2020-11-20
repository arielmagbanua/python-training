from random import *
from cs1graphics import Image
from cs1graphics import Canvas

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
    
    def __setattr__(self, name, value):
        if name == 'state':
            if value:
                # use the correc face image
                path = '{}{}_{}.png'.format(img_path, self.suit, self.face)
                self.image = Image(path)
            else:
                # use Back image since his card is hidden
                self.image = Image(img_path + 'Back.png')

        # set the properties as usual
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

    values = [card.value for card in hand]
    return sum(values)



def card_string(card):
    """
    Parameter "card" is a Card object
    Return a nice string to represent a card
    (sucn as "a King of Spades" or "an Ace of Diamonds")
    """

    vowels = 'aeiou'
    
    # set the determiner to 'a' initially
    determiner = 'a'

    if card.face[0].lower() in vowels:
        determiner = 'an'

    return '{} {} of {}'.format(determiner, card.face, card.suit)



def ask_yesno(prompt):
    """
    Display the text prompt and let's the user enter a string.
    If the user enters "y", the function returns "True",
    and if the user enters "n", the function returns "False".
    If the user enters anything else, the function prints "I beg your pardon!", and asks again,
	repreting this until the user has entered a correct string.
    """

    while True:
        # print(prompt)
        user_input = input(prompt)

        if user_input != 'y' and user_input != 'n':
            print('I beg your pardon!')
            continue
            
        if user_input == 'y':
            return True
        else:
            return False



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

    # start position of dealer's card
    x0, y0 = 0, 0

    # start position of player's card
    x1, y1 = 0, 200

    # the dimension of each cards
    i_w = 72
    i_h = 100

    # the amount of sliding during drawing of cards
    slide_amount = 20

    dealers_hand_total = 0
    players_hand_total = 0

    # draw dealer cards
    depth = 100
    for i in range(len(dealer)):
        card_image = dealer[i].image
        card_image.moveTo(i_w + x0, i_h + y0)
        card_image.setDepth(depth)
        bj_board.add(card_image)

        x0 += slide_amount
        depth -= 1

    # draw player cards
    depth = 100
    for i in range(len(player)):
        card_image = player[i].image
        card_image.moveTo(i_w + x1, i_h + y1)
        card_image.setDepth(depth)
        bj_board.add(card_image)

        x1 += slide_amount
        depth -= 1


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

# help('cs1graphics.Image')