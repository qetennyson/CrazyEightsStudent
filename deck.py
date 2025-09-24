from card import Card
from random import shuffle

class Deck:
    """
    A class representing a deck of cards.
    """
    ranks = range(2,15)
    suits = 'Spades Clubs Hearts Diamonds'.split()

    def __init__(self, cards=None):
        """
        This constructor is built for you.  You must
        build a correct Card object for it to work properly!
                

        >>> a_deck = Deck()
        >>> len(a_deck.cards) # for testing only, you will never do this!
        52
        >>> a_deck.cards[0]
        2 ♠
        """
        if cards:
            self.cards = cards
        else:
            self.cards = [Card(rank, suit) for suit in Deck.suits for rank in Deck.ranks]

    # Dunder Methods for Deck
    def __len__(self):
        """
        Override the __len__() method to return the length of the deck

        >>> a_deck = Deck()
        >>> len(a_deck)
        52
        """

    
    def __setitem__(self, position, value):
        """
        Override the __setitem__() method so that it changes
        the element at position to value.

        >>> a_deck = Deck()
        >>> a_deck[0]
        2 ♠
        >>> a_deck[0] = Card(3, 'Clubs')
        """

  
    def __getitem__(self, position):
        """
        Override the __getitem__() method so that it returns
        the Card located at the given position in the Deck

        >>> a_deck = Deck()
        >>> a_deck[0]
        2 ♠
        """
    
    def __repr__(self):
        """
        Return a string that represents a deck with this format:
        'A card deck with {NUM_CARDS} cards'

        >>> a_deck = Deck()
        >>> a_deck
        A card deck with 52 cards
        """


    def __add__(self, other):
        """
        This method is implemented for you!
        
        Overrides the __add__() method so that it supports
        adding a Deck to a Deck, similarly to list concatenation.
        """
        if isinstance(other, Deck):
            return Deck(self.cards + other.cards)
        else:
            raise TypeError("Can only add other Decks to Deck!")
    

    # Deck Methods
    def draw(self):
        """
        Return the current last card in the deck.

        There is one ideal way to do this with Python!

        >>> a_deck = Deck()
        >>> a_deck.draw()
        A ♦
        """

    
    def shuffle_deck(self):
        """
        DO NOT MODIFY THIS CODE.
        This method is implemented for you.
        """
        shuffle(self.cards)
