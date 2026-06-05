
import random


class NumberGuess:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.tries = -1
        self.game_over = False

    def check_guess(self, guess):
        if guess < self.number:
            self.tries += 1
            return "Too low!"
        
            
        elif guess > self.number:
            self.tries += 1
            return "Too high!"
        
        else:
            self.tries += 1 
            return "Correct!"
    
    def previous_guess(self, past_guess):
        if past_guess < self.number:
            return f"Your guess should be in between {past_guess} and 100."
        elif past_guess > self.number:
            return f"Your guess should be in between 1 and {past_guess}."


        
    
        

        
        
game = NumberGuess()

print("Welcome to the Number Guessing Game!\n")

while True:
    user_input = input("Enter your guess (1-100): ")
    result = game.check_guess(int(user_input))
    if result == "Correct!":
        print(f"Congratulations! You have guessed the number in {game.tries} {'try' if game.tries == 1 else 'tries'}!")
        break

    elif user_input != "Correct!":
        print("Try again!\n\n")
        print(game.previous_guess(int(user_input)))
        continue

        

