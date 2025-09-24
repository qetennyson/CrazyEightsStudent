from abstract_player import Player
from card_formatter import CARD_EMOJIS

class UserPlayer(Player):
    """
    Class for user players.

    Inherits the majority of its features from abstract player,
    but let's the user make play decisions.
    """

    def __init__(self, name, hand=None):
        """
        Initialize a UserPlayer using the super constructor method.

        >>> up = UserPlayer("Jim")
        >>> up.name
        'Jim'
        >>> isinstance(up, UserPlayer)
        True
        """
        super().__init__(name, hand)

    def get_user_play_input(self) -> int:
        """
        Steps for this method (no doctests)
        
        1. Display their hand using the correct method so they can decide
        what card to play by its position in their hand.

        while True:
            1. Gets input from the user to determine from what position
            in their hand they will play the card.

            2. However, if they choose to draw, input: 'd', return 'd' immediately.

            3. Convert the user input to an integer.

            4. Use the convert_numerical_choice_to_card(user_input_as_int) helper function
            to verify they have chosen a card that exists in their hand.

            5. If their valid card choice is a number that is between 0 and the length of the
            player's hand, return the card choice.
   
        Otherwise, continue the while loop so they have to choose another card.
        """
        self.display_hand()
        while True:
            print("Choose a valid card to play or [d]raw: ")
            user_input = input("> ").strip().lower()
            if user_input == 'd':
                return user_input
            
            # check valid card.
            user_input_as_int = int(user_input)
            
            # convert to a valid numerical choice.
            valid_numerical_card_choice = self.convert_numerical_choice_to_card(user_input_as_int)
            if valid_numerical_card_choice in range(0, len(self.hand)):
                return valid_numerical_card_choice
            else:
                continue    

    def convert_numerical_choice_to_card(self, players_numerical_card_choice):
        """
        This method is implemented for you.  
        DO NOT MODIFY THIS CODE.

        Read this code and use it to support your get_user_play_input() method.
        """
        to_index = players_numerical_card_choice - 1
        try:
            self.hand[to_index]
        except IndexError:
            print("No card in that slot.  Try a different value.")
            return False
        else:
            return to_index
            
    def play(self, current_card_to_match):
        """
        # IMPORTANT:  play() and get_user_play_input() are separate methods! 
        # This method uses get_user_play_input() as a helper method.

        Steps for this method (no doctests)
        
        while True:
            1. Use the get_user_play_input() method to get input 
            from the user for their play choice.

            2. If their input was 'd', then return False immediately.

            3. Otherwise, use their card input (an integer) as the index to
            access the correct card from their hand (self.hand) and store that in
            a variable which represents a "potentially valid card" to play.

            4. if that potential card either EQUALS the current_card_to_match OR
            the potential card's rank is 8
                a. .pop() that card from the hand by its index - 
                that index is whatever was returned by get_user_play_input()
               
                 b. return that card

            5. OTHERWISE, inform the user they tried to play a non-matching card 
            and let the loop run again.
        """
        while True:
            users_card_input = self.get_user_play_input()
            if users_card_input == 'd':
                return False
            
            potential_card = self.hand[users_card_input]

            if (potential_card == current_card_to_match) or potential_card.get_rank() == 8:
                # make sure you pop the potential card, based on index, if you've confirmed it.
                return self.hand.pop(users_card_input)
            else:
                print(f"You cannot play {potential_card}, try again!")
    
    def get_user_suit_choice(self):
        """
        This method is implemented for you.
        DO NOT MODIFY THIS CODE.

        # NOTE: This is an OPTIONAL feature implemented
        after you have completed the main project.
        
        Upon playing an 8 the user gets to choose a new, temporary suit
        for the current 8 card.
        """
        while True:
            print("Choose a new, temporary suit for the 8")
            for i, value in enumerate(CARD_EMOJIS.values()):
                print(f'{i+1}. {value}')
            
            try:
                suit_choice = int(input("> ").strip())
                if suit_choice not in range(1,5):
                    print("Value not recognized, choose [1-4]")
                    continue
            except ValueError:
                print("Value not recognized, choose [1-4]")
                continue
            else:
                choice_dict = {1: 'Spades', 2: 'Hearts', 3: 'Diamonds', 4: 'Clubs'}
                return choice_dict.get(suit_choice)

    
    