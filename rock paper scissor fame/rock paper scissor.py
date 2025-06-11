import random

def get_user_choice(choices):
    while True:
        user_input = input("Enter your move (rock, paper, scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid input. Please choose from rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = get_user_choice(choices)
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        replay = input("Play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()