# Number Guessing Game 

## Description

This is a simple Python-based **command-line number guessing game** where the computer randomly selects a number between 1 and 100. The player has to guess the number with hints provided after each attempt.

The game includes:
- Random number generation
- Input validation
- Attempt tracking
- Graceful exit on keyboard interrupt

---

## Features

- Randomly selects a number between 1 and 100
- Prompts the user until the correct guess is made
- Provides feedback ("Too low", "Too high") on each guess
- Tracks and displays the number of attempts taken
- Handles invalid input (non-integer entries)
- Handles keyboard interruption (Ctrl+C) cleanly

---

## Functions Used

| Function Name        | Purpose                                                    |
|---------------------|------------------------------------------------------------|
| `get_valid_guess()` | Continuously asks for input until a valid integer is given |
| `number_guessing_game()` | Contains the game logic, generates the random number, compares guesses, and counts attempts |

---

## Program Flow

1. The program starts by selecting a **random number** from 1 to 100 using:
   ```python
   number_to_guess = random.randint(1, 100)

**Output**

![num guessing op](https://github.com/user-attachments/assets/505b9327-319e-4ed0-997d-9b46521cbf90)

