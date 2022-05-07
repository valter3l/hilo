from game.HiLoCard import Card


class Director:

    def __init__(self):
        self.current = Card()
        self.is_playing = True
        self.score = 300


    def start_game(self):
        self.do_outputs()
        while self.is_playing:
            self.do_outputs()

    def get_total_score(self):
        self.difference = self.next.value - self.current.value
        if (self.guess == "h" and self.difference > 0) or (self.guess == "l" and self.difference < 0):
            self.score += 100
        else:
            self.score -= 75


    def do_outputs(self):
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