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


def play_hangman():
    print("Willkommen zu Hangman!")
    secret_word = input("Spieler 1, gib das geheime Wort ein (sichtbar!): ")
    game = HangmanGame(secret_word)

    print("\n" * 50)  # Simuliert "Bildschirm löschen", damit Spieler 2 das Wort nicht sofort sieht

    while not game.is_game_over():
        game.display_progress()
        guess = input("Spieler 2, gib einen Buchstaben ein: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Bitte gib genau einen Buchstaben ein.")
            continue
        game.guess_letter(guess)

    print("\n--- Spiel beendet! ---")
    if game.is_word_guessed():
        print("🎉 Glückwunsch, du hast das Wort erraten!")
    else:
        print(f"😢 Leider verloren. Das Wort war: {game.word}")
    game.display_progress()


if __name__ == "__main__":
    play_hangman()
