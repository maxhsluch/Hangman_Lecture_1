# This is my try of Hangman via Git

print("Welcome to Hangman!")

class Hangman:
    def __init__(self, word, max_attempts=6):
        self.word = word.lower()
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.max_attempts = max_attempts
        


