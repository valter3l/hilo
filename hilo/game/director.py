from game.HiLoCard import Card

class Director:
    """
    A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        current (Card): A current card object
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.current = Card()
        self.is_playing = True
        self.score = 300


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.do_outputs()
        while self.is_playing:
            self.do_outputs()

    def get_total_score(self):
         """Updates the total game score based on the values guessed.
        
        Args:
            self (Director): an instance of Director.
        """
        self.difference = self.next.value - self.current.value
        if (self.guess == "h" and self.difference > 0) or (self.guess == "l" and self.difference < 0):
            self.score += 100
        else:
            self.score -= 75


    def do_outputs(self):
         """Displays the current card and the score. Generates the next card. Compares the player guesses with the next card Also asks the player if he wants to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        self.next = Card()
        while self.next.value == self.current.value:
            self.next = Card()
        print("The card is {}".format(self.current.value))
        self.guess = input("Higher or lower? [h/l] ")
        guess_acceptable = ["h", "H", "l", "L"]
        while self.guess not in guess_acceptable:
            print ("You entered an invalid answer.")
            self.guess = input("Higher or lower? [h/l] ")
        print("Next card was {}".format(self.next.value))
        self.get_total_score()
        print ("Your score is {}".format(self.score))
        self.current = self.next
        if self.score <= 0:
           self.is_playing = False
        playing = input("Play again? [y/n] ")
        print()
        playing_acceptable = ["y", "Y", "n", "N"]
        while playing not in playing_acceptable:
            print ("You entered an invalid answer.")
            playing = input("Play again? [y/n] ")
        if playing == "n" or playing == "N":
        self.is_playing = False
