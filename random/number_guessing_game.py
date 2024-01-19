import random

def number_guessing_game():
    while True:
        # Generate a random number between 0 and 100
        secret_number = random.randint(0, 100)
        
        # Set the maximum number of chances
        max_chances = 5
        current_chances = max_chances
        
        print("Welcome to the Number Guessing Game!")
        print(f"Guess the number between 0 and 100. You have {max_chances} chances.")

        while current_chances > 0:
            # Get user input for the guess
            user_guess = int(input(f"Enter your guess ({current_chances} chances left): "))

            # Check if the guess is correct
            if user_guess == secret_number:
                print("Congratulations! You guessed the correct number.")
                break
            elif user_guess < secret_number:
                print("The number is higher. Try again.")
            else:
                print("The number is lower. Try again.")

            # Decrease the remaining chances
            current_chances -= 1

        else:
            print(f"Sorry, you've run out of chances. The correct number was {secret_number}.")

        # Ask the player if they want to play again
        play_more = input("Do you want to play again? (yes/no): ").lower()
        if play_more != 'yes':
            print("Thank you for playing. Goodbye!")
            break

# Run the game
number_guessing_game()
