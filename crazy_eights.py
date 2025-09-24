from typing import List
from user_player import UserPlayer
from deck import Deck

class CrazyEights:
    """
    A class representing a game of CrazyEights with a Deck of Cards
    and UserPlayers.
    """
    def __init__(self, players: List[UserPlayer], current_suit='Spades', crazy_deck=None):
        """
        - Initialize self.players to the players parameter.
        - Initialize current_suit to current_suit, ensure the default argument of 
        current_suit is 'Spades'.
        - Initialize crazy_deck to the crazy_deck argument if given, or Deck() + Deck() otherwise.

        Use this exact expression for the deck:
        self.crazy_deck = crazy_deck if crazy_deck is not None else Deck() + Deck()

        The final line of the constructor should shuffle the crazy_deck using
        the appropriate method.

        >>> p1, p2 = UserPlayer("Tom"), UserPlayer("Sheri")
        >>> new_game = CrazyEights([p1, p2])
        >>> new_game.players
        [Tom - Hand:, Sheri - Hand:]
        """

    def deal_cards(self):
        """
        Deal 7 cards to each player in the game.

        Steps:
        1. Loop through each player.
        2. WHILE that player's hand length is < 7.
            a. draw a card from the crazy_deck
            b. have the current player accept that card.
        
        This method should not return anything!

        >>> p1, p2 = UserPlayer("Tom"), UserPlayer("Sheri")
        >>> new_game = CrazyEights([p1, p2])
        >>> new_game.players 
        [Tom - Hand:, Sheri - Hand:]
        >>> new_game.deal_cards()
        >>> len(p1.hand)
        7
        >>> len(p2.hand)
        7
        """


    # DO NOT MODIFY THESE METHODS!
    # Display / Output Methods
    def display_current_card_to_match(self, discard_top):
        print("\n\tCard to match:")
        print('\t'+'-'*10)
        print(f'\t    {discard_top}')
        print('\t'+'-'*10)

    def display_crazy_eight_interaction(self, name, card):
        print("CRAZY EIGHT DETECTED!")
        # TODO: Clear up use of .get_name() over __repr__() here
        print(f'Player: {name} plays:')
        print(f'{card}')

    def display_players_move(self, name, card):
        print(f'Player {name} plays: ')
        print(card)

    # DO NOT MODIFY THESE METHODS!
    # Game State Methods
    def check_for_empty_player_hand(self, current_player):
        return current_player.hand_is_empty()   
    
    def temporarily_change_eight_suit(self, card, user_suit_choice):
        card.set_suit(user_suit_choice)

    # Primary Game Loop
    def play_crazy_eights(self):

        print("\t\tCrAzY EiGhTs!")

        # deal the cards using the correct method.


        # draw from crazy_deck using the correct method, and store it in 
        # a variable representing the "top of the discard deck"
        # (this is the card that a player will have to match.)


        # DO NOT MODIFY THIS CODE - This runs the game while everyone has cards
        # and there are cards remaining in the deck.
        while self.crazy_deck.cards and all(player.hand for player in self.players):
            """
            Crazy Eight Game Algorithm Steps

            1. For each player, get their move - they must play a valid card or continue drawing until
                they can play.

            2. If they do not have a valid card, they must draw and then effectively restart their turn
                UNTIL they have a valid card to play.
                
            3. Otherwise, if they plan a card with rank 8, display a "crazy eight" message and the card, 
                and let the player choose the new suit.

            4. Otherwise, if it's a valid card, simply display the played card.

            5. After the above criteria have been correctly evaluted for that player, replace
                the "discard pile" top card with the player's card.

            # NOTE: Use the correct abstractions/methods for each step.  Pay close attention to the comments!
            """

            # for each player in the game. (what kind of loop do you need?)
            # and what should it loop over?

            # NOTE: PAY VERY CLOSE ATTENTION to indentation in these comments.  They are indented
            # correctly based on where your code should be!

                
                # get the player's name for this round using the correct method
                # store it in a well-named variable.


                # the player must PLAY / DRAW UNTIL they have a valid card.
                # the player should have the chance to play each time they draw.
                # NOTE: UNTIL means a certain type of loop is necessary here!
               
                    # display the current card to match using the correct method.
                    # and pass the top card of the discard pile as the argument.
                    

                    # use the .play() method correctly and store the player's chosen card.
                    # note the behavior of .play() if the player does NOT have a valid card.
                    

                    # If the player cannot play based on what .play() returned

                        # use the correct deck method to draw a card
                        # and have the player accept it.
                        

                        # use the continue keyword to start the play process over for
                        # the CURRENT player.
                        

                    # otherwise if the drawn card's rank is 8
                    

                        # use the display crazy eight interaction method.
                        
                        
                        # OPTIONAL FEATURE - Let the player change the suit of the 8 when they play it, per
                        # original Crazy Eight Rules.  DO NOT UNCOMMENT UNTIL ALL OTHER FEATURES ARE FINISHED!

                        # suit_choice = player.get_user_suit_choice()
                        # self.temporarily_change_eight_suit(player_card, suit_choice)

                        
                    # otherwise if the player successfully plays a non-8
                    

                        # call the display player move function
                        
        
                    
                # within the for player in players loop, but NOT inside any if statement, replace the
                # top card of the discard pile with the player's card.
                # HINT: you're just changing what's stored in a variable here!
                

                # check for a victory condition
                # use the correct method to check for an empty player hand
                # they win immediately if that method returns True
                
                    # Print a victory message with the player's name
                    # and break the while loop.
                    
            
                    

    

    
        
            

    