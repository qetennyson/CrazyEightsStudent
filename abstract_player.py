class Player:
    """
    Parent class for all players in Crazy Eights
    """
    def __init__(self, name, hand=None):
        """
        Initialize a Player with a name and optional hand.
        
        The hand attribute should be set to the passed argument
        if it is not None, otherwise, set the hand attribute to 
        an empty list.

        HINT: (hand if hand is not None else [])
        
        >>> from card import Card
        >>> empty_hand = []
        >>> p1 = Player("Alice", empty_hand)
        >>> p2 = Player("Bob", [Card(2, "Spades"), Card(10, "Diamonds")])
        >>> p1.name
        'Alice'
        >>> len(p1.hand)
        0
        >>> len(p2.hand)
        2
        """

    # Abstract Player Behaviors
    def get_name(self):
        """
        Return only the player's name.
        """

    def accept_card(self, card):
        """
        Accept a single card and add it to the player's hand.
        Additionally, print the card which was accepted.

        >>> from card import Card
        >>> p = Player("Alice")
        >>> card = Card(10, "Hearts")
        >>> p.accept_card(card)
        >>> len(p.hand)
        1
        >>> p.hand[0] == card
        True
        """


    def play(self):
        """
        Make a decision about how to play (hit or stay).
        
        This method will be OVERRIDEN by subclasses.  For example, UserPlayer
        will get the input from the user on what they want to do.  On the other
        hand the Dealer must be play based on house rules.

        This abstract method should simply return True.

        >>> p = Player("Alice")
        >>> p.play()
        True
        """


    # Check Hand State
    def hand_is_empty(self):
        """
        Return True if no cards remain in the player's hand.

        >>> from card import Card
        >>> p = Player("Alice")
        >>> p.hand
        []
        >>> p.hand_is_empty()
        True
        >>> card = Card(10, "Hearts")
        >>> p.accept_card(card)
        >>> len(p.hand)
        1
        >>> p.hand_is_empty()
        False
        """


    # Display / Output Methods - DO NOT MODIFY
    def display_hand(self):
        """
        This method is implemented for you.
        DO NOT MODIFY THIS CODE.
        """
        print(f'\n{self.name}')
        output = ''
        for card_index in range(len(self.hand)):
            output += f'{card_index+1}. |' + str(self.hand[card_index]) + '|  '
        print(output)

    def __repr__(self):
        """
        This method is implemented for you.
        DO NOT MODIFY THIS CODE.
        """
        return f"{self.name} - Hand:{''.join(self.hand)}"