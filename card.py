from card_formatter import CARD_EMOJIS

class Card:
    """
    A standard card class with ranks between 2 and 10, along with face cards
    and suits of Spades Clubs Diamonds and Hearts

    Build a dictionary, as a class attribute, with keys
    that represent the card ranks 11-14 and values with their card names, e.g.
    Jack, Queen, King, Ace - call it RANKS_TO_VALUES.
    """
    # CLASS ATTRIBUTES GO HERE.

    def __init__(self, rank, suit):
        """
        Initialize a card using the rank and suit passed as arguments.

        >>> c = Card(2, 'Spades')
        >>> c # this calls upon the __repr__ method so you will see 2 ♠ output.
        2 ♠
        >>> c.rank
        2
        >>> c.suit # a direct reference to the suit like this will return the string.
        'Spades'
        >>> c.RANKS_TO_VALUES
        {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        >>> k = Card(13, 'Diamonds')
        >>> k
        K ♦
        >>> k.rank
        13
        >>> k.suit 
        'Diamonds'
        """


    # Dunder Methods for Card    
    def __eq__(self, card):
        """
        Implement the dunder equals method for cards.

        # NOTE: in Crazy Eights, cards are equal if their rank
        or their suit match!

        >>> c = Card(2, 'Spades')
        >>> k = Card(13, 'Diamonds')
        >>> another_two = Card(2, 'Hearts')
        >>> another_spade = Card(3, 'Spades')
        >>> c == k
        False
        >>> c == another_two
        True
        >>> c == another_spade
        True
        """

    
    def __ne__(self, card):
        """
        Implement the dunder not equals method for cards. 

        # NOTE: in Crazy Eights, cards are not equal if neither
        # their rank or suit match!
        
        >>> c = Card(2, 'Spades')
        >>> k = Card(13, 'Diamonds')
        >>> another_two = Card(2, 'Hearts')
        >>> c != k
        True
        >>> c != another_two
        False
        """

    
    def __str__(self):
        """
        This method is implemented for you, but requires a correctly
        defined RANKS_TO_VALUES dictionary.
        """
        def get_suit_emoji(suit):
            return CARD_EMOJIS.get(suit)
        
        rank = self.rank
        emoji = get_suit_emoji(self.suit)
        return f'{rank} {emoji}' if self.rank < 11 else f'{Card.RANKS_TO_VALUES.get(rank)[0]} {emoji}'
    
    def __repr__(self):
        """
        This method is implemented for you, but requires a correctly
        defined RANKS_TO_VALUES dictionary.
        """
        def get_suit_emoji(suit):
            return CARD_EMOJIS.get(suit)
        
        rank = self.rank
        emoji = get_suit_emoji(self.suit)
        return f'{rank} {emoji}' if self.rank < 11 else f'{Card.RANKS_TO_VALUES.get(rank)[0]} {emoji}'
    

    # Card Methods
    def get_rank(self):
        """
        This is a 'getter' method.
        Simply return the rank of the card.

        >>> c = Card(2, 'Spades')
        >>> k = Card(13, 'Diamonds')
        >>> c.get_rank()
        2
        >>> k.get_rank()
        13
        """

    
    def get_suit(self):
        """
        This is a 'getter' method.
        Simply return the (non-emoji) suit of the card.

        >>> c = Card(2, 'Spades')
        >>> k = Card(13, 'Diamonds')
        >>> c.get_suit()
        'Spades'
        >>> k.get_suit()
        'Diamonds'
        """

    
    def set_suit(self, new_suit):
        """
        This method is implemented for you!
        DO NOT MODIFY
        
        This is a 'setter' method for suit so that
        crazy eights can change suit.

        >>> c = Card(2, 'Spades')
        >>> k = Card(13, 'Diamonds')
        >>> c.set_suit('Diamonds')
        >>> c.suit
        'Diamonds'
        >>> k.set_suit('Clubs')
        >>> k.suit
        'Clubs'
        """
        self.suit = new_suit