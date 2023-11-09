import random

class NumberGuessingGame:
    def __init__(self, min_number, max_number):
        self.min_number = min_number
        self.max_number = max_number
        self.secret_number = random.randint(min_number, max_number)
        self.attempts = 0

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}.")

        while True:
            try:
                # Get the player's guess
                player_guess = int(input("Enter your guess: "))
                self.attempts += 1

                # Check if the guess is correct
                if player_guess == self.secret_number:
                    print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                    break
                elif player_guess < self.secret_number:
                    print("Try a higher number.")
                else:
                    print("Try a lower number.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    game = NumberGuessingGame(1, 100)  # Set the range for the game
    game.play()
