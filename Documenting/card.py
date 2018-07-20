import random

class Card:
    """
    The card class represents a single playing card
    and is initialised by passing a suit and number.
    """
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """Gets or sets the suit of the card"""
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """Gets the number of the card in the form  2-10 or J Q K A"""
        return self._number

    @number.setter
    def number(self, number):
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:
    """
    The Deck class represents a deck of playing cards in order
    """
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        """Populate (resets) the deck of cards with all 52 cards in the order
    2-10, J, Q, K, A, Hearts, Clubs, Diamonds, Spades""" 
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        """Shuffles the deck in a random order of playing cards"""
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """Deals (and removes) a number of cards from the deck"""
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
        
deck = Deck()
print(deck)
