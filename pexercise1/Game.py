from random import random


class NumberGuesser:
    def __init__(self, secret_number=random.randint(1, 100), attempts=[]):
        self.number = secret_number
        self.attempts = attempts

    def guess(self,number):
        if number == self.number:
            print("You won after", self.attempts, "attempts")
        else:
            if number > self.number:
                print("Lower")
            else:
                print("Higher")

