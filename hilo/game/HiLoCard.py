import random

class Card:
     """A small card set with individual cards represented as a number from 1 to 13.

    The responsibility of Card is to generate a random value to a card in the range 1 to 13
   
    Attributes:
        value (int): The value of the card.
    """
    def __init__(self):
         """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)
