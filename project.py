import random

class guessing_game:
    def __init__(self, min_number, max_number):
        self.min_number = min_number
        self.max_number = max_number
        self.secret_number = random.randint(min_number, max_number)
        self.attempts = 0

    def play(self):
        print("Welcome to the Number Guessing Game!")
       
        while True:
            try:
                # Get the player's guess
                player_guess = int(input("Enter your guess: "))
                self.attempts += 1

                # Check if the guess is correct
                if player_guess == self.secret_number:
                    print(f"Congratulations! You have guessed the number correctly  {self.secret_number} in {self.attempts} attempts.")
                    break
                elif player_guess < self.secret_number:
                    print("Try a higher number.")
                else:
                    print("Try a lower number.")
            except ValueError:
                print("Please enter a valid number!!.")

if __name__ == "__main__":
    game = guessing_game(1,50)  # Setting the range for the game
    game.play() #calling the play function 
