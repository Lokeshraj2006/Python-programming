# Rock, Paper, Scissors Game

## Description

This is a simple **command-line version of the classic Rock, Paper, Scissors game** built using Python. The player competes against the computer, which randomly selects its move. The game continues until the player decides to stop.

---

## Features

- Allows user to select one of: rock, paper, or scissors
- Computer randomly selects a move
- Determines winner based on standard rules
- Validates input to ensure correct choices
- Offers replay option after each round

---

## Game Rules

- **Rock beats Scissors**
- **Scissors beats Paper**
- **Paper beats Rock**
- Same choices result in a tie

---

## Functions Used

| Function Name             | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| `get_user_choice(choices)` | Gets and validates user input until a valid choice is entered           |
| `determine_winner(user, computer)` | Compares user and computer choices and returns the winner or a tie |
| `play_game()`             | Controls the game loop and manages player vs computer interaction       |

---

## How the Program Works

1. The user is prompted to enter `"rock"`, `"paper"`, or `"scissors"`.
2. Input is validated to ensure it matches one of the allowed options.
3. The computer randomly selects one of the three choices.
4. Both choices are compared using the `determine_winner` function.
5. The result is printed.
6. The user is then asked if they want to play again. If they answer `"yes"`, the game restarts; otherwise, it exits with a thank-you message.

---

## Sample Output

![rps op](https://github.com/user-attachments/assets/dd1b55b2-dfba-41b5-a1f5-ea052e8deb45)
