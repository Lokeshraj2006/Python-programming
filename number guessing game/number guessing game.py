import random

def get_valid_guess():
    while True:
        guess = input("Enter your guess (an integer): ")
        try:
            return int(guess)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = get_valid_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    try:
        number_guessing_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        exit(0)