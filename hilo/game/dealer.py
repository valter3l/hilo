# It might have a director and a chooser?
# it should generate random numbers from 1 to 13
# player starts with 300 points
# player should get if the number is higher or lower
# dealer or director displays the card
# player gets 100 points if the card is guessed
# player loses 75 points if card is not guessed
# if player reaches 0 points game is over, otherwise player chooses to continue or not
# If a player decides not to play again the game is over
# from game.player import Player
import random
from game.player import Player


class Dealer:
    def __init__(self):
        self.playing = True
        self.player = Player()

    def input(self):
        self.player.get_card_number()

    def start_game(self):
        # if we are playing we need to get stuff
        while self.playing:
            self.out_puts()
            self.input()
            self.updates()
            self.keep()

    def updates(self):
        return self.player.points_calculation()

    def out_puts(self):

        self.player.get_card_number()
        print(f"\nThis card is {self.player.card_number}")

    def keep(self):
        keep = input("Keep playing? [y/n]")
        if keep == "y":
            self.playing = True
        elif keep == "n":
            self.playing = False