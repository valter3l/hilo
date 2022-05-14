import random


class Player:
    def __init__(self):
        self.card_number = 0
        self.player = 0
        self.card_number = 0
        self.score = 300

    def get_card_number(self):
        self.card_number = random.randint(1, 13)

    def points_calculation(self):
        self.get_card_number()
        card_guess = input("Higher or lower? [h/l]: ")
        second_number = random.randint(1, 13)
        if second_number >= self.card_number and card_guess == "h":
            self.score += 100
        elif second_number <= self.card_number and card_guess == "h":
            self.score -= 75
        elif second_number >= self.card_number and card_guess == "l":
            self.score -= 75
        elif second_number <= self.card_number and card_guess == "l":
            self.score += 100
        print(f"Next card was:{second_number}")
        print(f"Your score is: {self.score}")