# This is my try of Hangman via Git

print("Welcome to Hangman!")

class HangmanGame:
    def __init__(self, word, max_attempts=6):
        self.word = word.lower()
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.max_attempts = max_attempts

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print(f"'{letter}' was already guessed.")
            return
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.wrong_guesses += 1
            print(f"Wrong guess! Attempts left: {self.max_attempts - self.wrong_guesses}")
        else:
            print(f"Good guess!")

    def is_game_over(self):
        return self.wrong_guesses >= self.max_attempts or self.is_word_guessed()

    def is_word_guessed(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def display_progress(self):
        progress = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(f"Word: {progress}")



